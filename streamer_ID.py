import json
import pprint as pp

path = "D:/TereBin/TtTB/streamer_list.json"

streamer_json = open(path, 'r', encoding='utf-8')
streamer_dict = json.load(streamer_json)
pp.pprint(streamer_dict)
