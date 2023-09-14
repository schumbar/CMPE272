import tweepy
import os
import authorization_information as auth_info
# Authenticate to Twitter


import requests
import json

def create_headers():
    content_type = 'application/json'
    cookie = 'guest_id=v1%3A169467230559775424'
    authorization = 'OAuth oauth_consumer_key="mO6OfA6TDsESaDDdXUtkm9sNM",oauth_token="1701643355695009792-0J9e4JUlUnEgDAE5NOk9xT1V97naxK",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1694672396",oauth_nonce="MWsrTbx01Cc",oauth_version="1.0",oauth_signature="MLU%2FXN2y1eAHOJe%2FIxwWRMqDUNY%3D"'
    auth_header = {
        'Content-Type': content_type,
        'Authorization': authorization,
        'Cookie': cookie
  }
    return auth_header

def create_message(message):
    message_payload = json.dumps({
        "text": message
    })
    return message_payload

def post_tweet(message):
    url = "https://api.twitter.com/2/tweets"
    headers = create_headers()
    payload = create_message(message)
    response = requests.request("POST", url, headers=headers, data=payload)
    return response

if __name__ == "__main__":
    tweet_content = "This is a test of the refactored another_get_tweets.py"
    resp = post_tweet(tweet_content)
    print(resp.text)
