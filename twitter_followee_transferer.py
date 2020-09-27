import tweepy
from credential import CK, CS, AT, AS
from settings import pre_screen_name,post_screen_name

auth = tweepy.OAuthHandler(CK,CS)
auth.set_access_token(AT,AS)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

pre_follower = {id for id in tweepy.Cursor(api.followers_ids, screen_name=pre_screen_name).items()}
pre_followee = {id for id in tweepy.Cursor(api.friends_ids, screen_name=pre_screen_name).items()}
post_followee = {id for id in tweepy.Cursor(api.friends_ids, screen_name=post_screen_name).items()}

print(pre_followee)
print(len(pre_followee))
print(pre_follower)
print(len(pre_follower))
print(post_followee)
print(len(post_followee))

target_for_transfer = pre_followee - pre_follower - post_followee
print(target_for_transfer)
print(len(target_for_transfer))

for id in target_for_transfer:
    api.create_friendship(id=id)
    print(post_screen_name + ' followed ' + api.get_user(id=id).screen_name)