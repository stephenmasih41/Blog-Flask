from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html",all_data=response)

@app.route("/post/<int:num>")
def post(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    # Find the correct post
    selected_post = None
    for post in response:
        if post["id"] == num:
            selected_post = post
            break
    return render_template("post.html",post=selected_post)



if __name__ == "__main__":
    app.run(debug=True)
