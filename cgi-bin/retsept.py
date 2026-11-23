#!/usr/bin/env python3
import sqlite3
import html
from urllib.parse import parse_qs
import os


if os.name == "nt":
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(SCRIPT_DIR, "..", "instance", "retseptid.db")
else:
    DB_PATH = os.path.expanduser("~/public_html/instance/retseptid.db")


params = parse_qs(os.environ.get("QUERY_STRING", ""))
retsepti_id = params.get("id", [""])[0] #Retsepti ID, mida kasutaja valis. Sellega saab retsepti infot kuvada

try:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    retsept = conn.execute("""
    SELECT nimi
    FROM retseptid
    WHERE id = ?
""", (retsepti_id,)).fetchone()

except Exception as e:
    print(f"<pre>VIGA: {html.escape(str(e))}</pre>")
    raise

print("Content-Type: text/html; charset=utf-8\n")

nimi = html.escape(retsept["nimi"])

print(f"""
<!DOCTYPE html>
<html lang="et">
<head>
    <meta charset="UTF-8">
    <title>Retsept</title>
</head>
<body>

    <h1>{nimi}</h1>
    <div><img src="../static/retseptid/pannkook.jpeg" alt="Pannkoogid" width="300"></div>
    <div>
        <h2>Koostisosad</h2>
        
        <ul>
            <li>Jahu</li>
            <li>Piim</li>
            <li>Munad</li>
            <li>Suhkur, sool</li>
        </ul>
    </div>

    <div>
        <h2>QR kood</h2>
        <p>[QR koodi pilt]</p>
    </div>

    <div>
        <h2>Juhend</h2>
        <p>1. Klopi munad ja piim kokku.<br>
           2. Lisa jahu ja maitseained.<br>
           3. Prae pannil kuldpruuniks.</p>
    </div>

    <div>
        <h2>Dieedid</h2>
        
    </div>

</body>
</html>
""")