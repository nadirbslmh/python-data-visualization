import matplotlib.pyplot as plt

grades_a = [75, 78, 88, 90, 95]
grades_b = [66, 67, 70, 95, 90]
grades_c = [80, 80, 80, 75, 85]

plt.title("Student Progress")

plt.ylabel("Scores")

plt.plot(grades_a, label="Student A")
plt.plot(grades_b, label="Student B")
plt.plot(grades_c, label="Student C")

plt.legend(loc="lower right")

plt.show()
