from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    message = ""

    if request.method == "POST":

        youtube_url = request.form.get("youtube_url")

        message = f"Link diterima: {youtube_url}"

    return render_template(
        "index.html",
        message=message
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
