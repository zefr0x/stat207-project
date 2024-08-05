# Type of Videos Mostly Watch in Social Media vs. Average Hours of Sleep

import csv

import matplotlib.pyplot as plt


with open("sample.csv", "r") as f:
    data = list(csv.reader(f))

labels = ["Stories", "tiktoks", "youtubes", "Live Streams"]
choises: list[list[float]] = [[], [], [], []]


# Getting needed data
for row in data[1:]:
    if row[11] == "قِصص stories":
        choises[0].append(float(row[10]))
    elif row[11] == "مقاطع قصيرة tiktoks":
        choises[1].append(float(row[10]))
    elif row[11] == "مقاطع طويلة youtubes":
        choises[2].append(float(row[10]))
    elif row[11] == "بُثُوث مباشرة":
        choises[3].append(float(row[10]))

###

print({label: len(choise) for label, choise in zip(labels, choises)})

# Drawing

plt.rcParams.update({"font.size": 20})
plt.rcParams["figure.autolayout"] = True

fig, ax1 = plt.subplots(figsize=(10, 6))

box = plt.boxplot(choises, tick_labels=labels, showmeans=True)

plt.xlabel("Type of Videos Mosty Watched")
plt.ylabel("Average Hours of Sleep")

plt.show()
