print(" ----------------------")
print(" -      Index.py      -")
print(" -    door Techx32    -")
print(" ----------------------")

while True:
    print("\n---------------------------------")
    print(" Welkom! ")
    print("\n1 - Neofetch ")
    print("2 - Bron ")
    print("3 - Github ")
    print("4 - Updates")
    print("---------------------------------")
    print("E - Afsluiten ")
    print("---------------------------------")

    wahl = input(">>> ")

    if wahl =="1":
        print("""
        gebruiker@kali
        --------------
        OS: Kali Linux
        RAM: 16GB (2GB gebruikt)
        Opslag 251GB
        CPU: Intel i5
        """)

    elif wahl == "2":
        print("Source or Inspo By Mr Robot")

    elif wahl == "3":
        print("https://github.com/AeroXPtech")

    elif wahl == "4":
        print("""
                Updates
                ------
                Meer functies toegevoegd
                Duitse versie van Index.py toegevoegd
                Nederlandse versie van Index.py toegevoegd
            """)

    elif wahl == "E":
        print("Tot ziens!")
        break

    else:
        print("Ongeldige optie")