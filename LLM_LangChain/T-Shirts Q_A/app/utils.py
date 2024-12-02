import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import FewShotPromptTemplate, SemanticSimilarityExampleSelector
from langchain.prompts.prompt import PromptTemplate
from langchain.chains.sql_database.prompt import _mysql_prompt, PROMPT_SUFFIX
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from few_shot import few_shots

load_dotenv()
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
api_key = os.getenv('GROQ_API_KEY')

def get_few_shot_db_chain():

    llm = ChatGroq(model="llama-3.1-70b-versatile",
               api_key=api_key,
               temperature=0.1)
    
    db_user = "root"
    db_password = "root"
    db_host = "127.0.0.1"
    db_name = "atliq_tshirts"

    db = SQLDatabase.from_uri(f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}')

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    to_vectorize = [" ".join(example.values()) for example in few_shots]
    vectorstore = Chroma.from_texts(
    texts = to_vectorize,
    embedding=embeddings,
    metadatas=few_shots
                        )
    
    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vectorstore,
        k=2
                    )
    
    example_prompt = PromptTemplate(
    input_variables=["Question","SQLQuery","SQLResult","Answer"],
    template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}"
        )
    

    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=_mysql_prompt + """
            \nReturn the result of the query execution. Do not include the SQLQuery or any explanations. You can add little preamble text to communicate the answer properly.
            Make sure to use absolutely only the information present gotten from the SQLResult
                                """,
        suffix=PROMPT_SUFFIX + """
            \nReturn the result of the query execution. Do not include the SQLQuery or any explanations. You can add little preamble text to communicate the answer properly.
            Make sure to use absolutely only the information present gotten from the SQLResult
                                """,
        input_variables=["input","table_info","top_k"]
        )
    
    chain = SQLDatabaseChain.from_llm(
                llm=llm,
                db=db,
                prompt=few_shot_prompt,  
                verbose=True
                )
    
    return chain

# def get_response(question):
#     chain = get_few_shot_db_chain()
#     return chain.invoke(question)

# if __name__ == "__main__":
#     print(get_response("What brand of t-shirts will make the most money if they are all sold and how much will it make"))