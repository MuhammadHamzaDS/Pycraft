import pandas as pd

student = pd.DataFrame({
    "name": ["Ali", "Ayesha", "Ahmed", "Sara", "Hamza"],
    "age": [16, 17, 16, 18, 17],
    "marks": [85, 90, 78, 88, 95],
    "grade": ["A", "A", "B", "A", "A"]
})
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Box plot of marks distribution
plt.figure(figsize=(6,4))
sns.boxplot(y=student["marks"])
plt.title("Marks Distribution - Boxplot")
plt.show()

# 2. Violin plot comparing marks by grade
plt.figure(figsize=(6,4))
sns.violinplot(x="grade", y="marks", data=student)
plt.title("Marks by Grade - Violin Plot")
plt.show()

# 3. Heatmap of correlation between age and marks
plt.figure(figsize=(5,4))
corr = student[["age", "marks"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap (Age vs Marks)")
plt.show()
