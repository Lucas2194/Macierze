import numpy as np
choice = 'c'
while True:
    # Pytamy użytkownika o wymiary macierzy
    if choice == 'c':
        nA = int(input("Podaj ilość wierszy macierzy A: "))
        mA = int(input("Podaj ilość kolumn macierzy A: "))
        nB = int(input("Podaj ilość wierszy macierzy B: "))
        mB = int(input("Podaj ilość kolumn macierzy B: "))

        # Wypełniamy macierz A
        print("Podaj elementy macierzy A:")
        A = np.zeros((nA, mA))
        for i in range(nA):
            for j in range(mA):
                A[i][j] = float(input())

        # Wypełniamy macierz B
        print("Podaj elementy macierzy B:")
        B = np.zeros((nB, mB))
        for i in range(nB):
            for j in range(mB):
                B[i][j] = float(input())

    # Wyświetlamy możliwe operacje
    print("Co chcesz zrobić z tymi macierzami?")
    print("1. Dodaj macierze")
    print("2. Odejmij macierze")
    print("3. Pomnóż macierze")
    print("4. Transponuj macierz A")
    print("5. Transponuj macierz B")
    print("6. Wyjdź z programu")

    # Pobieramy wybór użytkownika
    choice = int(input("Wybierz opcję: "))

    # Wykonujemy wybraną operację
    if choice == 1:
        # Dodajemy macierze
        if A.shape == B.shape:
            result = A + B
            print("Wynik dodawania macierzy:")
            print(result)
        else:
            print("Nie można dodać macierzy o różnych wymiarach")
    elif choice == 2:
        # Odejmujemy macierze
        if A.shape == B.shape:
            result = A - B
            print("Wynik odejmowania macierzy:")
            print(result)
        else:
            print("Nie można odjąć macierzy o różnych wymiarach")
    elif choice == 3:
        # Mnożymy macierze
        if mA == nB:
            result = np.dot(A, B)
            print("Wynik mnożenia macierzy:")
            print(result)
        else:
            print("Nie można pomnożyć tych macierzy")
    elif choice == 4:
        # Transponujemy macierz A
        result = np.transpose(A)
        print("Transponowana macierz A:")
        print(result)
    elif choice == 5:
        # Transponujemy macierz B
        result = np.transpose(B)
        print("Transponowana macierz B:")
        print(result)
    elif choice == 6:
        break
    else:
        print("Nieprawidłowa opcja")

    # Pytamy użytkownika, co chce teraz zrobić
    while True:
        next_choice = input("Co chcesz teraz zrobić? [c]ontinue, [n]ew matrix, [q]uit: ")
        if next_choice == "c":
            choice == 'new'
            break
        elif next_choice == "n":
            choice == 'c'
            break
        elif next_choice == "q":
            exit()
        else:
            print("Nieprawidłowa opcja")