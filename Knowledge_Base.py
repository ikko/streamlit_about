import uuid

import streamlit as st
import streamlit.components.v1 as components
import streamlit_mermaid

from dynamic_pages.courses import st_courses
from dynamic_pages.main import st_main_page
from dynamic_pages.mindmap import st_mindmap, small_mindmap


# Page setup
st.set_page_config(page_title="RAG Q&A Explorer of Miklos", page_icon="📖", layout="wide")
if "session_id" not in st.session_state:
    st.session_state.session_id = uuid.uuid4().hex[:8]
st.title("📖 RAG Q&A Explorer of Miklos")

# Load CSS for styling expander labels in courses
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with st.sidebar as sidebar:
    # Mindmap in sidebar
    st.markdown(
        'Look at the <a href="/?_page=mindmap" target="_self">Detailed Mindmap</a>!', unsafe_allow_html=True
        )
    streamlit_mermaid.st_mermaid(small_mindmap())
    st.divider()

    # Courses in sidebar
    st.markdown(
        'View <a href="/?_page=certs" target="_self">Completed Courses</a>!', unsafe_allow_html=True
        )
    left_column, middle_column, right_column = st.columns([1, 1, 1])
    with left_column:
        st.image("images/icon_python.png")
    with middle_column:
        st.image("images/icon_databricks.png")
    with right_column:
        st.image("images/icon_business.png")
    st.divider()

    # Draw attention to Topic Clusters in sidebar
    st.success("📂 Navigate through **Topic Clusters** using this sidebar at the top!")


# Loaded the mindmap_page in the previous request
# so this time load the main page
if st.session_state.get("mindmap_page_loaded", False) is True:
    st.query_params["_page"] = "main"
if st.session_state.get("courses_page_loaded", False) is True:
    st.query_params["_page"] = "main"

# Page routing
if st.query_params.get("_page", "main") == "main" :
    st.session_state["mindmap_page_loaded"] = False
    st.session_state["courses_page_loaded"] = False
    st_main_page()
elif st.query_params.get("_page", "main") == "mindmap":
    st.session_state["mindmap_page_loaded"] = True
    st.session_state["courses_page_loaded"] = False
    st_mindmap()
elif st.query_params.get("_page", "main") == "certs":
    local_css("style.css")
    st.session_state["mindmap_page_loaded"] = False
    st.session_state["courses_page_loaded"] = True
    st_courses()

# Focus browser to chat input area
# This is a streamlit workaround
def callback():
    st.session_state['counter'] += 1
if 'counter' not in st.session_state:
    st.session_state['counter'] = 0
components.html(
    f"""
        <div hidden style='visibility:hidden; overflow:hidden; position:absolute;'>some hidden container</div>
        <p hidden style='visibility:hidden; overflow:hidden; position:absolute;'>{st.session_state.counter}</p>
        <script>
            function focusInput() {{
                const input = window.parent.document.querySelector('textarea');
                if (input) {{
                    console.log('Input found. Focusing...');
                    input.focus();
                }} else {{
                    console.log('Input not found. Retrying in 100ms...');
                    setTimeout(focusInput, 100);
                }}
            }}
            focusInput();
        </script>
    """,
    height=0,
)
