from flask import Flask, render_template
import os  # เพิ่มบรรทัดนี้

app = Flask(__name__)

# Route for index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for gallery page
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# Route for flower page
@app.route('/flower')
def flower():
    return render_template('flower.html')

# Run the server
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # ใช้ PORT จาก environment variable
    app.run(host='0.0.0.0', port=port, debug=True)
