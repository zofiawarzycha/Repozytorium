'''
Napisać program, który dla wprowadzonego przez użytkownika ciągu liczb rzeczywistych wyznacza ich
średnią arytmetyczną. Wprowadzanie ciągu kończy się poprzez wprowadzenie napisu ’end’. Program
powinien raportować błąd, jeśli ’end’ jest pierwszą podaną wartością. Przykładowo, dla wejścia:
1
-22
8
-3.5
13
end
Poprawną odpowiedzią jest -0.7.
'''

def oblicz_srednia():
    liczby = []
    print("Podaj liczby rzeczywiste (wprowadź 'end', aby zakończyć):")

    while True:
        wejscie = input()

        if wejscie == 'end':
            if not liczby:
                print("Błąd: 'end' zostało podane jako pierwsza wartość.")
                return
            break

        try:
            liczba = float(wejscie)
            liczby.append(liczba)
        except ValueError:
            print("Niepoprawna wartość. Podaj liczbę rzeczywistą lub 'end'.")

        if liczby:
            srednia = sum(liczby) / len(liczby)
            print(f"Średnia arytmetyczna: {srednia}.")
        else:
            print("Brak liczb do obliczenia średniej.")

oblicz_srednia()


