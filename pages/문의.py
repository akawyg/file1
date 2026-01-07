import streamlit as st

st.title("📬 문의하기")

st.write("문의 사항이 있으면 아래 양식을 작성하거나 담당자에게 직접 연락할 수 있습니다.")

st.page_link(
    "5_담당자목록.py",
    label="📇 담당자 목록 바로가기",
    icon="➡️"
)

st.divider()

name = st.text_input("이름")
email = st.text_input("이메일")
message = st.text_area("문의 내용")

if st.button("제출"):
    if name and email and message:
        st.success("문의가 접수되었습니다. 감사합니다!")
    else:
        st.error("모든 항목을 입력해주세요.")
