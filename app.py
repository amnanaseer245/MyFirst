import os
import streamlit as st
import google.generativeai as genai


GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)


model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🎓 Education AI Student Assistant")
st.write("You can ask your academic questions here!")

student_name = st.text_input("Your Name:")
student_email = st.text_input("Your Email:")
student_query = st.text_area("Your Question or Request:")

if st.button("Submit Request"):
    if student_name and student_query:
        with st.spinner("Processing..."):
            response = model.generate_content(student_query)
            st.success("Your answer is ready!")
            st.write(response.text)
    else:
        st.warning("Please fill in your name and question!")
