import json

streamer_json_path = "D:/TereBin/TtTB/data/streamer_list.json"

def edit_list(i, is_live):
    streamer_json = json.load(
        open(streamer_json_path, 'r', encoding='utf-8'))  # readable
    if is_live and streamer_json[str(i)]["4_signal"] == "False":
        streamer_json[str(i)]["4_signal"] = "True"
        with open(streamer_json_path, 'w', encoding='utf-8') as file:
            json.dump(streamer_json, file, indent="\t")
        print("방송시작\n")
        return True
    if (is_live == False) and streamer_json[str(i)]["4_signal"] == "True":
        streamer_json[str(i)]["4_signal"] = "False"
        with open(streamer_json_path, 'w', encoding='utf-8') as file:
            json.dump(streamer_json, file, indent="\t")
        print("방송종료\n")
        return False
    else:
        print("현상유지\n")
        return False
