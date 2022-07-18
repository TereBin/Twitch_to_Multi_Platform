import requests

streamer_ID = 'soonps'
# get app_key and app_secret from local txt file
app_data_txt = open("D:/TereBin/TtTB/twitch_app_data.txt", 'r')
app_data = app_data_txt.read().splitlines()
app_key = app_data[0]
app_secret = app_data[1]
app_data_txt.close()

# get access_token and token_type from oauth2
auth_req = requests.post('https://id.twitch.tv/oauth2/token?client_id=' + app_key + '&client_secret=' + app_secret + '&grant_type=client_credentials')
auth_req_json = auth_req.json()

access_token = auth_req_json["access_token"]
token_type = auth_req_json["token_type"]
token_type = token_type[0].upper() + token_type[1:]

auth_token = token_type+" "+access_token
# print(auth_token)
headers = {'client-id':app_key, 'Authorization':auth_token}

# get channel data from twitch
stream_req = requests.get(f"https://api.twitch.tv/helix/search/channels?query={streamer_ID}", headers=headers)
stream_req_json = stream_req.json()

# check for specific streamer
i = 0
while i < len(stream_req_json["data"]):
    if stream_req_json["data"][i]["broadcaster_login"] == streamer_ID :
        is_live = stream_req_json["data"][i]["is_live"]
        break
    else :
        i+=1

print(is_live)
