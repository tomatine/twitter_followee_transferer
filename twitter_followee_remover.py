import tweepy
import time
import json
from credential import pre_CK, pre_CS, pre_AT, pre_AS
from settings import pre_screen_name,post_screen_name

auth = tweepy.OAuthHandler(pre_CK,pre_CS)
auth.set_access_token(pre_AT, pre_AS)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

pre_follower = {id for id in tweepy.Cursor(api.followers_ids, screen_name=pre_screen_name).items()}
pre_followee = {id for id in tweepy.Cursor(api.friends_ids, screen_name=pre_screen_name).items()}
post_followee = {id for id in tweepy.Cursor(api.friends_ids, screen_name=post_screen_name).items()}
outgoing=set(api.friendships_outgoing())#フォロー許可待ちの集合

target_for_remove = (pre_followee - pre_follower) & post_followee
print(len(target_for_remove))

for id in target_for_remove:
    api.destroy_friendship(id=id)
    print(pre_screen_name + ' unfollowed ' + api.get_user(id=id).screen_name)
    time.sleep(10)