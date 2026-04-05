import streamlit as st

# 로직 함수
def analyze_text(user_input):
    text_length = len(user_input)
    word_count = len(user_input.split())
    
    if word_count < 5:
        comment = "조금 짧은 문장이네요. 내용을 더 보완해 볼까요?"
    elif word_count < 20:
        comment = "적당한 길이의 문장입니다."
    else:
        comment = "꽤 긴 문장이네요. 핵심만 줄여 보는 것도 좋겠습니다."
    
    return text_length, word_count, comment

# 스트림릿 화면 구성
st.title("💡 텍스트 길이와 단어 수 분석기")

user_input = st.text_area("분석할 문장을 입력하세요.", height=150)

if st.button("분석하기"):
    if user_input.strip():
        length, count, comment = analyze_text(user_input)
        
        col1, col2 = st.columns(2)
        with col1:
            st.success(f"📏 문장 길이: {length}자")
        with col2:
            st.info(f"📝 단어 수: {count}개")
            
        st.write("---")
        st.subheader("🧐 분석 결과")
        st.write(comment)
    else:
        st.warning("문장을 입력해 주세요!")
