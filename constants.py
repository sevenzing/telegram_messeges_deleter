BOT_TOKEN = ''

with open('stickers.txt') as f:
    stickers = list(map(str.strip, f.readlines()))