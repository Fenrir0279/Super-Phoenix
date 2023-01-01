import tomllib

with open('data.toml', 'rb') as f:
    text = tomllib.load(f)

TOKEN = text['TOKEN']
COGS = text['COGS']

USER_FILES = text['USER_FILES']
COLOR = text['COLOR']
