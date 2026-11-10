
import matplotlib.pyplot as plt
import numpy as np

# Sample dataset
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

students = ['A', 'B', 'C', 'D', 'E']
marks = [75, 85, 65, 90, 80]

# 1. Line Graph
plt.figure()
plt.plot(x, y, marker='o')
plt.title("Line Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid()
plt.show()

# 2. Scatter Plot
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 3. Bar Chart
plt.figure()
plt.bar(students, marks)
plt.title("Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 4. Horizontal Bar Chart
plt.figure()
plt.barh(students, marks)
plt.title("Horizontal Bar Chart")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.show()

# 5. Histogram
plt.figure()
plt.hist(marks, bins=5, edgecolor='black')
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 6. Pie Chart
plt.figure()
plt.pie(marks, labels=students, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

# 7. Box Plot
plt.figure()
plt.boxplot(marks)
plt.title("Box Plot")
plt.ylabel("Marks")
plt.show()

# 8. Area Plot
plt.figure()
plt.fill_between(x, y, alpha=0.5)
plt.title("Area Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 9. Multiple Graphs using Subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot(x, y, marker='o')
axes[0, 0].set_title("Line Graph")

axes[0, 1].scatter(x, y)
axes[0, 1].set_title("Scatter Plot")

axes[1, 0].bar(students, marks)
axes[1, 0].set_title("Bar Chart")

axes[1, 1].hist(marks, bins=5)
axes[1, 1].set_title("Histogram")

plt.tight_layout()
plt.show()
