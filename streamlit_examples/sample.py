import streamlit as st

st.title("RAG Agent")

with st.sidebar:
    st.header("Sidebar")
    with st.form("api_credentials"):
        openai_key = st.text_input("OpenAI Key", type="password")
        openai_url = st.text_input("URL")
        azure_openai = st.radio(options=["azure", "openai"], label="LLM Model hosting")

        if st.form_submit_button("Submit Credentials"):
            print(openai_key)

    st.divider()

