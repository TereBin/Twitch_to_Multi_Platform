# check list of streamers. check it every minute.

import json

def read_list(streamer_json_path):
    streamer_json = open(streamer_json_path, 'r', encoding='utf-8')  # open streamer_list.json as streamer_json
    streamer_dict = json.load(streamer_json)  # make streamer_json to streamer_dict
    streamer_json.close()
    return streamer_dict
