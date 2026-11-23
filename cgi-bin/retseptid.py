
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


params = parse_qs(os.environ.get("QUERY_STRING", ""))
otsi = params.get("otsi", [""])[0]
valitud_dieedid = params.get("dieet", [])

print("Content-Type: text/html; charset=utf-8\n")



try:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Retseptide päring
    sql = """
        SELECT r.id, r.nimi, r.pilt
        FROM retseptid r
        WHERE r.nimi LIKE ?
    """

    andmed = [f"%{otsi}%"]

    if valitud_dieedid:
        kohad = ",".join("?" for _ in valitud_dieedid)

        sql += f"""
            AND r.id IN (
                SELECT rd.retsepti_id
                FROM retsepti_dieedid rd
                WHERE rd.dieedi_id IN ({kohad})
                GROUP BY rd.retsepti_id
                HAVING COUNT(DISTINCT rd.dieedi_id) = ?
            )
        """

        andmed.extend(valitud_dieedid)
        andmed.append(len(valitud_dieedid))

    sql += " ORDER BY r.nimi"

    retseptid = conn.execute(sql, andmed).fetchall()

    # Dieetide päring
    dieedid = conn.execute("""
        SELECT id, nimi
        FROM dieedid
        ORDER BY nimi
    """).fetchall()

except Exception as e:
    print(f"<pre>VIGA: {html.escape(str(e))}</pre>")
    raise


print("""
<!DOCTYPE html>
<html lang="et">

<head>
    <meta charset="UTF-8">
    <title>Retseptid</title>
    <link rel="stylesheet" href="../static/css/style.css">
    <script src="../static/js/script.js" defer></script>
</head>


<body>
<h1 class="bordered">Retseptid</h1>
""")

print(f"""
<form action="./retseptid.py" method="GET">

    Otsi:
    <input type="text" name="otsi" value="{html.escape(otsi)}">
    <input type="submit" value="Otsi" class="button">

    <br><br>

    <button type="button" class="collapsible">Filter</button>

    <div class="content">
""")

for dieet in dieedid:
    nimi = html.escape(dieet["nimi"])
    dieet_id = str(dieet["id"])
    checked = "checked" if dieet_id in valitud_dieedid else ""

    print(f"""
        <label>
            <input type="checkbox" name="dieet"
                   value="{html.escape(dieet_id)}" {checked}>
            {nimi}
        </label>
    """)

print("""
    </div>

</form>
<br>

<div class="retseptide-grid">
""")

for retsept in retseptid:
    retsepti_id = retsept["id"]
    nimi = html.escape(retsept["nimi"])
    pilt = html.escape(retsept["pilt"])

    print(f"""
    <article class="retsepti-kaart">
        <a href="./retsept.py?id={retsepti_id}">
            <img class="retsepti-pilt"
                 src="../static/retseptid/{pilt}"
                 alt="{nimi}">
        </a>

        <h2 class="retsepti-nimi">{nimi}</h2>
        <div class="dieedi-grid"></div>
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
