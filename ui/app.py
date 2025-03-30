import streamlit as st

st.title("RAG Similarity Search Agent")

if "llm_url" not in st.session_state:
    st.session_state.llm_url = ""
if "llm_access_key" not in st.session_state:
    st.session_state.llm_access_key = ""
if "llm_type" not in st.session_state:
    st.session_state.llm_type = ""

with st.sidebar:
    st.header("Api Credentials")
    with st.form("api_credentials"):
        llm_type = st.radio(options=["azure", "openai"], label="LLM Model hosting")
        llm_key = st.text_input(f"{llm_type} Key", type="password")
        llm_url = st.text_input(f"{llm_type} URL")

        if st.form_submit_button("Submit Credentials"):
            if st.session_state.llm_url != llm_url:
                st.session_state.llm_url = llm_url
            if st.session_state.llm_access_key != llm_key:
                st.session_state.llm_access_key = llm_key
            if st.session_state.llm_type != llm_type:
                st.session_state.llm_type = llm_type

    st.divider()

