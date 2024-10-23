import streamlit as st 

st.set_page_config(page_title="연수 연습용", page_icon="❤️") 

st.title("형성평가")
st.header("점수에 들어가지 않는 연습용 평가입니다.")
st.write("수시로 들어와 배운 내용을 확인해봅시다.")

option = st.radio("옳은 것은?", ("1", "2", "3", "4"))  
option = st.selectbox("모두 고르시오", ("1", "2", "3", "4"))

agree = st.checkbox("동의하세요?")
if agree:
    st.write("동의하셨군요")
else:
    st.write("동의해주세요.")

option = st.checkbox(("동의"), ("비동의")) 

checkbox_state = st.checkbox("이 옵션을 선택하세요", value=True)

if checkbox_state:
    st.write("체크박스가 이미 선택되었습니다!")
else:
    st.write("체크박스를 선택해보세요.")

option2 = st.radio("학교는 어디에 있나요?", ("영등포구", "금천구", "구로구"))
if option2== "구로구":
    st.success("정답~")
    #st.balloons()
elif option2=="영등포구":
     st.error("다시 풀어보기~")
     #st.snow()
elif option2=="금천구":
     st.error("다시 풀어보기~")
     
     
agreement = st.radio("동의하십니까?", ("동의", "비동의"))
# 선택에 따른 메시지 출력
if agreement == "동의":
    st.write("사용자가 동의했습니다.")
else:
    st.write(
    st.write

