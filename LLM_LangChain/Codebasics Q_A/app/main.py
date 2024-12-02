import streamlit as st
from utils import get_qa_chain

st.title('Codebasics QA ❓')
st.button('Create Knowledgebase')
if st.button:
    pass
question = st.text_input('Question:')

if question:
    chain = get_qa_chain()
    response = chain.invoke(question)

    st.header("Answer: ")
    st.text(response['result'])