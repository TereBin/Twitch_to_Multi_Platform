from pprint import pprint

from twitchAPI import Twitch, EventSub, UserAuthenticator, AuthScope

app_key = '******************************' #use your own
app_secret = '******************************' #use your own

twitch = Twitch(app_key, app_secret)
user_info = twitch.get_users(logins=['YOUR_TWITCH_ID'])
pprint(user_info)

user_id = user_info['data'][0]['id']
pprint(user_id)

target_scope = [AuthScope.BITS_READ]
auth = UserAuthenticator(twitch, target_scope, force_verify=False)
token, refresh_token = auth.authenticate()
twitch.set_user_authentication(token, target_scope, refresh_token)
