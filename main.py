import json
import requests
import tweepy
import time

streamer_json_path = "D:/TereBin/TtTB/streamer_list.json"
app_data_path = "D:/TereBin/TtTB/twitch_app_data.txt"
twitter_api_data_path = "D:/TereBin/TtTB/twitter_api_data.txt"

def check_list(streamer_json_path):
    streamer_json = open(streamer_json_path, 'r', encoding='utf-8')  # open streamer_list.json as streamer_json
    streamer_dict = json.load(streamer_json)  # make streamer_json to streamer_dict
    return streamer_dict

def check_twitch(app_data_path, streamer_ID):
    # get app_key and app_secret from local txt file
    app_data_txt = open(app_data_path, 'r')
    app_data = app_data_txt.read().splitlines()
    app_key = app_data[0]
    app_secret = app_data[1]
    app_data_txt.close()

    # get access_token and token_type from oauth2
    auth_req = requests.post(
        'https://id.twitch.tv/oauth2/token?client_id=' + app_key + '&client_secret=' + app_secret + '&grant_type=client_credentials')
    auth_req_json = auth_req.json()

    access_token = auth_req_json["access_token"]
    token_type = auth_req_json["token_type"]
    token_type = token_type[0].upper() + token_type[1:]

    auth_token = token_type + " " + access_token
    # print(auth_token)
    headers = {'client-id': app_key, 'Authorization': auth_token}

    # get channel data from twitch
    stream_req = requests.get(f"https://api.twitch.tv/helix/search/channels?query={streamer_ID}", headers=headers)
    stream_req_json = stream_req.json()["data"]

    # check for specific streamer
    i = 0
    is_live = False # refreshing variable is_live
    while i < len(stream_req_json):
        if stream_req_json[i]["broadcaster_login"] == streamer_ID:
            is_live = stream_req_json[i]["is_live"]
            print(stream_req_json[i]["display_name"])
            break
        else:
            i += 1

    if is_live:
        print("online\n")

    else:
        print("offline\n")

    return is_live

def tweet(twitter_api_data_path, tweet, link):
    twitter_data_txt = open(twitter_api_data_path, 'r')
    twitter_data = twitter_data_txt.read().splitlines()
    api_key = twitter_data[0]
    api_secret = twitter_data[1]
    access_token = twitter_data[2]
    access_secret = twitter_data[3]
    twitter_data_txt.close()
    tweet = tweet + "\n" + link

    def send_tweet(tweet, api_key, api_secret, access_token, access_secret):
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_secret)
        bot = tweepy.API(auth)
        bot.update_status(status=tweet)

    send_tweet(tweet, api_key, api_secret, access_token, access_secret)

# check for streamer that is online and send tweet about it
# while True :
streamer_dict = check_list(streamer_json_path)

i = 0
while i < len(streamer_dict) :
    is_live = check_twitch(app_data_path, streamer_dict[str(i)]["1_twitch_id"])
    if is_live:
        tweet(twitter_api_data_path, streamer_dict[str(i)]["3_tweet"], "twitch.tv/" + streamer_dict[str(i)]["1_twitch_id"])
    i+=1
    time.sleep(60)
