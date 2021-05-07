import numpy as np
import pickle
from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL
#from sklearn.tree import DecisionTreeRegressor

app = Flask(__name__)

model = pickle.load(open('Model.sav', 'rb'))

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
    cur.close()
    return render_template('index.html', date = data)

@app.route('/add_value', methods=['POST'])
def add_value():
    if request.method == 'POST':
        year = request.form['year']
        month = request.form['month']
        day = request.form['day']
        hour = request.form['hour']
        cur = mysql.connection.cursor()
        
        with open('Model.sav', 'rb') as f:
            model = pickle.load(f)
        features = np.array([445,318,4324,5025,154,0,1214,6183,7096,43,74,100,210,3118,29014,283,283,283,1036,84,5,256,0,275,275,275,1036,87,1,196,16,271,271,271,1005,75,1,224,0,280,280,280,1038,78,2,45,0,275,275,275,1021,81,1,220,0,year,month,day,hour])
        #features = get_features(year, month, day, hour)
        
        price = model.predict(features.reshape(1, -1))
        
        cur.execute('INSERT INTO date (year, month, day, hour, price) VALUES (%s, %s, %s, %s, %s)', (year, month, day, hour, price[0]))
        mysql.connection.commit()
        flash('Date Added Successfully')
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_value(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM date WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Date Removed Successfully')
    return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(port = 3000, debug = True)