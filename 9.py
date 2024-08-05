# Topics You Are Following in Social Media

import csv

import matplotlib.pyplot as plt


with open("sample.csv", "r") as f:
    data = list(csv.reader(f))


labels = [
    "Comedy",
    "Gaming",
    "News",
    "Sports",
    "Vlogs",
    "Sience",
    "Food",
    "Songs",
    "Random",
    "Other",
]
topics = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


# Getting needed data
for row in data[1:]:
    for topic in row[17].split(";")[:-1]:
        if topic == "كوميديا":
            topics[0] += 1
        elif topic == "ألعاب":
            topics[1] += 1
        elif topic == "أخبار عالمية أو محلية":
            topics[2] += 1
        elif topic == "رياضات":
            topics[3] += 1
        elif topic == "حياة يومية لأشخاص":
            topics[4] += 1
        elif topic == "عُلُوم":
            topics[5] += 1
        elif topic == "طعام":
            topics[6] += 1
        elif topic == "أغاني":
            topics[7] += 1
        elif topic == "عشوائيات بشكل بحت (لا أُتابع موضوع معيَّن)":
            topics[8] += 1
        else:
            topics[9] += 1


_sum = sum(topics)
topics = [(x / _sum) * 100 for x in topics]

###

# Drawing

plt.rcParams.update({"font.size": 20})
plt.rcParams["figure.autolayout"] = True

fig, ax1 = plt.subplots(figsize=(10, 6))

explode = (0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0)

ax1.pie(
    topics,
    explode=explode,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    startangle=90,
)

ax1.axis("equal")

plt.title("Topics")

plt.show()
