"""Aplikasi Flask untuk praktikum pipeline CI/CD."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """Menampilkan halaman utama."""
    return "<h1>DevSecOps Lab</h1><p>Aplikasi Flask berjalan.</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
