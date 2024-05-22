from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/blog")
def blog():
    response = requests.get("https://api.npoint.io/514af50cd28d50586082", verify=False)
    all_posts = response.json()
    print(all_posts)
    return render_template("for-if-template.html", posts=all_posts)

if __name__ == "__main__": 
    app.run(debug=True)