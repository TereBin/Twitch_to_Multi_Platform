import requests

# get channel data from twitch. get it every minute
def check_twitch(streamer_id, app_key, auth_token):
    stream_headers = {'client-id': app_key, 'Authorization': auth_token}
    try:
        stream_req = requests.get(f"https://api.twitch.tv/helix/search/channels?query={streamer_id}", headers=stream_headers)
    except tweepy.errors.Forbidden as err:
        err_str = str(err)
        with open(err_log_path, 'a') as f:
            err_code = "[" + str(time.strftime('%m/%d %H:%M', time.localtime(time.time()))) + "] " + "req error : \n" + err_str + "\n"
            f.write(err_code)
            print("req error! twitch 연결 불가")
            pass

    stream_data_json = stream_req.json()["data"]

    # check for specific streamer
    i = 0
    category = ""
    title = ""
    is_live = False  # refreshing variable is_live
    while i < len(stream_data_json):
        stream_data = stream_data_json[i]
        if stream_data["broadcaster_login"] == streamer_id:
            is_live = stream_data["is_live"]
            category = stream_data["game_name"]
            title = stream_data["title"]
            print(stream_data["display_name"])
            break
        else:
            i += 1

    if is_live:
        print("online")
        return is_live, category, title

    else:
        print("offline")
        return is_live, category, title
