import pickle
import numpy as np
from flask import Flask,request,render_template

#reading both the pickle files with Age & Gender modals
modal_age = pickle.load(open("adCampaignRecommenderAge.pkl","rb"))
modal_gender = pickle.load(open("adCampaignRecommenderGender.pkl","rb"))

app =Flask(__name__)

@app.route("/")
def homepage():
	return render_template("index.html")
	####################################################################

@app.route("/age_preiction",methods=['POST'])
def predictAge():
    pre_sal = modal_age.predict([[int(x) for x in request.form.values()]])
    return render_template("index.html",prediction_text = "Your Age is "+str(pre_sal[0]))

@app.route("/gender_preiction",methods=['POST'])
def predictAge():
    pre_sal = modal_gender.predict([[int(x) for x in request.form.values()]])
    return render_template("index.html",prediction_text = "Your Gender is "+str(pre_sal[0]))

    
if __name__=="__main__":
    app.run(port=5000,debug=True)