import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv


load_dotenv()

key = os.getenv('GROQ_API_KEY')

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
        model="llama-3.1-70b-versatile",
        api_key=key,
        temperature=0
                        )
        
    def extract_jobs(self,cleaned_text):
        prompt_extract = PromptTemplate.from_template(
                        """
                        ### SCRAPED TEXT FROM WEBSITE:
                        {page_data}
                        ### INSTRUCTION:
                        The scraped text is from the career's page of a website. Your job is to extract the job postings and return them in JSON format
                        containing the following keys: 'role', 'experience', 'skills' and 'description'
                        Only return the valid JSON
                        VALID JSON NO PREAMBLE
                        JUST THE JSON
                        DONT ADD ```
                        """
                                    )
        chain_extract = prompt_extract | self.llm
        response = chain_extract.invoke(input={'page_data':cleaned_text})
        try:
            json_parser = JsonOutputParser()
            json_response = json_parser.parse(response.content)
        except OutputParserException:
            raise OutputParserException('Context too big. Unable to pass jobs')
        
        return json_response if isinstance(json_response, list) else [json_response]
    
    def write_mail(self,job,links):
        prompt_email = PromptTemplate.from_template(
                        """ 
                        JOB DESCRIPTION
                        {job_description}

                        ### INSTRUCTION:
                        You are Teslim, a business development executive at TestDev Inc. TestDev Inc. is an AI & SOftware company
                        that brings about the seamless integration of business processes through automated tools.
                        Over our experience, we have empowered numerous enterprises with tailored solutions such as process optimization,
                        cost reduction, and heightened overall eficiency.
                        Your job is to write a cold email to the client regarding the job mentioned above and talk about fulfilling their needs.
                        Also add the most relevant ones from the following links to showcase TestDev Inc. portfolio {link_list}.
                        Remember, you are Teslim, CEO of TestDev Inc.
                        Do not provide a preamble.
                        ### EMAIL (NO PREAMBLE)
                        DONT ADD ```
                        """
                        )
        chain_email = prompt_email | self.llm
        response = chain_email.invoke(input={
                            'job_description':str(job),
                            'link_list':links
                                    })
        
        return response.content