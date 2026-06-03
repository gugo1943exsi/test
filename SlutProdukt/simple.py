# En funktion der tjekker tal
def tjek_tal(tal):
    """
    Tjekker om tallet er negativt, nul eller positivt
    """
    if tal < 0:
        return "Negativt tal"
    elif tal == 0:
        return "Tallet er 0"
    else:
        return "Positivt tal"


# Variabel
i = -2

# For-loop
for i in range(-2, 3):
    resultat = tjek_tal(i)  # kalder funktionen
    print(f"Tallet {i}: {resultat}")