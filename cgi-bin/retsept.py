#!/usr/bin/env python3
print("Content-Type: text/html; charset=utf-8\n")

print("""
<!DOCTYPE html>
<html lang="et">
<head>
    <meta charset="UTF-8">
    <title>Retsept</title>
    <link rel="stylesheet" href="../static/css/style.css">
</head>
<body>
    <main class="retsepti-leht">
        <h1 class="bordered">Pannkoogid</h1>

        <div class="retsepti-pais">
            <img src="../static/pannkoogid.jpg" alt="Pannkoogid" class="retsepti-pilt">
        </div>

        <div class="retsepti-plokid retsepti-plokid--kolm">
            <section class="retsepti-kast">
                <h2>Koostisosad</h2>
                <ul>
                    <li>Jahu</li>
                    <li>Piim</li>
                    <li>Munad</li>
                    <li>Suhkur, sool</li>
                </ul>
            </section>

            <section class="retsepti-kast">
                <h2>Juhend</h2>
                <p class="juhendi-tekst">1. Klopi munad ja piim kokku.<br>
                   2. Lisa jahu ja maitseained.<br>
                   3. Prae pannil kuldpruuniks.</p>
            </section>

            <section class="retsepti-kast">
                <h2>Dieedid</h2>
                <div class="dieetide-grid">
                    <span class="dieedi-silt">Taimetoit</span>
                </div>
            </section>
        </div>
    </main>
</body>
</html>
""")