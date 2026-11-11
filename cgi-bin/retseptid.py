#!/home/markusmalk/.venv/bin/python3

import sqlite3
import html
from urllib.parse import parse_qs
import os


if os.name == "nt":
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(SCRIPT_DIR, "..", "instance", "retseptid.db")
else:
    DB_PATH = os.path.expanduser("~/public_html/instance/retseptid.db")

print("Content-Type: text/html; charset=utf-8")
print()

print("""
<!DOCTYPE html>
<html lang="et">

<head>
    <meta charset="UTF-8">
    <title>Retseptid</title>
    <link rel="stylesheet" href="/~markusmalk/static/css/style.css">
</head>
""")

params = parse_qs(os.environ.get("QUERY_STRING", ""))
otsi = params.get("otsi", [""])[0]

try:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    retseptid = conn.execute("""
        SELECT id, nimi, pilt
        FROM retseptid
        WHERE nimi LIKE ?
        ORDER BY nimi
    """, (f"%{otsi}%",)).fetchall()

except Exception as e:
    print(f"<pre>VIGA: {html.escape(str(e))}</pre>")
    raise


print(f"""
<body>
<h1 class="bordered">Retseptid</h1>

<form action="/~markusmalk/cgi-bin/retseptid.py" method="GET">
    Otsi:
    <input type="text" name="otsi" value="{html.escape(otsi)}">
    <input type="submit" value="Otsi" class="button">
</form>

<br>
<button type="button" class="collapsible">Filter</button>

<div class="retseptide-grid">
""")

for retsept in retseptid:
    nimi = html.escape(retsept["nimi"])
    pilt = html.escape(retsept["pilt"])
    dieedid = html.escape(retsept["dieedid"])

    print(f"""
    <article class="retsepti-kaart">
        <img class="retsepti-pilt"
             src="/~markusmalk/static/retseptid/{pilt}"
             alt="{nimi}">

        <h2 class="retsepti-nimi">{nimi}</h2>
        <div class="dieedi-grid">{dieedid}</div>
    </article>
    """)

if not retseptid:
    print("<p>Andmebaasis pole veel retsepte.</p>")

print("""
</div>
</body>
</html>
""")
conn.close()