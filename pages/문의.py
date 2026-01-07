import streamlit as st

st.title("📬 문의하기")

name = st.text_input("이름")
email = st.text_input("이메일")
message = st.text_area("문의 내용")

if st.button("제출"):
    if name and email and message:
        st.success("문의가 접수되었습니다. 감사합니다!")
    else:
        st.error("모든 항목을 입력해주세요.")
