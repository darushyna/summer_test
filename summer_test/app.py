from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    score = 0
    for i in range(1, 8):
        answer = request.form.get(f"q{i}")
        if answer is not None:
            score += int(answer)

    if score >= 4:
        result_text = "🌲 당신은 싱그러운 산 속<br>'강원 영월형 인간'이군요!"
        image = "영월.jpg"
    else:
        result_text = "🌾 당신은 따스한 평야의<br>'충남 당진형 인간'이군요!"
        image = "당진.jpg"

    return render_template("result.html", result=result_text, image=image)

if __name__ == "__main__":
    app.run(debug=True, port=5002)

