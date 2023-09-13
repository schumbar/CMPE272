import tweepy
import authorization_information as ai

authorization_tokens = ai.AuthorizationInformation()
bearer_token = authorization_tokens.bearer_token
consumer_key = authorization_tokens.consumer_key
consumer_secret = authorization_tokens.consumer_secret
access_key = authorization_tokens.access_token
access_secret = authorization_tokens.access_token_secret


def get_tweets(username):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
 
        # Calling api
        api = tweepy.API(auth)
 
        # 200 tweets to be extracted
        number_of_tweets=10
        tweets = api.user_timeline(screen_name=username)
 
        # Empty Array
        tmp=[]
 
        # create array of tweet information: username,
        # tweet id, date/time, text
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created
        for j in tweets_for_csv:
 
            # Appending tweets to the empty array tmp
            tmp.append(j)
 
        # Printing the tweets
        print(tmp)
 
 
# Driver code
if __name__ == '__main__':
 
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("schumbar")