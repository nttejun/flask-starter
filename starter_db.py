from flask import Flask, render_template, request
import sqlite3 as sql
starter_db = Flask(__name__)

@starter_db.route('/')
def home():
    return render_template('db/home.html')

@starter_db.route('/enternew')
def new_student():
    return render_template('db/student.html')


@starter_db.route('/addrec', methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sql.connect('test.db') as con:
                cur = con.cursor()
                
                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?, ?, ?, ?)", (nm,addr,city,pin))

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("db/msg.html", msg = msg)
            con.close()

@starter_db.route('/list')
def list():
    con = sql.connect("test.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall();
    return render_template("db/list.html", rows = rows)

if __name__ == '__main__':
    starter_db.run(debug = True)