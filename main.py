import requests
import time

from read_list import read_list
from tweet import tweet
from twitch_check import check_twitch
from edit_list import edit_list

streamer_json_path = "D:/TereBin/TtTB/data/streamer_list.json"
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

# check for streamer that is online and send tweet about it
while True:
    streamer_dict = read_list(streamer_json_path)
    i = 1  # 0 is sample data
    while i < len(streamer_dict):
        streamer_data = streamer_dict[str(i)]
        is_live, game_name, title = check_twitch(streamer_data["1_twitch_id"], app_key, auth_token)
        live_change = edit_list(i, is_live)
        if live_change:
            print("트윗 전송")
            tweet(twitter_api_data_path, streamer_data, game_name, title, "twitch.tv/" + streamer_data["1_twitch_id"])
            print("\n")
        i += 1
    print("-"*50)
    time.sleep(60)
