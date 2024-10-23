import streamlit as st

st.title("😊 Streamlit 연수 실습용")
st.subheader("2024. 10. 23. streamlit과 github에 가입 후 연습")
st.write("오른쪽 위의 'fork' 버튼을 눌른 후 원본의 페이지와 앱이 그대로 복사된 것.")

st.link_button("네이버 지식백과 바로가기", "https://terms.naver.com/")


st.success("초록색 창")
st.error("빨간색 창")
st.info("파란색 창")
st.warning("노란색 창") # ctrl+/ : 주석처리
st.image("https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif?cid=790b7611jyo1q4j0g2wbtehx5dm61ms3hiqy5l62jhk385z2&ep=v1_gifs_trending&rid=giphy.gif&ct=g",caption="랄랄라")  

st.success("success가 초록색 창이네")
st.error("error는 빨간색이고")
st.info("info는 파란색")
st.warning("warning은 노란색") 

st.video("https://www.youtube.com/watch?v=Yl3nsVSnlAo") 

