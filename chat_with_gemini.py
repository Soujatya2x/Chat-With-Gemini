import streamlit as st
import google.generativeai as genai
import subprocess

genai.configure(api_key="API_KEY") # Replace with your API key.
model = genai.GenerativeModel('gemini-2.0-flash') 


st.title("chat with google gemini")
st.write("this app runs gemini-2.0 flash model")


def conversation():

    query=st.text_input("enter your query")
    
    if st.button("enter"):
        response = model.generate_content(query)
        #with st.popover("see result"):
        #st.markdown("here is your answer")
        st.write(response.text)
   

conversation()







