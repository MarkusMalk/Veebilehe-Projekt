#!/usr/bin/env python3

print("Content-Type: text/html; charset=utf-8")
print()

print("""
<!DOCTYPE html>
<html lang="et">

<head>
    <meta charset="UTF-8">
    <title>Retseptid</title>
    <link rel="stylesheet" href=/~markusmalk/static/css/style.css">
</head>

<body>

    <h1 class="bordered">Retseptide leht</h1>

    <table border="2" class="centered">
        <thead>
            <tr>
                <th>Otsi retsepte</th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <td>
                    <a href="/~markusmalk/cgi-bin/retseptid.py">
                        <img src="/~markusmalk/static/avaleht_retseptid.jpg"
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