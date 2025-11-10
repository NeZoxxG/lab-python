from collections import *
import urllib.request
url = "http://dfedorov.spb.ru/python3/sport.txt"
with urllib.request.urlopen(url) as response:
    text = response.read().decode('cp1251').splitlines()
sports = []
for line in text[1:]:
    parts = line.split('\t')
    if parts[3] == '':
        continue
    else:
        sport = parts[3].strip()
        if "," in sport:
            sport = sport.split(",")
            for i in range(len(sport)):
                sports.append(sport[i])
        else:
            sports.append(sport)

for i in range(len(sports)):
    sports[i] = sports[i].strip()

sports_3 = Counter(sports)
print(sports_3.most_common(3))


