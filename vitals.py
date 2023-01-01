import json
import config
import discord

def is_registered(uid: int) -> bool:
    with open(config.USER_FILES + 'users.json', 'r') as f:
        if str(uid) in (jdta := json.load(f)):
            return jdta
        return False

class UserNotRegistered(discord.Embed):
    def __init__(self):
        super(UserNotRegistered, self).__init__(title='User Not Registered', description='You must be registered to run this command! Run `/register` to register!', color=config.COLOR)
