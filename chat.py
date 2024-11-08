import streamlit as st
from api_call import getResponse  

st.title("Chubby🤖")

if "messages" not in st.session_state:
    st.session_state.messages = []

if prompt := st.chat_input("What would you like to chat about?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Use getResponse function from your script
    response = getResponse(prompt)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
