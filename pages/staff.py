import streamlit as st

st.title("📇 담당자 목록")

staff = {
    "Kim Minsoo (Academic Affairs)": "minsoo.kim@ooschool.edu",
    "Lee Seoyeon (Student Affairs)": "seoyeon.lee@ooschool.edu",
    "Park Junho (Administration)": "junho.park@ooschool.edu",
    "Choi Eunji (Counselor)": "eunji.choi@ooschool.edu"
}

selected = st.selectbox("담당자를 선택하세요", list(staff.keys()))

st.subheader("📧 Contact Email")
st.code(staff[selected])
