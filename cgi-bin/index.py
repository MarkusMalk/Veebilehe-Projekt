#!/home/markusmalk/.venv/bin/python3

print("Content-Type: text/html; charset=utf-8")
print()

print("""
<!DOCTYPE html>
<html lang="et">

<head>
    <meta charset="UTF-8">
    <title>Retseptid</title>
    <link rel="stylesheet" href="../static/css/style.css">

    <style>
        body {
            text-align: center;
        }

        table {
            margin-left: auto;
            margin-right: auto;
        }
    </style>
</head>

<body>

    <h1 class="bordered">Temp Pealkiri</h1>

    <table border="2" class="centered">
        <thead>
            <tr>
                <th>Otsi retsepte</th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <td>
                    <a href="./retseptid.py">
                        <img src="../static/avaleht_retseptid.jpg"
                             style="width:500px; height:500px;"
                             alt="Otsi retsepte">
                    </a>
                </td>
            </tr>
        </tbody>
    </table>

</body>
</html>
""")