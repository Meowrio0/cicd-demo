from flask import Flask, jsonify, request

app = Flask(__name__)


def add(a: float, b: float) -> float:
    return a + b


def multiply(a: float, b: float) -> float:
    return a * b


@app.get("/health")
def health():
    return jsonify(status="ok")


HOME_PAGE = """<!doctype html>
<html lang="zh-Hant">
<head><meta charset="utf-8"><title>CI/CD Demo</title></head>
<body style="font-family: sans-serif; max-width: 640px; margin: 40px auto;">
<h1>CI/CD Demo</h1>
<p>這個網站由 GitHub Actions 自動測試、打包，核准後部署到 Render。</p>
<h2>組員</h2>
<ul>
<li>朱宸立（PO）</li>
<li>王柏森（SM）</li>
<li>Louis Imbert</li>
<li>Axel Bauer</li>
<li>林健勛</li>
</ul>
<h2>加法</h2>
<form action="/add" method="get">
<input name="a" type="number" step="any" value="2"> +
<input name="b" type="number" step="any" value="3">
<button type="submit">計算</button>
</form>
<p><a href="/health">/health</a></p>
</body>
</html>
"""


@app.get("/")
def home():
    return HOME_PAGE


@app.get("/add")
def add_route():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(result=add(a, b))


@app.get("/multiply")
def multiply_route():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(result=multiply(a, b))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
