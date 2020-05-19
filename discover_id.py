import os, slackclient

SLACK_BOT_NAME = os.environ.get('SLACK_BOT_NAME')
SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')

# initialize slack client
slack_bot_client = slackclient.SlackClient(SLACK_BOT_TOKEN)

# find slack bot's id
if(slack_bot_client.api_call("users.list").get('ok')):
    for user in slack_bot_client.api_call("users.list").get('members'):
        if user.get('name') == SLACK_BOT_NAME:
            print(SLACK_BOT_NAME + " ID: " + user.get('id'))
else:
    print('Could not find bot :(')
