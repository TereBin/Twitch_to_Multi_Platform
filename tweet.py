import tweepy

twitter_data_txt = open("D:/TereBin/TtTB/twitter_api_data.txt", 'r')
twitter_data = twitter_data_txt.read().splitlines()
api_key = twitter_data[0]
api_secret = twitter_data[1]
access_token = twitter_data[2]
access_secret = twitter_data[3]
twitter_data_txt.close()

def send_tweet(tweet, api_key, api_secret, access_token, access_secret):
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)
    bot = tweepy.API(auth)
    bot.update_status(tweet)

tweet = "API 활용 봇 트윗 테스트입니다\n보안성 테스트 중입니다"

send_tweet(tweet, api_key, api_secret, access_token, access_secret)
