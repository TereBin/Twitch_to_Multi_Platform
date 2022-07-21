import tweepy

def tweet(twitter_api_data_path, tweet, link):
    twitter_data_txt = open(twitter_api_data_path, 'r')
    twitter_data = twitter_data_txt.read().splitlines()
    api_key = twitter_data[0]
    api_secret = twitter_data[1]
    access_token = twitter_data[2]
    access_secret = twitter_data[3]
    twitter_data_txt.close()
    tweet = tweet + "\n" + link

    def send_tweet(tweet, api_key, api_secret, access_token, access_secret):
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_secret)
        bot = tweepy.API(auth)
        bot.update_status(status=tweet)

    print(tweet)
    send_tweet(tweet, api_key, api_secret, access_token, access_secret)
