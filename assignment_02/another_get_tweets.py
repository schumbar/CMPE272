import tweepy
import os

# Authenticate to Twitter
auth = tweepy.OAuthHandler(os.environ.get("CONSUMER_KEY"), os.environ.get("CONSUMER_SECRET"))
auth.set_access_token(os.environ.get("ACCESS_TOKEN"), os.environ.get("ACCESS_TOKEN_SECRET"))

# Create API object
api = tweepy.API(auth)

# Post a tweet
tweet = "Hello, world!"
api.update_status(tweet)


# from requests_oauthlib import OAuth1Session
# import os
# import json

# import tweepy
# import configparser
# import pandas as pd
# api_key = os.environ.get("CONSUMER_KEY")
# api_key_secret = os.environ.get("CONSUMER_SECRET")
# access_token = os.environ.get("ACCESS_TOKEN")
# access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

# # authentication
# auth = tweepy.OAuthHandler(api_key, api_key_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)

# public_tweets = api.home_timeline()

# # create dataframe
# columns = ['Time', 'User', 'Tweet']
# data = []
# for tweet in public_tweets:
#     data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

# df = pd.DataFrame(data, columns=columns)

# df.to_csv('tweets.csv')


# # consumer_key = os.environ.get("CONSUMER_KEY")
# # consumer_secret = os.environ.get("CONSUMER_SECRET")
# # api_key = os.environ.get("CONSUMER_KEY")
# # api_key_secret = os.environ.get("CONSUMER_SECRET")
# # access_token = os.environ.get("ACCESS_TOKEN")
# # access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

# # params = {"ids": "1278747501642657792", "tweet.fields": "created_at"}
# # request_token_url = "https://api.twitter.com/oauth/request_token"
# # oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

# # try:
# #     fetch_response = oauth.fetch_request_token(request_token_url)
# # except ValueError:
# #     print(
# #         "There may have been an issue with the consumer_key or consumer_secret you entered."
# #     )

# # resource_owner_key = fetch_response.get("oauth_token")
# # resource_owner_secret = fetch_response.get("oauth_token_secret")
# # print("Got OAuth token: %s" % resource_owner_key)

# # # Get authorization
# # base_authorization_url = "https://api.twitter.com/oauth/authorize"
# # authorization_url = oauth.authorization_url(base_authorization_url)
# # print("Please go here and authorize: %s" % authorization_url)
# # verifier = input("Paste the PIN here: ")

# # # Get the access token
# # access_token_url = "https://api.twitter.com/oauth/access_token"
# # oauth = OAuth1Session(
# #     consumer_key,
# #     client_secret=consumer_secret,
# #     resource_owner_key=resource_owner_key,
# #     resource_owner_secret=resource_owner_secret,
# #     verifier=verifier,
# # )
# # oauth_tokens = oauth.fetch_access_token(access_token_url)


# # access_token = oauth_tokens["oauth_token"]
# # access_token_secret = oauth_tokens["oauth_token_secret"]

# # # Make the request
# # oauth = OAuth1Session(
# #     consumer_key,
# #     client_secret=consumer_secret,
# #     resource_owner_key=access_token,
# #     resource_owner_secret=access_token_secret,
# # )

# # response = oauth.get(
# #     "https://api.twitter.com/2/tweets", params=params
# # )

# # if response.status_code != 200:
# #     raise Exception(
# #         "Request returned an error: {} {}".format(response.status_code, response.text)
# #     )

# # print("Response code: {}".format(response.status_code))
# # json_response = response.json()
# # print(json.dumps(json_response, indent=4, sort_keys=True))