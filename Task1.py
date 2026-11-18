import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\Gen AI\Day 4\empoyees.csv")

avg = df.groupby("department")["salary"].mean()

plt.bar(avg.index,avg.values, color="green",
        label="Products Sold")

plt.xlabel("Department")
plt.ylabel("Salary")
plt.title("Average salary")
plt.legend()
plt.savefig("bar.png")
plt.show()

plt.hist(df["salary"], bins=5, color="blue",
        label="Products Sold")
plt.title("Salary Distribution")
plt.legend()
plt.savefig("hist.png")
plt.show()

for dept in df["department"].unique():
    data = df[df["department"] == dept] 
plt.scatter(data["id"], data["salary"], label=dept)
plt.xlabel("ID")
plt.ylabel("Salary")
plt.title("ID vs Salary")
plt.savefig("scatter.png")
plt.legend()
plt.show()


months = ["Jan", "feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]
plt.plot(months, sales, marker="o")
plt.savefig("line.png")
plt.show()
