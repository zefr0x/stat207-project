# Average Hours of Video Content pre Day + Average Hours of Text Content pre Day

import csv

import matplotlib.pyplot as plt
import statistics


with open("sample.csv", "r") as f:
    data = list(csv.reader(f))


totals = []

# Getting needed data
for row in data[1:]:
    totals.append(float(row[12]) + float(row[14]))

print("Mean:", sum(totals) / len(totals))
print("Standard Deviation:", statistics.stdev(totals))
###

# Drawing

plt.rcParams.update({"font.size": 20})
plt.rcParams["figure.autolayout"] = True

fig, ax1 = plt.subplots(figsize=(10, 6))

plt.hist(totals, rwidth=0.9)

plt.xlabel("Total Hours in Social Media")
plt.ylabel("Number of People")

plt.show()
