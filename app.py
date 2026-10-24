
"""Modul backend autentikasi Flask untuk pengujian pipeline."""

import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


def init_db():
    """Inisialisasi basis data untuk demonstrasi login."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users "
        "(username TEXT, password TEXT)"
    )
    cursor.execute(
        "INSERT INTO users (username, password) "
        "SELECT ?, ? WHERE NOT EXISTS "
        "(SELECT 1 FROM users WHERE username = ?)",
        ("admin", "supersecret", "admin"),
    )
    conn.commit()
    conn.close()


@app.route("/", methods=["GET", "POST"])
def index():
    """Menampilkan formulir login dan memproses autentikasi."""
    message = None
    status_class = None

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        # Parameterized query untuk mencegah SQL Injection.
        query = (
            "SELECT * FROM users "
            "WHERE username = ? AND password = ?"
        )
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            message = "Login berhasil."
            status_class = "success"
        else:
            message = "Login gagal. Kredensial tidak valid."
            status_class = "danger"

    return render_template(
        "index.html",
        message=message,
        status_class=status_class,
    )


if __name__ == "__main__":
    init_db()
    # Host 0.0.0.0 diperlukan agar port container dapat diakses.
    # Pengecualian ini khusus untuk konfigurasi jaringan lab.
    app.run(host="0.0.0.0", port=5000)  # nosemgrep
