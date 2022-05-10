from flask import Flask, request, render_template, redirect, url_for
import passwd_gen, os
import json

app = Flask(__name__)

@app.route("/",methods = ["POST","GET"])
def index():
    if request.method == "POST":
        length = request.form.get("length")
        try:
            if int(length) < 5:
                return "Enter length more than 5"
            else:
                try:
                    return redirect(f"/gen/{length}")
                    
                except Exception:
                    return "There was some error taking your input"
        except Exception:
            return redirect ('/gen/15')
            
    else:
        return render_template("index.html")

@app.route("/gen/<int:length>",methods = ["POST","GET"])
def gen(length):
    try:
        length = int(length)
        password = passwd_gen.generate_pass(length)
        password = str(password)
        return render_template("gen.html", password = password)
    except Exception:
        return "there were some error redirecting"
@app.route("/api/",methods=["POST", "GET"])
def home():
    data_set = {'Length': 'None', 'Password': 'None', 'Message':'This is Home page of the api'}
    json_dump = json.dumps(data_set)
    return json_dump

@app.route("/api/gen/<int:length>",methods=["POST","GET"])
def page(length):
    #if request.method == "POST":
        #length = request.form.get("length")

    length = int(length)
    password = passwd_gen.generate_pass(length)
    password = str(password)
    if int(length) < 5:
        msg = { "Message" : "Enter Length More than 5 characters"}
        json_msg = json.dumps(msg)
        return json_msg
    else:
        
        data_set = {'Length' : length, 'Password': password, 'Message' : 'Succesfully Generated Password'}
    
        json_dump = json.dumps(data_set)
        return json_dump 

if __name__ == "__main__":
    app.run(port = int(os.environ.get('PORT', 5000)))