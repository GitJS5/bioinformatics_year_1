# PROGRAM PENTRU ALGORITMUL NEEDLEMANWUNSCH
import numpy as np

amount = int(input("Introduceti numarul de valori pe care vreti la introduceti in secventa\n"))
sec1 = np.random.choice(['A', 'T', 'G', 'C', '_'], amount)
sec2 = np.random.choice(['A', 'T', 'G', 'C', '_'], amount)
main = np.zeros((len(sec1) + 1, len(sec2) + 1))
nw_zeros_check = np.zeros((len(sec1), len(sec2)))
print(nw_zeros_check)
print(sec1)
print(sec2)

print("SCHEMA DE SCOR")
right = int(input("POTRIVIRE = "))
wrong = int(input("NEPOTRIVIRE = "))
gap = int(input("GAP = "))

for i in range(len(sec1)):
    for j in range(len(sec2)):
        if sec1[i] == sec2[j]:
            nw_zeros_check[i][j] = right
        else:
            nw_zeros_check[i][j] = wrong

for i in range(len(sec1) + 1):
    main[i][0] = i * gap
for j in range(len(sec2) + 1):
    main[0][j] = j * gap
for x in range(len(sec2) + 1):
    main[0][j] = j / gap


def initializare(x, y, main_nw, zeros_check):
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            main_nw[i][j] = max(main_nw[i - 1][j - 1] + zeros_check[i - 1][j - 1],
                                main_nw[i-1][j] + gap,
                                main_nw[i][j - 1] + gap)
    print(main_nw)


def backtrack(sec1, sec2, main_array, zeros_check):
    # Formatare aliniere backtracking
    aligned_1 = ""
    aligned_2 = ""

    ti = len(sec1)
    tj = len(sec2)

    while ti > 0 and tj > 0:

        if (ti > 0 and tj > 0 and main_array[ti][tj] == main_array[ti - 1][tj - 1] + zeros_check[ti - 1][
            tj - 1]):

            aligned_1 = sec1[ti - 1] + aligned_1
            aligned_2 = sec2[tj - 1] + aligned_2

            ti = ti - 1
            tj = tj - 1

        elif ti > 0 and main_array[ti][tj] == main_array[ti - 1][tj] + gap:
            aligned_1 = sec1[ti - 1] + aligned_1
            aligned_2 = "-" + aligned_2
            ti = ti - 1
        else:
            aligned_1 = "-" + aligned_1
            aligned_2 = sec2[tj - 1] + aligned_2

            tj = tj - 1

    # test
    print(aligned_1)
    print(aligned_2)


initializare(sec1, sec2, main, nw_zeros_check)
backtrack(sec1, sec2, main, nw_zeros_check)
