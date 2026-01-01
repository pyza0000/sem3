import matplotlib.pyplot as plt
import numpy as np
#task 1
# def task1():
#     x = np.linspace(-np.pi, np.pi, 100)
#     y1 = np.sin(x)
#     y2 = 2 * np.cos(x)
#     plt.plot(x, y1, label="sin(x)")
#     plt.plot(x, y2, label="2cos(x)")
#     plt.title("Wykres sin(x) oraz 2cos(x)")
#     plt.xlabel("x")
#     plt.ylabel("wartość funkcji")
#     plt.legend()
#     plt.grid(True)
#     plt.show()
#task 2
# def task2():
#     labels = 'Frogs', 'Cats', 'Dogs', 'Birds'
#     sizes = [20, 25, 40, 15]
#     explode = (0, 0.1, 0, 0)
#     fig1, ax1 = plt.subplots()
#     ax1.pie(
#         sizes,
#         explode=explode,
#         labels=labels,
#         autopct='%1.1f%%',
#         shadow=True,
#         startangle=90)
#     ax1.set_title("Wykres- zakres ludnosci zwierzat")
#     ax1.legend(labels, title="Zwierze",loc="center left", bbox_to_anchor=(1.0, 0.5))
#     plt.show()
#task 3
# def task3():
# #     fig, ax = plt.subplots()
# #     fruits = ['apple', 'blueberry', 'cherry', 'orange', 'strawberry']
# #     counts = [40, 100, 30, 55, 75]
# #     bar_labels = ['green', 'blue', '_red', 'orange','red']
# #     bar_colors = ['green', 'blue', 'red', 'orange','red']
# #     ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
# #     ax.set_ylabel('ilość spożytkowania')
# #     ax.set_title('Najchętniej spożywane owoce')
# #     ax.legend(title='nazwa owoca')
# #     plt.show()
#task 4
# def task4():
#     np.random.seed(4)
#     x = np.arange(10)
#     format1 = np.random.randint(0, 100, size=10)
#     format2 = np.random.randint(0, 100, size=10)
#     format3 = np.random.randint(0, 100, size=10)
#     plt.plot(x, format1, "Dg-", label="zielone diamenty")
#     plt.plot(x, format2, "*y-.", label="żółte gwiazdki")
#     plt.plot(x, format3, "pm--", label="fioletowe pięciokąty")
#     plt.title("liczby - różne formatowania linii")
#     plt.xlabel("X-<0-9>")
#     plt.ylabel("Y-losowe liczby całkowite")
#     plt.legend()
#     plt.grid(True)
#     plt.xticks(x)
#     plt.show()
#task 5
# def task5():
#     np.random.seed(7)
#     table = np.random.randint(0, 10, 100)
#     quantity = np.arange(10)
#     counts = np.bincount(table,minlength=10)
#     fig, ax = plt.subplots(1, 2, figsize=(10, 4))
#     ax[0].bar(quantity, counts)
#     ax[0].set_title("Liczba powtórzeń ")
#     ax[0].set_xlabel("Liczba")
#     ax[0].set_ylabel("występowanie")
#     ax[0].set_xticks(quantity)
#     ax[1].hist(table, bins=np.arange(-0.5, 10.5, 1), rwidth=0.9)
#     ax[1].set_title("Histogram ")
#     ax[1].set_xlabel("Liczba")
#     ax[1].set_ylabel("występowanie")
#     ax[1].set_xticks(quantity)
#     plt.show()
#task 6
# def task6():
#     x= np.linspace(-np.pi, np.pi, 100)
#     y = np.sin(x)
#     plt.plot(x,y, label='sin(x)')
#     plt.title("liczby - różne formatowania linii")
#     plt.xlabel("liczby")
#     plt.ylabel("wartości ")
#     plt.legend(title= "randomowe wartosci",loc="center left")
#     #plt.legend(loc=2)
#     plt.show()

if __name__ == "__main__":
    task6()