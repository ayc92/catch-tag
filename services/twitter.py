from base64 import b64encode
import logging
import requests
from urllib import quote_plus

logger = logging.Logger()


class TwitterAPIClient(object):
    """
    This is the service provider for Twitter application-only API calls.
    """
    # Let's just store our consumer key and secret in plaintext. This application
    # isn't life changing; the worst that could happen if someone were to use our
    # consumer key and secret is that they could make requests to Twitter on behalf
    # of our application, and potentially cause our application to reach its rate limit.
    TWITTER_CONSUMER_KEY = '7MY8c3BpeA95xNitXp7kNS9nU'
    TWITTER_CONSUMER_SECRET = 'L8qq9PZyRg6ieKGEKhZolGC0vJWLw8iEJ88DRdyOg'

    # Twitter endpoints
    TWITTER_TOKEN_URL = 'https://api.twitter.com/oauth2/token'
    TWITTER_SEARCH_TWEET_URL = 'https://api.twitter.com/1.1/search/tweets.json'

    def _get_base_64_bearer_token_creds(self):
        return b64encode('%s:%s' % (quote_plus(self.TWITTER_CONSUMER_KEY), quote_plus(self.TWITTER_CONSUMER_SECRET)))

    def _get_bearer_token(self):
        """
        Use the base64-encoded key and secret to get the bearer token that will be used
        to make future application-only API requests.
        """
        credentials = self._get_base_64_bearer_token_creds()
        headers = {
            'Authorization': 'Basic %s' % credentials,
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        data = { 'grant_type': 'client_credentials' }
        response = requests.post(self.TWITTER_TOKEN_URL, headers=headers, data=data)
        response_dict = response.json()
        if response_dict['token_type'] != 'bearer':
            # This really shouldn't ever happen.
            logger.error('For some reason, the Twitter OAuth2 token endpoint returned the wrong type of token.')
        return response_dict['access_token']

    def __init__(self):
        """
        Get the Twitter application-only access token on instance creation.
        """
        self.access_token = self._get_bearer_token()

    def search_tweets(self, hashtag):
        """
        Search tweets filtered by a hashtag parameter.
        """
        pass
