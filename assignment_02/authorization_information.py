import tweepy
import os
from dotenv import load_dotenv, find_dotenv

# Author: Shawn Chumbar

load_dotenv(find_dotenv())

class AuthorizationInformation:
    def __init__(self) -> None:
        self.bearer_token = os.environ.get("BEARER_TOKEN")
        self.consumer_key = os.environ.get("CONSUMER_KEY")
        self.consumer_secret = os.environ.get("CONSUMER_SECRET")
        self.access_token = os.environ.get("ACCESS_TOKEN")
        self.access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
        self.auth = self.auth()
        self.api = self.api()
        return
    
    def auth(self):
        auth = tweepy.OAuth1UserHandler(
            self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret
        )
        return auth
    
    def api(self):
        api = tweepy.API(self.auth)
        return api

# If the authentication was successful, this should print the
# screen name / username of the account
if __name__ == "__main__":
    s = AuthorizationInformation()
    print(s.api.verify_credentials().screen_name)