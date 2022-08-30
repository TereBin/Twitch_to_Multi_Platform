import tweepy

def tweet(twitter_api_data_path, streamer_data, category, title, link):
    twitter_data_txt = open(twitter_api_data_path, 'r')
    twitter_data = twitter_data_txt.read().splitlines()
    api_key = twitter_data[0]
    api_secret = twitter_data[1]
    twitter_data_txt.close()
    tweet = streamer_data["3_tweet"]
    access_token = streamer_data["5_access_token"]
    access_secret = streamer_data["6_access_secret"]
    img_file = streamer_data["8_img"]
    streamer_req_data = list(map(str, streamer_data["7_req_data"].split(", ")))
    i = 0

    while i < len(streamer_req_data):
        # streamer_req_data[i] = distutils.util.strtobool(streamer_req_data[i]) 3.10 이후로 못쓴다
        if streamer_req_data[i] == "True" :
            streamer_req_data[i] = True
        else :
            streamer_req_data[i] = False

        i = i+1

    if streamer_req_data[0]:  # category
        tweet = tweet + "\n" + "카테고리 : [ " + category + " ]"
    if streamer_req_data[1]:  # title
        tweet = tweet + "\n" + "방제 : [ " + title + " ]"
    if streamer_req_data[2]:  # link
        tweet = tweet + "\n" + link
    img_upload = streamer_req_data[3]

    def send_tweet(tweet, img_upload, img_file, api_key, api_secret, access_token, access_secret):
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_secret)
        bot = tweepy.API(auth)
        if img_upload:
            bot.update_status_with_media(status=tweet, filename=img_file)
        else:
            bot.update_status(status=tweet)

    print(tweet)
    send_tweet(tweet, img_upload, img_file, api_key, api_secret, access_token, access_secret)


def test_tweet(tweet):
    api_key = '*************************'
    api_secret = '**************************************************'
    access_token = "**************************************************"
    access_secret = "*********************************************"
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)
    bot = tweepy.API(auth)
    bot.update_status(status=tweet)

test_tweet("TtTB 연결 테스트용 트윗입니다.")
