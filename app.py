import streamlit as st
import pandas as pd
import numpy as np

st.title('탭과 사이드바 활용 📑')

# 사이드바
st.header('1. 사이드바 활용')

st.sidebar.title('사이드바 메뉴')
st.sidebar.write('다양한 옵션을 선택하세요.')

# 사이드바 입력 요소
view_mode = st.sidebar.radio('보기 모드 선택:', ['기본 보기', '고급 보기'])
data_filter = st.sidebar.slider('데이터 필터링:', 0, 100, 50)
show_code = st.sidebar.checkbox('코드 표시')

# 선택에 따른 내용 표시
st.write(f"선택한 보기 모드: {view_mode}")
st.write(f"필터 값: {data_filter}")

if show_code:
    st.code("""
    st.sidebar.title('사이드바 메뉴')
    view_mode = st.sidebar.radio('보기 모드 선택:', ['기본 보기', '고급 보기'])
    """)

# 구분선 추가
st.sidebar.divider()
st.sidebar.caption('© 2025 Streamlit 데모')

# 탭 인터페이스
st.header('2. 탭 인터페이스')

tab1, tab2, tab3 = st.tabs(["차트", "데이터", "설정"])

with tab1:
    st.header("차트 탭")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.line_chart(chart_data)

with tab2:
    st.header("데이터 탭")
    st.dataframe(chart_data)

with tab3:
    st.header("설정 탭")
    st.write("차트 설정을 변경하세요.")
    
    chart_type = st.selectbox(
        "차트 유형 선택",
        ["선 차트", "막대 차트", "영역 차트"]
    )
    
    use_container_width = st.checkbox("전체 너비 사용", value=True)