import streamlit as st
from resume_helper import get_resume_feedback

st.set_page_config(page_title="AI Resume Helper")

st.title("AI Resume Helper")
st.write("Paste your resume below to get improvement suggestions from AI.")

resume_text = st.text_area("Resume Text", height=300)

if st.button("Get AI Feedback"):
    if resume_text:
        with st.spinner("Analyzing..."):
            feedback = get_resume_feedback(resume_text)
        st.subheader("AI Suggestions")
        st.write(feedback)
    else:
        st.warning("Please enter your resume first.")
