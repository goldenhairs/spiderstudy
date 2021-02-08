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

time = []
china = []

for data in china_datas:
    time.append(str(data['dateId']))
    china.append(data['confirmedIncr'])


plt.figure(figsize=(10, 8), dpi=80)

plt.scatter(time, china)

plt.show()

