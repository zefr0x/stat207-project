# Gender .vs Type of Videos Mostly Watch in Social Media

import csv

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency


with open("sample.csv", "r") as f:
    data = list(csv.reader(f))


male = {
    "قِصص stories": 0,
    "مقاطع قصيرة tiktoks": 0,
    "مقاطع طويلة youtubes": 0,
    "بُثُوث مباشرة": 0,
}
female = {
    "قِصص stories": 0,
    "مقاطع قصيرة tiktoks": 0,
    "مقاطع طويلة youtubes": 0,
    "بُثُوث مباشرة": 0,
}
total = {
    "قِصص stories": 0,
    "مقاطع قصيرة tiktoks": 0,
    "مقاطع طويلة youtubes": 0,
    "بُثُوث مباشرة": 0,
}

# Getting just gender and Type of Videos Mostly Watch in Social Media
for row in data[1:]:
    if row[5] == "أُنثى":
        female[row[11]] += 1
    elif row[5] == "ذكر":
        male[row[11]] += 1
    total[row[11]] += 1

print(f"{male=}")
print(f"{female=}")
print(f"{total=}")

###

males_count = sum(male.values())
females_count = sum(female.values())
print(f"{males_count=}, {females_count=}\n")

print("males%:", {y: x / males_count for y, x in male.items()})
print("females%:", {y: x / females_count for y, x in female.items()})

# Chi-square test

stat, p, dof, expected = chi2_contingency([list(male.values()), list(female.values())])
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

x_categories = ("stories", "tiktoks", "youtubes", "live streams")
x_axis = np.arange(len(x_categories))

plt.bar(x_axis - 0.2, [x / males_count for x in male.values()], 0.4, label="Males")
plt.bar(
    x_axis + 0.2, [x / females_count for x in female.values()], 0.4, label="Females"
)

plt.xticks(x_axis, x_categories)
plt.xlabel("Type of Watched Content")
plt.ylabel("Percentage of People")
plt.title("Male/Female usage of diffrent content types")

plt.legend()
plt.show()
