import tweepy
import time
from credential import post_CK, post_CS, post_AT, post_AS
from settings import pre_screen_name,post_screen_name

auth = tweepy.OAuthHandler(post_CK,post_CS)
auth.set_access_token(post_AT,post_AS)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

pre_follower = {id for id in tweepy.Cursor(api.followers_ids, screen_name=pre_screen_name).items()}
pre_followee = {id for id in tweepy.Cursor(api.friends_ids, screen_name=pre_screen_name).items()}
post_followee = {id for id in tweepy.Cursor(api.friends_ids, screen_name=post_screen_name).items()}
outgoing=set(api.friendships_outgoing())#フォロー許可待ちの集合

target_for_transfer = pre_followee - pre_follower - post_followee - outgoing
print(len(target_for_transfer))

for id in target_for_transfer:
    api.create_friendship(id=id)
    print(post_screen_name + ' followed ' + api.get_user(id=id).screen_name)
    time.sleep(10)