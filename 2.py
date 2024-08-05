# Following Friends That you Realy Know .vs Interact with others or just watch them

import csv

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency


with open("sample.csv", "r") as f:
    data = list(csv.reader(f))


friend_you_know = {"أجل، أتفاعل": 0, "لا، أُفضل المتابعة فقط": 0}
strange_people = {"أجل، أتفاعل": 0, "لا، أُفضل المتابعة فقط": 0}
total = {"أجل، أتفاعل": 0, "لا، أُفضل المتابعة فقط": 0}

# Getting just gender and Type of Videos Mostly Watch in Social Media
for row in data[1:]:
    if row[19] == "أجل":
        strange_people[row[20]] += 1
    elif row[19] == "لا":
        friend_you_know[row[20]] += 1
    total[row[20]] += 1

print(f"{friend_you_know=}")
print(f"{strange_people=}")
print(f"{total=}")

###

friends_you_know_count = sum(friend_you_know.values())
strange_poeple_count = sum(strange_people.values())
print(f"{friends_you_know_count=}, {strange_poeple_count=}\n")

print(
    "folow_friends%:",
    {y: x / friends_you_know_count for y, x in friend_you_know.items()},
)
print(
    "folow_strangers%:",
    {y: x / strange_poeple_count for y, x in strange_people.items()},
)

# Chi-square test

stat, p, dof, expected = chi2_contingency(
    [list(friend_you_know.values()), list(strange_people.values())]
)
print("\n#Chi-sqaure test")
print("Test statistic:", stat)
print("Degree of freedom:", dof)
print("Expected values:", expected, sep="\n")
print("Total expected:", [x + y for x, y in zip(*expected)], sep="\n")

# interpret p-value

alpha = 0.05
print("\np value is", p)
if p <= alpha:
    print("Dependent (reject H0)")
else:
    print("Independent (H0 holds true)")

# Drawing

plt.rcParams.update({"font.size": 20})

fig = plt.figure(figsize=(10, 6))

x_categories = ("Intract", "Don't Intract")
x_axis = np.arange(len(x_categories))

plt.bar(
    x_axis - 0.2,
    [x / friends_you_know_count for x in friend_you_know.values()],
    0.4,
    label="Folowing Friends",
)
plt.bar(
    x_axis + 0.2,
    [x / strange_poeple_count for x in strange_people.values()],
    0.4,
    label="Folowing Strangers",
)

plt.xticks(x_axis, x_categories)
plt.xlabel("Intraction Status")
plt.ylabel("Percentage of People Intraction")
plt.title("Effect of Folowing Friends in Intractions")

plt.legend()
plt.show()
