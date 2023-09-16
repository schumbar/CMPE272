import unittest
import twitter_client
from datetime import datetime
import json

TWEET_ID_DELETE = "123456789"

class TestTwitterFunctionality(unittest.TestCase):
    def test_create_headers(self):
        client = twitter_client.twitter_client()
        headers = client.create_headers()
        expected_headers = {'Content-Type': 'application/json'}
        self.assertEqual(headers, expected_headers)

    def test_create_payload(self):
        client = twitter_client.twitter_client()
        payload = client.create_payload("This is a test tweet")
        expected_payload = {"text": "This is a test tweet"}
        self.assertEqual(payload, expected_payload)

    def test_get_post_tweet_url(self):
        client = twitter_client.twitter_client()
        post_url = client.get_post_tweet_url()
        expected_post_url = "https://api.twitter.com/2/tweets"
        self.assertEqual(post_url, expected_post_url)

    def test_get_delete_tweet_url(self):
        client = twitter_client.twitter_client()
        delete_url = client.get_delete_tweet_url(TWEET_ID_DELETE)
        expected_delete_url = f"https://api.twitter.com/2/tweets/{TWEET_ID_DELETE}"
        self.assertEqual(delete_url, expected_delete_url)

    def test_post_tweet(self):
        client = twitter_client.twitter_client()
        content = str(datetime.now())
        tweet_id, post_return = client.post_tweet(content)
        expected_tweet_id = tweet_id
        expected_post_return = f"Tweet Content: {content} Tweet ID: {tweet_id}"
        self.assertEqual(post_return, expected_post_return)
        self.assertEqual(tweet_id, expected_tweet_id)

    def test_delete_tweet(self):
        client = twitter_client.twitter_client()
        delete_return = client.delete_tweet(TWEET_ID_DELETE)
        expected_delete_return = f"The following Tweet has been deleted successfuly: {TWEET_ID_DELETE}"
        self.assertEqual(delete_return, expected_delete_return)

if __name__ == '__main__':
    unittest.main()