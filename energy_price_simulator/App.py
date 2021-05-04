from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'FilipeCosta21989'
app.config['MYSQL_DB'] = 'final_project'
mysql = MySQL(app)

# Settings
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM date')
    data = cur.fetchall()
    return render_template('index.html', date = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        year = request.form['year']
        month = request.form['month']
        day = request.form['day']
        hour = request.form['hour']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO date (year, month, day, hour) VALUES (%s, %s, %s, %s)', (year, month, day, hour))
        mysql.connection.commit()
        flash('Date Added Successfully')
        return redirect(url_for('Index'))


@app.route('/edit/<id>')
def get_date(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM date WHERE id = %s', (id))
    data = cur.fetchall()
    return render_template('edit-date.html', value = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_value(id):
    if request.method == 'POST':
        year = request.form['year']
        month = request.form['month']
        day = request.form['day']
        hour = request.form['hour']
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE date
        SET year = %s,
            month = %s,
            day = %s,
            hour = %s
        WHERE id = %s
    """, (year, month, day, hour, id))
    mysql.connection.commit()
    flash('Value Updated Successfully')
    return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM date WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Date Removed Successfully')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)