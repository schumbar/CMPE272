import authorization_information as auth_info
import tweepy
import requests
import json
import requests_oauthlib


class twitter_client():
    def __init__(self) -> None:
        env_vars = auth_info.AuthorizationInformation()
        consumer_key = env_vars.consumer_key
        consumer_secret = env_vars.consumer_secret
        access_token_key = env_vars.access_token
        access_token_secret = env_vars.access_token_secret

        auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token_key, access_token_secret)
        api = tweepy.API(auth)
        self.auth_api = requests_oauthlib.OAuth1(consumer_key, consumer_secret, access_token_key, access_token_secret)

        self.create_tweet_url = "https://api.twitter.com/2/tweets"
        self.delete_tweet_url = "https://api.twitter.com/2/tweets"

        return
    
    def create_headers(self):
        headers = {'Content-Type': 'application/json'}
        return headers
    
    def create_payload(self, tweet):
        payload = {"text": tweet}
        return payload
    
    def get_post_tweet_url(self):
        post_url = "https://api.twitter.com/2/tweets"
        return post_url
    
    def get_delete_tweet_url(self, tweet_id):
        delete_url = self.delete_tweet_url + f"/{tweet_id}"
        return delete_url
    
    def post_tweet(self, tweet):
        URL = self.get_post_tweet_url()
        headers = self.create_headers()
        payload = self.create_payload(tweet)
        response = requests.post(URL, auth=self.auth_api, headers=headers, data=json.dumps(payload))
        if response.status_code in [200, 201, 204]:
            tweet_id = json.loads(response.text)['data']['id']
            return tweet_id, "Tweet Content: " + tweet + " Tweet ID: " + tweet_id
        else:
            return -1, f"Tweet posting failed. Status code: {response.status_code}, Failure Message: {response.text}"
    
    def delete_tweet(self, tweet_id):
        response = requests.delete(self.get_delete_tweet_url(tweet_id), auth=self.auth_api)
        if response.status_code in [200,201,204]:
            return f"The following Tweet has been deleted successfuly: {tweet_id}"
        return f"Tweet deletion failed. Status code: {response.status_code}, Failure Message: {response.text}"

if __name__ == "__main__":
    tweet_content = "This is a test of post_tweet function on 09/16/2023. 3"
    tweet_id = "1702209142272995786"
    client = twitter_client()
    print(client.post_tweet(tweet_content))
    print(client.delete_tweet(tweet_id))