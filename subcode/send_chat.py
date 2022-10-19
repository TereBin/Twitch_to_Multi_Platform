from twitch_chat_irc import twitch_chat_irc

def send_chat(twitch_bot_data_path, channel):
    username = 'TtTB_'
    oauth_data = open(twitch_bot_data_path, 'r', encoding='utf-8')
    oauth = oauth_data.read()
    oauth_data.close()
    connection = twitch_chat_irc.TwitchChatIRC(username, oauth)

    message = '[TtTB] 방송시작 알림이 자동으로 트윗되었습니다.'
    connection.send(channel, message)
    connection.close_connection()
