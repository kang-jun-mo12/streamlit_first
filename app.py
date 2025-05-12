import streamlit as st

st.title("🧠 간단한 퀴즈 테스트")
st.subheader("객관식 + 주관식 퀴즈 2개")

st.markdown("## 🔸 1. 객관식 문제")
q1 = st.radio(
    "Q1. 파이썬의 창시자는 누구인가요?",
    ["Guido van Rossum", "Elon Musk", "Bill Gates", "Linus Torvalds"]
)

if q1:
    if q1 == "Guido van Rossum":
        st.success("정답입니다! 🎉")
    else:
        st.error("오답입니다. 🥲")

st.markdown("## 🔸 2. 주관식 문제")
q2 = st.text_input("Q2. 대한민국의 수도는?")

if q2:
    if q2.strip().lower() in ["서울", "seoul"]:
        st.success("정답입니다! 🎉")
    else:
        st.error("오답입니다. 다시 생각해보세요! ❌")
