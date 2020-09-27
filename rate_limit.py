import tweepy
import json
from credential import CK, CS, AT, AS
from settings import pre_screen_name,post_screen_name

auth = tweepy.OAuthHandler(CK,CS)
auth.set_access_token(AT,AS)

api = tweepy.API(auth)

#print(json.dumps(limit,indent=4))

limit = api.rate_limit_status()

#print(json.dumps(limit,indent=4))

print("API.followers")
print(limit["resources"]["followers"]["/followers/list"],"\n" +"-"*50)

print("API.friends")
print(limit["resources"]["friends"]["/friends/list"],"\n" +"-"*50)

print("API.followers_ids")
print(limit["resources"]["followers"]["/followers/ids"],"\n" +"-"*50)

print("API.friedns_ids")
print(limit["resources"]["friends"]["/friends/ids"],"\n" +"-"*50)

print("API.show_friendship")
print(limit["resources"]["friendships"]["/friendships/show"],"\n" +"-"*50)

print("API.search")
print(limit["resources"]["search"]["/search/tweets"],"\n" +"-"*50)

print("API.rate_limit_status")
print(limit["resources"]["application"]["/application/rate_limit_status"],"\n" +"-"*50)