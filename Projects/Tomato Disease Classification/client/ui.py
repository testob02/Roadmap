import streamlit as st
import utils

st.set_page_config(layout='centered',page_title="Tomato Disease Classification",page_icon="🍅🍀")

st.markdown(
"""
<style> 
.stDeployButton {
    visibility: hidden;
}
#MainMenu {
    visibility: hidden;
}
div.stButton{
    text-align: center
}

</style>
""", unsafe_allow_html=True)


st.markdown('<h1 style="color:green;text-align:center">Tomato Leaf Disease Classification</h1>',unsafe_allow_html=True)
st.write('---')

uploaded_file = st.file_uploader(':green[**Upload a tomato leaf image**]', type=['png','jpg'], accept_multiple_files=False)
predict = st.button(':green[**Classify Image**]')

st.write('---')
   
col1, col2 = st.columns([0.6,0.4],vertical_alignment='center')
if uploaded_file is not None :
    if predict:
        with col1:
            st.image(uploaded_file,width=400) 
        with col2:
            with st.spinner('Classifying'):
                cls, confidence = utils.classify(uploaded_file)
            st.write('<div style="color:green;font-size:20px;text-align:center;font-weight:bold;text-decoration:underline">Predicted Class</div>',unsafe_allow_html=True)
            st.write('')
            st.write('')
            st.write(f'<div id="cls_div" style="color:green;font-size:20px;text-align:center;font-weight:bold">{cls}</div>',unsafe_allow_html=True)
            st.write('---')    
            st.write('<div style="color:green;font-size:20px;text-align:center;font-weight:bold;text-decoration:underline">Confidence</div>',unsafe_allow_html=True)
            st.write('')
            st.write('')
            st.write(f'<div id="conf_div" style="color:green;font-size:20px;text-align:center;font-weight:bold">{confidence}%</div>',unsafe_allow_html=True)