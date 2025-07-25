from flask import Flask, render_template
import webbrowser

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template("qrcode.html")

if __name__ == '__main__':
    print("🌐 فتح واجهة QR...")
    webbrowser.open("http://127.0.0.1:5000")
    app.run()
