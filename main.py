def citireLista(l):
    l= []
    givenString = input("Dati lista, cu elemente separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l

def elementePrimeDinLista(l):
    '''
    Elimina nr prime din lista data
    :param l: lista cu nr intregi
    :return: returneaza lista dupa eliminarea nr prime
    '''
    rezultat = []
    for x in l:
        k = True
        if x < 2:
            k = False
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                k = False
        if k == False:
            rezultat.append(x)
        return rezultat

def MedieAritmetica(l):
    '''
    Calculeaza media aritmetica a nr din lista
    :param l: lista de nr intregi
    :return: media aritmetica
    '''
    rezultat = 0
    for x in l:
        rezultat = rezultat + x
    rezultat = rezultat // int(len(1))
    return rezultat

def main():
    l = []
    while True:
        print("1. Citirea unei liste de numere întregi. ")
        print("2. Afișarea listei după eliminarea numerelor prime din listă.")
        print("3. Se afișează dacă media aritmetică a numerelor este mai mare decât un număr n dat.")
        print("4. Afișarea listei obținută prin adăugarea după fiecare element numărul de divizori proprii ai elementului.")
        print("5. Afișarea listei obținute din lista inițială în care numerele sunt înlocuite cu un tuplu în care pe prima poziție este numărul, pe a doua poziție va fi indexul elementului din listă, iar pe a treia poziție apare numărul de apariții a numărului.")
        print("x. Iesire")

        optiune = input("Dati optiunea:  ")

        if optiune == "1":
            l= citireLista(l)
        elif optiune == "2":
            print(elementePrimeDinLista(l))
        elif optiune == "3":
            print(MedieAritmetica(l))
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")

main()