from keys import *
import tweepy, time

from user_list import UserList

#Consumer Keys
auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
#Access Token and Secret
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#objeto da API
api = tweepy.API(auth, wait_on_rate_limit = True) #autenticar e definir limite de tweets

search = ""
comment = ""

user_list = UserList()

for tweet in tweepy.Cursor(api.search_tweets, search).items(100):  
  try:    
    if tweet.user.id_str not in user_list.user_list:
      tweet.favorite()   
      api.update_status(status="@" + tweet.user.screen_name + comment, in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
      user_list.add_user(tweet.user.id_str)
    else:
       print("User already in list")
          
    # time.sleep(60)
  except tweepy.TweepError as e:
    print(e)
    # time.sleep(60)
  except StopIteration:
    break