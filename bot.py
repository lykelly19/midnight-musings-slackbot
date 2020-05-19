import os, time, slackclient
import quotable_api

# constants
READ_DELAY = 1

SLACK_BOT_NAME = os.environ.get('SLACK_BOT_NAME')
SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
SLACK_BOT_ID = os.environ.get('SLACK_BOT_ID')

slack_bot_client = slackclient.SlackClient(SLACK_BOT_TOKEN)


def is_private(event): # check if private channel
    channel = event.get('channel')
    return channel.startswith('D')

def post_message(message, channel):
    slack_bot_client.api_call('chat.postMessage', channel=channel, text=message, as_user=True)

def get_mention(user):
    return '<@{user}>'.format(user=user)

def is_for_me(event):
    type = event.get('type')
    if type and type == 'message' and not(event.get('user')==SLACK_BOT_ID):
        if is_private(event):
            return True
        text = event.get('text')
        channel = event.get('channel')
        if slack_bot_mention in text.strip().split():
            return True

def handle_message(message, user, channel):
    post_message(message=quotable_api.get_quote(), channel=channel)

def run():
    if slack_bot_client.rtm_connect():
        print(SLACK_BOT_NAME + " is on!")
        while True:
            event_list = slack_bot_client.rtm_read()
            if len(event_list) > 0:
                for event in event_list:
                    print(event)
                    if is_for_me(event):
                        handle_message(message=event.get('text'), user=event.get('user'), channel=event.get('channel'))
            time.sleep(READ_DELAY)
    else:
        print('Connection to Slack failed')

if __name__=='__main__':
    slack_bot_mention = get_mention(SLACK_BOT_ID)
    run()
