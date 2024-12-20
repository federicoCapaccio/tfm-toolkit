# Import Libraries
import streamlit as st
from streamlit_chat import message

# Open API key


# Generating responses from the api

def generate_response(prompt):
   
    return "Hi, I am not able to answer yet, but I'll learn soon!"

# Creating the chatbot interfaces

st.title("The Frontier MINDS Toolkit")

# Storing the input

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

# Creating a function that returns the user's input from a text input field

def get_text():
    input_text = st.text_input("You : ", "", key = "input")
    return input_text

# We will generate response using the 'generate response' function and store into variable called output

user_input = get_text()

if user_input:
    output = generate_response(user_input)

    # Store the output
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)


# Finally we display the chat history

if st.session_state['generated']:

    for i in range(len(st.session_state['generated']) -1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
