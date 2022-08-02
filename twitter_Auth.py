import tweepy
import json
import pprint as pp

twitter_api_data_path = "D:/TereBin/TtTB/twitter_api_data.txt"
twitter_data_txt = open(twitter_api_data_path, 'r')
twitter_data = twitter_data_txt.read().splitlines()
api_key = twitter_data[0]
api_secret = twitter_data[1]
twitter_data_txt.close()

streamer_json_path = "D:/TereBin/TtTB/data/streamer_list.json"
streamer_json = json.load(
        open(streamer_json_path, 'r', encoding='utf-8'))  # readable

pp.pprint(streamer_json)
'''
twitch_id = input("트위치 아이디를 적어주세요 : ")
twitter_id = input("트위터 아이디를 적어주세요  : ")
tweet = input("원하는 문장을 적어주세요 : ")

print(twitch_id, twitter_id, tweet)

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
'''

oauth1_user_handler = tweepy.OAuth1UserHandler(api_key, api_secret, callback='oob')
print(oauth1_user_handler.get_authorization_url(signin_with_twitter=True))

verifier = input("Input PIN: ")
access_token, access_secret = oauth1_user_handler.get_access_token(verifier)
print(access_token)
print(access_secret)
