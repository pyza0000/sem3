import numpy as np
# def replace_zeros(A, x):
#     array1 = np.array(A)
#     array1[array1 == 0] = x
#     return array1.tolist()
# def task1():
#     A = [[0, 1, 0], [2, 0, 3]]
#     print(replace_zeros(A, 3))
# if __name__ == "__main__":
#     task1()
#task 2
# def medianize(A):
#     array2 = np.array(A, dtype=float)
#     mean = array2.mean()
#     return array2 - mean
# def task2():
#     A = [1,3,4,5,6,7,2,3,5,10]
#     print(medianize(A))
# if __name__ == "__main__":
#     task2()
#task 3
# def max_values(A):
#     max_result_global = np.max(A)
#     max_result_column = A.max(axis=0)
#     max_result_row = A.max(axis=1)
#     print("macierz ogolnie:\n ", A)
#     print("maksymalna wartosc globalna: ", max_result_global)
#     print("maksymalne wartosci w kolumnach: ", max_result_column)
#     print("maksymalne wartosci w wierszach: ", max_result_row)
# def task3():
#     matrix = np.random.randint(100,size = (3,3))
#     max_values(matrix)
# if __name__ == "__main__":
#     task3()
#task 4
# def task4():
#     A = np.arange(42)
#     print(A)
#     A1 = A.reshape(-1,6)
#     print("\n",A1)
#     A2 = A.reshape(7,-1)
#     print("\n",A2)
# if __name__ == "__main__":
#     task4()
#task 5