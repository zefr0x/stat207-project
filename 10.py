# Following Friends That you Realy Know

import csv

import matplotlib.pyplot as plt


with open("sample.csv", "r") as f:
    data = list(csv.reader(f))


labels = ["Yes", "No"]
choises = [0.0, 0.0]


# Getting needed data
for row in data[1:]:
    if row[19] == "أجل":
        choises[0] += 1
    elif row[19] == "لا":
        choises[1] += 1


_sum = sum(choises)
choises = [(x / _sum) * 100 for x in choises]

###

# Drawing

plt.rcParams.update({"font.size": 20})
plt.rcParams["figure.autolayout"] = True

fig, ax1 = plt.subplots(figsize=(10, 6))

explode = (0, 0.1)

ax1.pie(
    choises,
    explode=explode,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    startangle=90,
)

ax1.axis("equal")

plt.title("Folowing Real Friends")

plt.show()
