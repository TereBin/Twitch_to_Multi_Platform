import json

streamer_json_path = "D:/TereBin/TtTB/streamer_list.json"
live_stream = 1

def edit_live(streamer_json_path, is_live, live_stream):
    streamer_json = json.load(
        open(streamer_json_path, 'r', encoding='utf-8'))  # open streamer_list.json as streamer_json
    file = json.load(open(streamer_json_path, 'w', encoding='utf-8'))
    if is_live == "True" and streamer_json[str(live_stream)]["4_signal"] == "False":
        streamer_json[str(live_stream)]["4_signal"] = "True"
        json.dumps(streamer_json, file, indent="\t")
        return True
    elif is_live == "False" and streamer_json[str(live_stream)]["4_signal"] == "True":
        streamer_json[str(live_stream)]["4_signal"] = "False"
        json.dumps(streamer_json, file, indent="\t")
        return None
    else:
        return None
