from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    username = request.args.get('username', 'World') # Set 'World' as the default value if no parameter is provided
    return render_template('index.html', username=username) # Pass 'username' variable to the template

@app.route('/healthcheck')
def healthcheck():
    return jsonify(status="OK", message="Service is running")

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=8001)