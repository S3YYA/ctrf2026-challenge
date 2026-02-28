from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    role = request.cookies.get('role')
    
    # Vulnerability: Trusting client-controlled plain-text cookie
    if role == 'admin':
        return render_template('index.html', theme='dark', flag='EHAX{cl13nt_byp4ss_4nd_c00k13_f0rg3ry}')
    
    return render_template('index.html', theme='light')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Backend validation that requires direct HTTP manipulation to reach
    if not username or not password:
        return "Bad Request: Missing Credentials", 400
        
    # Give them the guest cookie regardless of credentials,
    # as long as they bypassed the client-side restrictions.
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('role', 'guest')
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)