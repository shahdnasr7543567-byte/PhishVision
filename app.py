from flask import Flask, request, jsonify, render_template
from pipeline import scan

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan_url():
    data = request.json
    url = data.get('url', '')
    
    if not url:
        return jsonify({'error': 'Enter a URL'}), 400
    
    result = scan(url)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)



