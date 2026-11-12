#!/usr/bin/env python3
print('Content-Type: text/html; charset=utf-8\n')

print('''
<!DOCTYPE html>
<html lang="et">
<head>
    <meta charset="utf-8">
    <title>Retsept ....</title>
    <link rel='stylesheet' href='../static/css/style.css>
</head>
<body>
      <main class='retsepti-konteiner'>
        <h1 class='retsepti-pealkiri'>Retsepti nimi</h1>
        
        <div class='retsepti-sisu'>
            <div class='vasak-veerg'>
                <div class='kast'>
                    <h2>Koostiosad</h2>
                    <p>Siia tulevad koostisosad...</p>
                </div>
                <div class='kast'>
                    <h3>QR kood</h3>
                </div>
            </div>
        
            <div class='parem-veerg'>
                <div class='kast'>
                    <h2>Juhend</h2>
                    <p>Siia tuleb valmistamisjuhend...</p>
                </div>
                <div class='kast'>
                    <h3>Dieedid</h3>
                    <p>Siia tulevad dieedisildid...</p>
                </div>
            </div>
        </div>
    </main>
</body>
</html>
''')