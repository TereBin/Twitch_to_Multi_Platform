from pprint import pprint

from twitchAPI import Twitch, EventSub, UserAuthenticator, AuthScope

client_key = '******************************'
client_secret = '******************************'

twitch = Twitch(client_key, client_secret)
pprint(twitch.get_users(logins=['YOUR_TWITCH_ID']))
