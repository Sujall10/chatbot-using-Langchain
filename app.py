

import streamlit as st
from langchain import HuggingFaceHub
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Hugging Face model
llm_hugging = HuggingFaceHub(
    repo_id="google/flan-t5-large",
    model_kwargs={"temperature": 0, "max_length": 1024},
)

# Streamlit app setup
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")

# Initialize session state
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = []

# Function to get response from Hugging Face model
def get_hugg_response(question):
    # Add user message to the chat history
    st.session_state['flowmessages'].append(f"User: {question}")
    
    # Get the response from the model
    response = llm_hugging(question)
    
    # Add the AI's response to the chat history
    st.session_state['flowmessages'].append(f"AI: {response}")
    
    return response

# User input and button
user_input = st.text_input("Ask your question:")
if st.button("Ask"):
    if user_input.strip():
        # Get the response and display it
        response = get_hugg_response(user_input)
        st.subheader("The response is:")
        st.write(response)
    else:
        st.warning("Please enter a valid question.")

# Display chat history
if st.session_state['flowmessages']:
    st.subheader("Chat History:")
    for message in st.session_state['flowmessages']:
        st.write(message)
