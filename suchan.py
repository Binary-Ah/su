import turtle as t
import time

# 화면 설정
t.setup(width=800, height=500)
t.bgcolor("black") # 킹 받는 블랙 배경
t.title("코코몽")

# 첫 번째 문구 (수찬아 힘내)
t.speed(2)
t.pensize(5)
t.keyup()
t.goto(-250, 50) # 글씨 쓸 위치로 이동
t.color("#00ff00") # 네온 초록

# 텍스트 쓰기
t.write("수찬아 힘내라! 💪", font=("궁서", 45, "bold"))

# 잠시 대기 후 명언 발사
time.sleep(1)

# 두 번째 문구 (최애 명언)
t.keyup()
t.goto(-320, -50)
t.color("yellow") # 눈에 띄는 노란색
t.write("🌹 향기로운 수찬은 늠름하게 핀다 🌹", font=("궁서", 25, "bold"))

# 거북이 숨기기 및 창 유지
t.hideturtle()
print("수찬아 힘내라!!!")
t.done()