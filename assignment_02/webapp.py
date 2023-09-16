from flask import Flask, render_template, request
import twitter_client

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    delete_message = ""
    post_message = ""
    client = twitter_client.twitter_client()
    if request.method == 'POST':
        if 'delete' in request.form:
            tweet_id = request.form['tweet_id']
            output = client.delete_tweet(tweet_id)
            delete_message = f"Deleted tweet with ID: {tweet_id}"
            if "failed" in output:
                delete_message = "Tweet deletion failed."
        
        elif 'post' in request.form:
            tweet_content = request.form['tweet_content']
            tweet_id, output = client.post_tweet(tweet_content)
            post_message = "Tweet Posted! Here are the Tweet Details: " + output
            if tweet_id == -1:
                post_message = "Tweet posting failed."

    return render_template('index.html', delete_message = delete_message, post_message=post_message)

if __name__ == '__main__':
    app.run(debug=True)