import os
from flask import Flask, render_template, request
from tweetslack import twitter_slack
app = Flask(__name__)

@app.route("/")
def index():
	tweet = None
	message = request.values.get('message')
	if message:
		tweet = twitter_slack(message)
	return render_template('index.html', tweet=tweet)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)