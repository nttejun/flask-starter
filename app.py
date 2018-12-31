from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/board/<contents>')
def board_detail(contents):
    return 'Board Contents %s' % contents

@app.route('/board/<int:page>')
def board_page(page):
    return 'Board page No = %i' %page

@app.route('/access/admin')
def access_admin():
    return 'Access Admin'

@app.route('/access/<guest>')
def access_guest(guest):
    return 'Access Guest %s' %guest 

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('access_admin'))
    else:
        return redirect(url_for('access_guest', guest = name))

if __name__ == '__main__':
   app.run(debug = True)
