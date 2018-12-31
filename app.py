from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/board/<contents>')
def board_detail(contents):
    return 'Board Contents %s' % contents

@app.route('/board/<int:page>')
def board_page(page):
    return 'Board page No = %i' %page

# user url_for(access_admin)
@app.route('/access/admin')
def access_admin():
    return 'Access Admin'

# user url_for(access_guest)
@app.route('/access/<guest>')
def access_guest(guest):
    return 'Access Guest %s' %guest 

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('access_admin'))
    else:
        return redirect(url_for('access_guest', guest = name))

@app.route('/passlogin/<name>')
def passlogin(name):
    return "Login Pass %s" %name

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('passlogin', name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('passlogin', name = user))

@app.route('/<user>')
def index(user):
    return render_template('index.html', user=user)

@app.route('/score/<int:score>')
def score_num(score):
    return render_template('score.html', marks = score)

@app.route('/score/result')
def route():
    dict = {'phy':50, 'che':60, 'maths':70}
    return render_template('result.html', dict = dict)

@app.route('/click')
def click():
    return render_template('click.html')

if __name__ == '__main__':
   app.run(debug = True)
