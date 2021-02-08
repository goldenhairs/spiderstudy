import matplotlib.pyplot as plt

china_datas = [
    {'confirmedCount': 96807, 'confirmedIncr': 45, 'curedCount': 90704, 'curedIncr': 107, 'currentConfirmedCount': 1314,
     'currentConfirmedIncr': -62, 'dateId': 20210101, 'deadCount': 4789, 'deadIncr': 0, 'highDangerCount': 0,
     'midDangerCount': 0, 'suspectedCount': 4273, 'suspectedCountIncr': 0},
    {'confirmedCount': 96894, 'confirmedIncr': 87, 'curedCount': 90788, 'curedIncr': 84, 'currentConfirmedCount': 1315,
     'currentConfirmedIncr': 1, 'dateId': 20210102, 'deadCount': 4791, 'deadIncr': 2, 'highDangerCount': 0,
     'midDangerCount': 0, 'suspectedCount': 4303, 'suspectedCountIncr': 30},
    {'confirmedCount': 96972, 'confirmedIncr': 78, 'curedCount': 90851, 'curedIncr': 63, 'currentConfirmedCount': 1330,
     'currentConfirmedIncr': 15, 'dateId': 20210103, 'deadCount': 4791, 'deadIncr': 0, 'highDangerCount': 0,
     'midDangerCount': 0, 'suspectedCount': 4323, 'suspectedCountIncr': 20},
    {'confirmedCount': 97061, 'confirmedIncr': 89, 'curedCount': 90914, 'curedIncr': 63, 'currentConfirmedCount': 1353,
     'currentConfirmedIncr': 23, 'dateId': 20210104, 'deadCount': 4794, 'deadIncr': 3, 'highDangerCount': 0,
     'midDangerCount': 0, 'suspectedCount': 4339, 'suspectedCountIncr': 16},
    {'confirmedCount': 97127, 'confirmedIncr': 66, 'curedCount': 91008, 'curedIncr': 94, 'currentConfirmedCount': 1325,
     'currentConfirmedIncr': -28, 'dateId': 20210105, 'deadCount': 4794, 'deadIncr': 0, 'highDangerCount': 0,
     'midDangerCount': 0, 'suspectedCount': 4348, 'suspectedCountIncr': 9},
    {'confirmedCount': 97217, 'confirmedIncr': 90, 'curedCount': 91106, 'curedIncr': 98, 'currentConfirmedCount': 1316,
     'currentConfirmedIncr': -9, 'dateId': 20210106, 'deadCount': 4795, 'deadIncr': 1, 'highDangerCount': 0,
     'midDangerCount': 0, 'suspectedCount': 4359, 'suspectedCountIncr': 11},
    {'confirmedCount': 97306, 'confirmedIncr': 89, 'curedCount': 91188, 'curedIncr': 82, 'currentConfirmedCount': 1323,
     'currentConfirmedIncr': 7, 'dateId': 20210107, 'deadCount': 4795, 'deadIncr': 0, 'highDangerCount': 0,
     'midDangerCount': 0, 'suspectedCount': 4375, 'suspectedCountIncr': 16},
    {'confirmedCount': 97387, 'confirmedIncr': 81, 'curedCount': 91262, 'curedIncr': 74, 'currentConfirmedCount': 1329,
     'currentConfirmedIncr': 6, 'dateId': 20210108, 'deadCount': 4796, 'deadIncr': 1, 'highDangerCount': 0,
     'midDangerCount': 0, 'suspectedCount': 4391, 'suspectedCountIncr': 16},
    {'confirmedCount': 97518, 'confirmedIncr': 131, 'curedCount': 91351, 'curedIncr': 89, 'currentConfirmedCount': 1369,
     'currentConfirmedIncr': 40, 'dateId': 20210109, 'deadCount': 4798, 'deadIncr': 2, 'highDangerCount': 0,
     'midDangerCount': 0, 'suspectedCount': 4412, 'suspectedCountIncr': 21},
    {'confirmedCount': 97652, 'confirmedIncr': 134, 'curedCount': 91418, 'curedIncr': 67, 'currentConfirmedCount': 1435,
     'currentConfirmedIncr': 66, 'dateId': 20210110, 'deadCount': 4799, 'deadIncr': 1, 'highDangerCount': 0,
     'midDangerCount': 0, 'suspectedCount': 4430, 'suspectedCountIncr': 18}]
usa_datas = [
    {'confirmedCount': 20074798, 'confirmedIncr': 329661, 'curedCount': 9136262, 'curedIncr': 379112,
              'currentConfirmedCount': 10591334, 'currentConfirmedIncr': -54239, 'dateId': 20210101,
              'deadCount': 347202, 'deadIncr': 4788, 'highDangerCount': 0, 'midDangerCount': 0, 'suspectedCount': 0,
              'suspectedCountIncr': 0},
             {'confirmedCount': 20136182, 'confirmedIncr': 61384, 'curedCount': 9170094, 'curedIncr': 33832,
              'currentConfirmedCount': 10618218, 'currentConfirmedIncr': 26884, 'dateId': 20210102, 'deadCount': 347870,
              'deadIncr': 668, 'highDangerCount': 0, 'midDangerCount': 0, 'suspectedCount': 0, 'suspectedCountIncr': 0},
             {'confirmedCount': 20430979, 'confirmedIncr': 294797, 'curedCount': 9223561, 'curedIncr': 53467,
              'currentConfirmedCount': 10857204, 'currentConfirmedIncr': 238986, 'dateId': 20210103,
              'deadCount': 350214, 'deadIncr': 2344, 'highDangerCount': 0, 'midDangerCount': 0, 'suspectedCount': 0,
              'suspectedCountIncr': 0},
             {'confirmedCount': 20639854, 'confirmedIncr': 208875, 'curedCount': 9312768, 'curedIncr': 89207,
              'currentConfirmedCount': 10975496, 'currentConfirmedIncr': 118292, 'dateId': 20210104,
              'deadCount': 351590, 'deadIncr': 1376, 'highDangerCount': 0, 'midDangerCount': 0, 'suspectedCount': 0,
              'suspectedCountIncr': 0},
             {'confirmedCount': 20823856, 'confirmedIncr': 184002, 'curedCount': 9471656, 'curedIncr': 158888,
              'currentConfirmedCount': 10998572, 'currentConfirmedIncr': 23076, 'dateId': 20210105, 'deadCount': 353628,
              'deadIncr': 2038, 'highDangerCount': 0, 'midDangerCount': 0, 'suspectedCount': 0,
              'suspectedCountIncr': 0},
             {'confirmedCount': 21051001, 'confirmedIncr': 227145, 'curedCount': 9595733, 'curedIncr': 124077,
              'currentConfirmedCount': 11097883, 'currentConfirmedIncr': 99311, 'dateId': 20210106, 'deadCount': 357385,
              'deadIncr': 3757, 'highDangerCount': 0, 'midDangerCount': 0, 'suspectedCount': 0,
              'suspectedCountIncr': 0},
             {'confirmedCount': 21305323, 'confirmedIncr': 254322, 'curedCount': 9664784, 'curedIncr': 69051,
              'currentConfirmedCount': 11279242, 'currentConfirmedIncr': 181359, 'dateId': 20210107,
              'deadCount': 361297, 'deadIncr': 3912, 'highDangerCount': 0, 'midDangerCount': 0, 'suspectedCount': 0,
              'suspectedCountIncr': 0},
             {'confirmedCount': 21579578, 'confirmedIncr': 274255, 'curedCount': 9729398, 'curedIncr': 64614,
              'currentConfirmedCount': 11484863, 'currentConfirmedIncr': 205621, 'dateId': 20210108,
              'deadCount': 365317, 'deadIncr': 4020, 'highDangerCount': 0, 'midDangerCount': 0, 'suspectedCount': 0,
              'suspectedCountIncr': 0},
             {'confirmedCount': 21870988, 'confirmedIncr': 291410, 'curedCount': 9785511, 'curedIncr': 56113,
              'currentConfirmedCount': 11716545, 'currentConfirmedIncr': 231682, 'dateId': 20210109,
              'deadCount': 368932, 'deadIncr': 3615, 'highDangerCount': 0, 'midDangerCount': 0, 'suspectedCount': 0,
              'suspectedCountIncr': 0},
             {'confirmedCount': 22138418, 'confirmedIncr': 267430, 'curedCount': 9827904, 'curedIncr': 42393,
              'currentConfirmedCount': 11937992, 'currentConfirmedIncr': 221447, 'dateId': 20210110,
              'deadCount': 372522, 'deadIncr': 3590, 'highDangerCount': 0, 'midDangerCount': 0, 'suspectedCount': 0,
              'suspectedCountIncr': 0}]

time = []
china = []
usa = []

for data in china_datas:
    time.append(str(data['dateId']))
    china.append(data['confirmedIncr'])

for data in usa_datas:
    usa.append(data['confirmedIncr'])

plt.figure(figsize=(10, 8), dpi=80)

china_bar = plt.bar([i-0.1 for i in range(0, len(time))], china, width=0.2, label='中国')
usa_bar = plt.bar([i+0.1 for i in range(0, len(time))], usa, width=0.2, label='美国')

i = 0
for c, u in zip(china, usa):
    plt.text(i - 0.2, c + 5, c)
    plt.text(i, u + 5, u)
    i += 1

plt.legend()

plt.xticks(range(0, len(time)), ['1月{}日'.format(i) for i in range(1, 11)])

plt.show()
