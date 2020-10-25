BOT_TOKEN = ''
BOT_ADMIN = 339999894
with open('stickers.txt') as f:
    stics = list(map(str.split, map(str.strip, f.readlines())))
    stickers = {}
    for stic, start, end in stics:
        stickers[stic] = (start, end)
    print(stickers)

redis = {
    'host': 'redis',
    'port': 5432,

}