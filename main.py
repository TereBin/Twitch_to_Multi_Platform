import tweepy


def send_tweet(tweet):
    api_key = 'IfvXwObubZGJQx8zkpw7DZ79U'
    api_secret = 'FtUuIbphcpn3vE1v3tDEjHs2wV7H2cnrmPbswZcMye27eSb2Sj'
    access_token = '1116920083291365376-m8JDBmQPVdghV6mCgZmWBbyJqspxfH'
    access_secret = 'SBCY1zlVMd1kPeIoA3AjpbTBNbD5OCaBfpIN71EPd42A0'

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)
    bot = tweepy.API(auth)
    bot.update_status(tweet)


tweet = "API 활용 봇 생성 테스트입니다"

send_tweet(tweet)
