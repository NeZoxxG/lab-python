from collections import *
f = open("/Users/nezoxxg/sport.txt", "r", encoding="cp1251")
text = f.readlines()
sports = []
for line in text[1:]:
    parts = line.split('\t')
    if parts[3] == '':
        continue
    else:
        sport = parts[3].strip()
        sports.append(sport)
sports_3 = Counter(sports)
print(sports_3.most_common(3))
