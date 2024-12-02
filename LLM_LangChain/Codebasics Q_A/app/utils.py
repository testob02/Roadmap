import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

load_dotenv()

api_key = os.getenv('GROQ_API_KEY')
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

llm = ChatGroq(model="llama-3.1-70b-versatile",
               api_key=os.getenv('GROQ_API_KEY'),
               temperature=0.6)


embeddings = HuggingFaceEmbeddings()


def create_db():
    data = CSVLoader('faqs.csv',source_column='prompt').load()
    vectordb = Chroma.from_documents(
        documents=data,
        embedding=embeddings,
        persist_directory='vectordb'
        )
    vectordb.persist()                                    

def get_qa_chain():
    vectordb = Chroma(
        embedding_function=embeddings,
        persist_directory='vectordb'
        )
    prompt_template = PromptTemplate.from_template(""" 
                    Given the following context and a question, generate an answer based on this content.
                    In the answer try to provide as much text as possible from "response" section in the source document
                    If the answer is not found in the context, kindly state "I dont know". Do not make up an answer. 
                    Act conversationally and do not use anything like "based on the context"
                    Provide as much text as possible from the source document

                    CONTEXT: {context}

                    QUESTION: {question}                          
                    """)

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=vectordb.as_retriever(),
        input_key="query",
        return_source_documents=True,
        chain_type_kwargs={"prompt":prompt_template}
                                        )
    return chain

