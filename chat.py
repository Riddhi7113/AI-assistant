import streamlit as st
from api_call import getResponse  # Import the function to get the response

st.title("Chubby🤖")

# Initialize messages list if it's not already in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages in the chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input and generate the response
if prompt := st.chat_input("What is up?"):
    # Append the user's message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display the user's message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate the assistant's response
    response = getResponse(prompt)
    
    # Append the assistant's message to session state
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Display the assistant's response
    with st.chat_message("assistant"):
        st.markdown(response)
