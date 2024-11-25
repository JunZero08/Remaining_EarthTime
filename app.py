from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

# 초기값 설정
initial_y = 500000  # 초기 남은 시간 (단위: 초)

# 지구 멸망 시간 계산 함수
def calculate_remaining_time(a, b, c, d, e):
    return initial_y - (0.3 * a + 0.1 * b + 0.05 * c + 0.02 * d) + 0.1 * e

@app.route("/", methods=["GET", "POST"])
def index():
    remaining_time = None
    if request.method == "POST":
        # 사용자 입력 가져오기
        try:
            a = float(request.form.get("a", 0))  # 탄소 배출량
            b = float(request.form.get("b", 0))  # 자연재해 발생 빈도
            c = float(request.form.get("c", 0))  # 산업화 및 도시화 비율
            d = float(request.form.get("d", 0))  # 사회적 무관심 비율
            e = float(request.form.get("e", 0))  # 환경 복원 활동 비율

            # 남은 시간 계산
            remaining_time = calculate_remaining_time(a, b, c, d, e)
        except ValueError:
            remaining_time = "올바른 숫자를 입력해주세요."

    return render_template("index.html", remaining_time=remaining_time)

if __name__ == "__main__":
    app.run(debug=True)
    