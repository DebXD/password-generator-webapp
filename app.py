from flask import Flask, request, render_template, redirect, url_for
import passwd_gen
app = Flask(__name__)

@app.route("/",methods = ["POST","GET"])
def index():
    if request.method == "POST":
        length = request.form.get("length")
        try:
            if int(length) < 4:
                return "Enter length more than 4"
            else:
                try:
                    return redirect(f"/gen/{length}")
                    
                except:
                    return "There was some error taking your input"
        except:
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
    except:
        return "there were some error redirecting"

if __name__ == "__main__":
    app.run()