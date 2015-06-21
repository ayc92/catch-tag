from base64 import b64encode
import requests
from urllib import quote_plus


class TwitterServiceException(Exception):
    """
    A subclass of a vanilla python Exception for more descriptive error reporting.
    """
    pass


class TwitterAPIClient(object):
    """
    This is the service provider for Twitter application-only API calls.
    """
    # Let's just store our consumer key and secret in plaintext. This application
    # isn't life changing; the worst that could happen if someone were to use our
    # consumer key and secret is that they could make requests to Twitter on behalf
    # of our application, and potentially cause our application to reach its rate limit.
    TWITTER_CONSUMER_KEY = '7MY8c3BpeA95xNitXp7kNS9nU'
    TWITTER_CONSUMER_SECRET = 'QCURvwq3Nrgk8xyinBf7iZO25Tn0GVtiM0UO0rZ0osLmUlJGMw'

    # Twitter endpoints
    TWITTER_TOKEN_URL = 'https://api.twitter.com/oauth2/token'
    TWITTER_SEARCH_TWEET_URL = 'https://api.twitter.com/1.1/search/tweets.json'
    TWITTER_TRENDS_PLACE_URL = 'https://api.twitter.com/1.1/trends/place.json'

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
            raise TwitterServiceException("For some reason, the Twitter OAuth2 token"
                                          "endpoint returned the wrong type of token.")
        return response_dict['access_token']

    def __init__(self):
        """
        Get the Twitter application-only access token on instance creation.
        """
        access_token = self._get_bearer_token()
        self.authorization_header = { 'Authorization': 'Bearer %s' % access_token }

    def get_twitter_trends(self, woeid):
        """
        Get the names of trending topics using the given woeid.
        """
        response = requests.get(
            self.TWITTER_TRENDS_PLACE_URL, headers=self.authorization_header, params={ 'id': woeid })
        response_json = response.json()
        trends = response_json['trends']
        search_queries = [trend['name'] for trend in trends]
        return search_queries

    def get_tweet_search_results(self, param):
        """
        Get the tweets associated with the given query parameter.
        """
        # URL-encode the search parameter.
        esc_param = quote_plus(param)
        response = requests.get(
            self.TWITTER_SEARCH_TWEET_URL, headers=self.authorization_header, params={ 'q': esc_param })
        response_json = response.json()
        tweets = response_json['statuses']
        map_id_to_tweet = { tweet['id_str']: tweet['text'] for tweet in tweets }
        return map_id_to_tweet
