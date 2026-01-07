import streamlit as st

st.title("📇 담당자 목록")

st.write("담당자를 선택하면 가상 이메일을 확인할 수 있습니다.")

teachers = {
    "김민수 (교무부)": "minsu.kim@ooschool.edu",
    "이서연 (학생부)": "seoyeon.lee@ooschool.edu",
    "박준호 (행정실)": "junho.park@ooschool.edu",
    "최은지 (상담교사)": "eunji.choi@ooschool.edu"
}

selected = st.selectbox("담당자를 선택하세요", list(teachers.keys()))

st.subheader("📧 이메일")
st.code(teachers[selected])
