# Age vs. Average Hours of Video Content pre Day

import csv

import numpy as np
import matplotlib.pyplot as plt
import pylab
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns
import pandas as pd


with open("sample.csv", "r") as f:
    data = list(csv.reader(f))


age = []
average_hours_of_video = []

# Getting just gender and Type of Videos Mostly Watch in Social Media
for row in data[1:]:
    age.append(int(row[6]))
    average_hours_of_video.append(float(row[12]))
    if float(row[12]) >= 20:
        print(row)

# Coefficient of correlation
slope, intercept, r, p, std_err = stats.linregress(age, average_hours_of_video)
print("r:", r)
print("r^2:", r**2 * 100, "%")
print("p:", p)
print("Slope:", slope)
print("Y-Intercept:", intercept)

# Find outliers
q1 = np.quantile(age, 0.25)
q3 = np.quantile(age, 0.75)
med = np.median(age)
iqr = q3 - q1

upper_bound = q3 + (1.5 * iqr)
lower_bound = q1 - (1.5 * iqr)

outliers_age = [x for x in age if (x <= lower_bound) or (x >= upper_bound)]
print("The following are the outliers in age:{}".format(outliers_age))

# Find outliers
q1 = np.quantile(average_hours_of_video, 0.25)
q3 = np.quantile(average_hours_of_video, 0.75)
med = np.median(average_hours_of_video)
iqr = q3 - q1

upper_bound = q3 + (1.5 * iqr)
lower_bound = q1 - (1.5 * iqr)

outliers_hours = [
    x for x in average_hours_of_video if (x <= lower_bound) or (x >= upper_bound)
]
print("The following are the outliers in average_hours_of_video:{}".format(outliers_hours))

# Statistical Inferences of Regression Model
x1_stats = sm.add_constant(age)
model = sm.OLS(average_hours_of_video, x1_stats)
results = model.fit()
print(results.summary())
print(results.params)

# Two-Way ANOVA
data_frame = pd.DataFrame(
    {"age": age, "average_hours_of_video": average_hours_of_video}
)
model = ols("age ~ C(average_hours_of_video)", data=data_frame).fit()
result = sm.stats.anova_lm(model, type=2)

print(result)

# Drawing
plt.rcParams.update({"font.size": 20})

fig = plt.figure(figsize=(10, 10))

plt.scatter(age, average_hours_of_video, s=60, alpha=0.7, edgecolors="k")

plt.axline(
    xy1=(0, intercept), slope=slope, label=f"$y = {slope:.1f}x {intercept:+.1f}$"
)

plt.xlabel("Age")
plt.ylabel("Average Hours of Video")
plt.title("ScatterPlot of Age and Average Hours of Watching Videos")

plt.show()

# Normal Quantile Plot
sm.qqplot(np.array(average_hours_of_video), dist=stats.distributions.norm)
pylab.show()

# Residual Plot

data = pd.DataFrame({"Age": age, "Residual": average_hours_of_video})
sns.residplot(x="Age", y="Residual", data=data)
plt.show()
