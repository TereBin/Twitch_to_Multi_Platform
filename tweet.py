import tweepy


def send_tweet(tweet):
    api_key = '*************************'
    api_secret = '**************************************************'
    access_token = '**************************************************'
    access_secret = '*********************************************'

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)
    bot = tweepy.API(auth)
    bot.update_status(tweet)


tweet = "API 활용 봇 트윗 테스트입니다"

send_tweet(tweet)
