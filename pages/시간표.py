import streamlit as st
import pandas as pd

st.title("📚 시간표")

grade = st.selectbox("학년을 선택하세요", ["1학년", "2학년", "3학년"])

timetable = {
    "과목": ["국어", "수학", "영어", "과학", "체육"]
}

df = pd.DataFrame(timetable)

st.subheader(f"{grade} 시간표")
st.table(df)
