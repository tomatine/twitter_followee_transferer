import tweepy
from credential import CK,CS,AT,AS

auth = tweepy.OAuthHandler(CK,CS)
auth.set_access_token(AT,AS)

api = tweepy.API(auth)

public_tweets = api.home_timeline()


followers_set = api.followers(skip_status=True, include_user_entities=False,count=200)

for follower in followers_set:
    print(follower.name)

print(len(followers_set))