import pprint as pp
import json
import requests
import time

from tweet import tweet
from twitch_check import check_twitch
from edit_live import edit_live

streamer_json_path = "D:/TereBin/TtTB/streamer_list.json"
app_data_path = "D:/TereBin/TtTB/twitch_app_data.txt"
twitter_api_data_path = "D:/TereBin/TtTB/twitter_api_data.txt"

# get twitch api key
app_data_txt = open(app_data_path, 'r')
app_data = app_data_txt.read().splitlines()
app_key = app_data[0]
app_secret = app_data[1]
app_data_txt.close()

# get access_token and token_type from twitch oauth2
auth_req = requests.post('https://id.twitch.tv/oauth2/token?client_id=' + app_key + '&client_secret=' + app_secret + '&grant_type=client_credentials')
auth_req_json = auth_req.json()
# parsing token and headers
access_token = auth_req_json["access_token"]
token_type = auth_req_json["token_type"]
token_type = token_type[0].upper() + token_type[1:]
auth_token = token_type + " " + access_token


# check list of streamers. check it every minute.
def read_list(streamer_json_path):
    streamer_json = open(streamer_json_path, 'r', encoding='utf-8')  # open streamer_list.json as streamer_json
    streamer_dict = json.load(streamer_json)  # make streamer_json to streamer_dict
    streamer_json.close()
    return streamer_dict
# check for streamer that is online and send tweet about it
# while True :
streamer_dict = read_list(streamer_json_path)
pp.pprint(streamer_dict)
i = 1  # 0 is sample data
while i < len(streamer_dict):
    streamer_data = streamer_dict[str(i)]
    is_live, live_stream = check_twitch(streamer_data["1_twitch_id"], app_key, auth_token)
    live_change = edit_live(streamer_json_path, is_live, live_stream + 1)
    if live_change :
        print("트윗 전송")
        tweet(twitter_api_data_path, streamer_data["3_tweet"], "twitch.tv/" + streamer_data["1_twitch_id"])
    i += 1
#  time.sleep(60)
