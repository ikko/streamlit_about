from string import printable

import streamlit as st


def st_main_page():
    st.markdown("""
    ### Reinforcement-Based Answer Generation and Exploration 🔍 
    This is a RAG model prepared for retrieval by query and exploration, __see below and left__. It uses notes from [Miklos Beky](https://www.linkedin.com/in/miklosbeky/).
    - 🎓 Navigate in the left sidebar to explore Q&A **Topic Clusters** identified with **Unsupervised Learning**.
    - 💡 After navigating to a Topic Page, click on any **question** to expand it and read the answer.
    - 🏡 Click on **Knowledge Base** in the top left sidebar to return to this page.
    - 🐧 Examine the [source code](https://github.com/ikko/streamlit_about) in the github repository.
    - 💬 Ask the **RAG** model in the rounded question box below to learn more about Miklos Beky's work.
    """)
    st.success("""
        💬 Ask questions like:
        - 🐍 How comprehensive is Miklos' knowledge about FastAPI?
        - 🤖 What does Miklos know about Machine Learning?
        - ⚙️ What are the software engineering methodologies that Miklos knows and practices?
    """)

    st.session_state.page = "main"
    
    ### Main RAG chat interface
    with st.status("⏳ Loading...", state="running", expanded=True) as status:
        st.write("Loading modules...")

        from backend.rag_base import rag_load_or_create
        from backend.rag_query import query_rag

        st.write("Loading vectors and metadata...")
        if "index" not in st.session_state or "bm25" not in st.session_state or "metadata" not in st.session_state:
            try:
                index, bm25, metadata = rag_load_or_create()
            except Exception as e:
                st.write(f"Error, please reload or come back later {repr(e)}")
                status.update(state="error")
                st.button("Reload")
                st.stop()
            st.session_state.index = index
            st.session_state.bm25 = bm25
            st.session_state.metadata = metadata
        else:
            index = st.session_state.index
            bm25 = st.session_state.bm25
            metadata = st.session_state.metadata

        status.update(
            label="✅ Everything loaded and ready. 🧪 Ask below or 🧭explore on the left!", state="complete",
            expanded=False
            )

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # React to textual user input
    question = st.chat_input("🪄 Ask RAG Model here about Miklos...")
    print("in streamlit main question is:")
    
    # Filter characters of question
    accepted_question = []
    unaccepted_characters = []
    if question:
        for char in list(question):
            if char in list(printable):
                accepted_question.append(char)
            else:
                unaccepted_characters.append(char)
    accepted_question = ''.join(accepted_question)
    unaccepted_characters = ''.join(unaccepted_characters)
    
    if accepted_question:
        with st.status(
                "Getting answer, be patient, this may take a while...",
                state="running",
                expanded=True
        ):
            # Display user message in chat message container
            if unaccepted_characters:
                st.write(f"Use regular English characters only. These are not accepted: '{unaccepted_characters}'")
            st.write("Sending question...")
            with st.chat_message("user"):
                st.markdown(accepted_question)
    
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": question})
    
            # Display assistant response
            st.write("Waiting for the answer...")
            session_id = st.session_state.session_id
            with st.chat_message("assistant") as chat:
                print("In streamlit just before calling backend, the question is:", question)
                response = st.write_stream(query_rag(question, index, bm25, metadata, session_id))
                print("In streamlit just after calling backend, the response is:", response)

            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
