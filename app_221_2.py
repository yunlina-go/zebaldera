import gradio as gr
import math


def calculate_membership_fee(total_amount, num_people, tip_percentage):
    # 1. 팁 포함 전체 금액 계산 (소수점 버림)
    total_with_tip = math.floor(total_amount * (1 + tip_percentage / 100))

    # 2. 인원 수로 나누어 1인당 금액 계산
    if num_people and num_people > 0:
        per_person = total_with_tip / num_people
        # 3. 100단위에서 반올림
        per_person_rounded = round(per_person, -3)
    else:
        per_person_rounded = 0

    return per_person_rounded, total_with_tip


# Gradio 인터페이스 구성
interface = gr.Interface(
    fn=calculate_membership_fee,
    inputs=[
        gr.Number(label="총 금액(원)"),
        gr.Number(label="인원 수(명)", precision=0),
        gr.Slider(minimum=0, maximum=20, step=1, label="팁/서비스 비율(%)")
    ],
    outputs=[
        gr.Number(label="1인당 금액(원) - 100단위 반올림"),
        gr.Number(label="팁 포함 총 금액(원)")
    ],
    title="모임 회비 관리 계산기",
    # 이 부분이 수정되었습니다: allow_flagging -> flagging_mode
    flagging_mode="never"
)

# 프로그램 실행
if __name__ == "__main__":
    interface.launch()