import matplotlib.pyplot as plt

movie_name = ['雷神3：诸神黄昏', '正义联盟', '东方快车谋杀案', '寻梦环游记', '全球风暴', '降魔传', '追捕', '七十七天', '密战', '狂兽', '其它']

place_count = [60605, 54546, 45819, 28243, 13270, 9945, 7679, 6799, 6101, 4621, 20105]

plt.figure(figsize=(20, 15), dpi=50)

plt.pie(place_count, labels=movie_name, autopct="%1.2f%%")

plt.legend()

plt.show()
