import streamlit as st
from utils import clean_text
from chains import Chain
from portfolio import Portfolio
from langchain_community.document_loaders import WebBaseLoader

st.set_page_config('Cold Mail Generator :email:',layout='wide')

st.title('Cold Mail Generator :email:')
url_input = st.text_input('Enter a URL:',value='https://jobs.nike.com/job/R-44279?from=job%20search%20funnel')
submit = st.button('Submit')

portfolio = Portfolio()
chain = Chain()

if submit:
    try:
        loader = WebBaseLoader([url_input])
        data = loader.load().pop().page_content
        clean_data = clean_text(data)
        portfolio.load_portfolio()
        jobs = chain.extract_jobs(clean_data)
        for job in jobs:
            skills = job.get('skills')
            links = portfolio.query_links(skills)
            mail = chain.write_mail(job,links)
            st.code(mail,language='markdown',wrap_lines=True)
    except Exception as e:
        st.error(f'Error Occurred {e}')
