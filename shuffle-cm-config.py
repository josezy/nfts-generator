import json
import random

with open('./test/cache.uu', 'r+') as fp:
    f = json.load(fp)

items = list(f['items'].values())

random.shuffle(items)

for idx in range(10000):
    items[idx]['onChain'] = False
    f['items'][str(idx)] = items[idx]

with open('./test/mainnet-beta-shuffledlegends.uu', 'w+') as fp:

    fp.seek(0)
    json.dump(f, fp, separators=(',', ':'))
    fp.truncate()
