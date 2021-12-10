from flask import Flask, render_template, request
import helper

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_tweet():
    if request.method == 'GET':
        return render_template('index.html', is_tweet_entered=False)
    else:
        tweet = request.form['tweet']
        cleaned_tweet = helper.preprocess_tweet(tweet)
        result = helper.predict(cleaned_tweet)
        return render_template('index.html', is_tweet_entered=True, message=tweet, result=result)


if __name__ == "__main__":
    app.run(host="localhost", debug=True, use_reloader=False, port=3000)
