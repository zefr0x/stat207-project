# Religious Commitment .vs (Average Hours of Video Content pre Day + Average Hours of Text Content pre Day)

import csv

import matplotlib.pyplot as plt


with open("sample.csv", "r") as f:
    data = list(csv.reader(f))

labels = ["1/5", "2/5", "3/5", "4/5", "5/5"]
levels: list[list[float]] = [[], [], [], [], []]

# Getting needed data
for row in data[1:]:
    levels[int(row[9]) - 1].append(float(row[12]) + float(row[14]))

###

print({label: len(level) for label, level in zip(labels, levels)})

# Drawing

plt.rcParams.update({"font.size": 20})
plt.rcParams["figure.autolayout"] = True

fig, ax1 = plt.subplots(figsize=(10, 6))

box = plt.boxplot(levels, tick_labels=labels, showmeans=True)

plt.xlabel("Religious Commitment")
plt.ylabel("Total Time in Social Meida")

plt.show()
