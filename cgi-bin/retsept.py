#!/usr/bin/env python3
print("Content-Type: text/html; charset=utf-8\n")

print("""
<!DOCTYPE html>
<html lang="et">
<head>
    <meta charset="UTF-8">
    <title>Retsept</title>
</head>
<body>

    <h1>Pannkoogid</h1>
    <div><img src="../static/pannkoogid.jpg" alt="Pannkoogid" width="300"></div>
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