import streamlit as st
import math

# 1. 로직 함수
def calculate_membership_fee(total_amount, num_people, tip_percentage):
    # 팁 포함 전체 금액 계산 (소수점 버림)
    total_with_tip = math.floor(total_amount * (1 + tip_percentage / 100))
    
    # 인원 수로 나누어 1인당 금액 계산
    if num_people and num_people > 0:
        per_person = total_with_tip / num_people
        # 1000단위 반올림 (예: 12500 -> 13000)
        per_person_rounded = round(per_person, -3)
    else:
        per_person_rounded = 0

    return per_person_rounded, total_with_tip

# 2. 스트림릿 화면 구성
st.set_page_config(page_title="회비 계산기", page_icon="💰")
st.title("💰 모임 회비 관리 계산기")
st.write("간편하게 총 금액과 인원수를 입력하여 회비를 계산해 보세요.")

# 3. 입력 구역
with st.container():
    st.subheader("📌 정보 입력")
    total_amount = st.number_input("총 금액 (원)", min_value=0, step=1000, value=50000)
    num_people = st.number_input("인원 수 (명)", min_value=1, step=1, value=4)
    
    # [수정 포인트] maximum -> max_value 로 변경되었습니다.
    tip_percentage = st.slider("팁/서비스 비율 (%)", min_value=0, max_value=20, value=0, step=1)

# 4. 계산 버튼 및 결과 출력
if st.button("회비 계산하기", type="primary"):
    per_person, total_all = calculate_membership_fee(total_amount, num_people, tip_percentage)
    
    st.write("---")
    st.subheader("📊 계산 결과")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="1인당 회비 (1000단위 반올림)", value=f"{int(per_person):,} 원")
    with col2:
        st.metric(label="팁 포함 총 금액", value=f"{int(total_all):,} 원")
        
    st.success(f"총 {num_people}명이서 각각 {int(per_person):,}원씩 걷으면 됩니다!")
