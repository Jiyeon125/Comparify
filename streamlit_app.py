import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="Comparify", page_icon="🔍", layout="wide")

# 헤더
st.markdown(
    "<h1 style='text-align: center; color: #000033;'>Comparify</h1>", 
    unsafe_allow_html=True
)
st.caption("상품 리뷰를 비교하고 요약합니다.")

# 검색 영역
product = st.text_input("찾고 싶은 상품을 입력하세요")

if st.button("상품 분석하기"):
    # (여기에 분석 결과 보여주는 코드 추가)
    st.subheader(f"'{product}'에 대한 리뷰 요약")
    st.write("요약된 리뷰 내용이 여기에 표시됩니다.")

    st.subheader("주요 키워드")
    st.write(["키워드1", "키워드2", "키워드3"])

    st.metric("평점", "4.5/5.0")
    st.metric("리뷰 수", "120개")

    st.markdown("[Amazon에서 보기](https://www.amazon.com)")



# 하단
st.markdown(
    "<hr style='border:1px solid #B0E5B0;'>", unsafe_allow_html=True
)
st.caption("Comparify © 2025. Powered by Streamlit.")

