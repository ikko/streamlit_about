import streamlit as st
from pathlib import Path

ACCOMPLISHMENTS_DIR = Path("accomplishments")

@st.cache_data
def get_description(course_dir):
    sum_file = course_dir / "summary.md"
    icon = course_dir / "icon.png"
    image = course_dir / "statement-of-accomplishment.png"
    certificate = course_dir / "certificate.png"
    summary = sum_file.read_text()
    return icon, image, summary, certificate


def display_course(course_dir):
    course_title = str(course_dir.name)
    icon, image, summary, certificate = get_description(course_dir)
    left_column, right_column = st.columns([1, 4])
    with left_column:
        st.image(icon)

    with right_column:
        with st.expander(course_title):
            image_columns, content_column = st.columns([2, 3])
            with image_columns:
                st.image(image)
            with content_column:
                st.markdown(summary)

            _, right = st.columns([1, 4])
            with right:
                st.image(certificate, use_container_width=True)


@st.cache_data
def main():
    st.markdown("## 📚 Completed Courses")
    courses = sorted([d for d in ACCOMPLISHMENTS_DIR.iterdir() if d.is_dir()], key=lambda x: x.name.lower())
    st.divider()
    for course in courses:
        display_course(course)

def st_courses():
    main()
