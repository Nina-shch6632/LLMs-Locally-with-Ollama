# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:13:29 2024

@author: ninac
"""
## Run LLMs Locally with Ollama 
import streamlit as st
import ollama

def main():
    st.title("My first LLM practice")
    
    #Set up user input config
    user_input = st.text_area("Your message？","")
    
    #when user press send button
    if st.button("send"):
        if user_input:
            #use ollama model have chat
            response = ollama.chat(model='mistral',messages=[{'role': 'user', 'content': user_input}])
            
            #show respone
            st.text("Respone：")
            st.write(response['message']['content'])
        else:
            st.warning("Please enter your question！")
            
if __name__ == "__main__":
    main()
