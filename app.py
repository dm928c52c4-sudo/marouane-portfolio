from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Café Sami - Kelaa</title>
<style>
body{font-family:sans-serif;background:#fff7ed;margin:0}
.header{background:#ff6b00;color:white;padding:30px;text-align:center}
.card{background:white;margin:15px;border-radius:15px;padding:15px;display:flex;gap:15px;box-shadow:0 2px 8px #0001}
.card img{width:80px;height:80px;border-radius:10px;object-fit:cover}
.price{color:#ff6b00;font-weight:bold}
</style>
</head>
<body>
<div class="header"><h1>Café Sami - Kelaa Des Sraghna</h1><p>📞 06 12 34 56 78</p></div>
<div style="max-width:500px;margin:auto">
<div class="card"><img src="https://images.unsplash.com/photo-1571934811356-5cc061b6821f?w=200"><div><b>Atay</b><br>Atay bel na3na3<br><span class="price">12 DH</span></div></div>
<div class="card"><img src="https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=200"><div><b>Café Noir</b><br>9ahwa 3arbia<br><span class="price">12 DH</span></div></div>
<div class="card"><img src="https://images.unsplash.com/photo-1541518763669-27fef04b14ea?w=200"><div><b>Tajine Lhem</b><br>Bel ber9o9 w loz<br><span class="price">75 DH</span></div></div>
<div class="card"><img src="https://images.unsplash.com/photo-1513104890138-7c749659a591?w=200"><div><b>Pizza</b><br>Fromage tomate<br><span class="price">60 DH</span></div></div>
<div class="card"><img src="https://images.unsplash.com/photo-1521390188846-e2a3a97453a0?w=200"><div><b>Panini</b><br>Djaj fromage<br><span class="price">35 DH</span></div></div>
</div>
</body>
</html>
"""

@app.route('/')
def home(): return HTML
@app.route('/sami')
def sami(): return HTML
