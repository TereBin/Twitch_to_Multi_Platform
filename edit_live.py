import json

streamer_json_path = "D:/TereBin/TtTB/streamer_list.json"
live_stream = 1
def edit_list(streamer_json_path, live_stream):
    streamer_json = json.load(open(streamer_json_path, 'r', encoding='utf-8'))  # open streamer_list.json as streamer_json
    streamer_json[str(live_stream)]["4_signal"] = "False"
    with open(streamer_json_path, 'w') as file:
        json.dump(streamer_json, file, indent="\t")
