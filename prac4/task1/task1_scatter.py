# task1_scatter.py
import matplotlib.pyplot as plt

street = [80, 98, 75, 91, 78]
garage = [100, 82, 105, 89, 102]
days = ['Mon','Tue','Wed','Thu','Fri']

plt.figure(figsize=(6,4))
plt.scatter(street, garage)
for i, txt in enumerate(days):
    plt.annotate(txt, (street[i], garage[i]), textcoords="offset points", xytext=(5,-5))
plt.xlabel("Улица")
plt.ylabel("Гараж")
plt.title("Диаграмма рассеяния: Улица vs Гараж")
plt.grid(True)
plt.show()
