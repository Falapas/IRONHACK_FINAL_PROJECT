from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<name>/")
def home(name):
    return render_template("index.html", content=["tim", "joe", "bill"], r=2)

#@app.route("/<name>/")
#def user(name):
#    return f"Hello {name}!"
#
#@app.route("/admin/")
#def admin():
#    return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run()
    
    
import numpy as np
import pandas as pd
import pickle
from sklearn.tree import DecisionTreeRegressor

def price_estimator(features):
    with open('Model.sav', 'rb') as f:
        model = pickle.load(f)
    return model.predict(features)

features = np.array([449,328,5196,4755,158,800,1009,1658,5000,43,71,50,195,5890,24382,281,281,281,0,100,7,58,0,0,0,269,269,269,1035,97,0,229,0,0,0,267,267,267,971,63,1,309,0,0,0,273,273,273,1039,75,1,21,0,0,0,270,270,270,1001,77,1,62,0,0,0,2015,1,1,0])
price_estimator(features.reshape(1, -1))