from flask import Flask
app = Flask(__name__)

@app.route('/')
def portfolio():
    return """
    <body style='background:#0f0f0f; color:white; font-family:Arial; padding:20px; text-align:center'>
        <h1 style='color:#00ff88'>👨‍💻 Marouane - Portfolio</h1>
        <p style='color:gray'>مبرمج من مراكش - كنصاوب مواقع وتطبيقات</p>
        
        <div style='display:grid; grid-template-columns:1fr 1fr; gap:15px; max-width:600px; margin:20px auto; text-align:right'>
            
            <div style='background:#1e1e1e; padding:15px; border-radius:12px; border:1px solid #333'>
                <h3>💰 Floussi</h3><p style='color:gray; font-size:13px'>برنامج حساب الفلوس للسطاسيون</p><span style='color:#00ff88'>✓ خدام</span>
            </div>
            
            <div style='background:#1e1e1e; padding:15px; border-radius:12px; border:1px solid #333'>
                <h3>🛵 Usheel</h3><p style='color:gray; font-size:13px'>تطبيق التوصيل السريع</p><span style='color:#00ff88'>✓ خدام</span>
            </div>

            <div style='background:#1e1e1e; padding:15px; border-radius:12px; border:1px solid #333'>
                <h3>💪 Iroun Fitness</h3><p style='color:gray; font-size:13px'>موقع الجيم واللياقة</p><span style='color:#00ff88'>✓ خدام</span>
            </div>

            <div style='background:#1e1e1e; padding:15px; border-radius:12px; border:1px solid #333'>
                <h3>☕ Café Marrakech</h3><p style='color:gray; font-size:13px'>مينيو ديجيتال للقهوة</p><span style='color:#00ff88'>✓ خدام</span>
            </div>

            <div style='background:#1e1e1e; padding:15px; border-radius:12px; border:1px solid #333'>
                <h3>📱 App</h3><p style='color:gray; font-size:13px'>تطبيق موبايل</p><span style='color:#00ff88'>✓ خدام</span>
            </div>

            <div style='background:#1e1e1e; padding:15px; border-radius:12px; border:1px solid #333; border-color:#00ff88'>
                <h3>🌟 Marouane Web</h3><p style='color:gray; font-size:13px'>الموقع الشخصي</p><span style='color:#00ff88'>✓ خدام</span>
            </div>
        </div>

        <a href='https://wa.me/212785521645' style='background:#00ff88; color:black; padding:12px 30px; border-radius:25px; text-decoration:none; font-weight:bold; display:inline-block; margin-top:10px'>تواصل معايا فواتساب</a>
        <p style='color:#555; margin-top:20px; font-size:12px'>مراكش - 2026</p>
    </body>
    """

# app.run(debug=True)