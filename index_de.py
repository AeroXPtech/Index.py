print("     ----------------------")
print("     -      Index.py      -")
print("     -    von  Techx32    -")
print("     ----------------------")

while True:
    print("\n---------------------------------")
    print("             Willkommen!         ")
    print("\n1 - Neofetch                   ")
    print("2 - Quelle                       ")
    print("3 - Github                       ")
    print("4 - Updates")
    print("---------------------------------")
    print("E - Benden                       ")
    print("---------------------------------")

    wahl = input(">>> ")

    if wahl =="1":
        print("""
        nutzer@kali
        -----------
        OS: Kali Linux
        RAM: 16GB (2GB genutzt)
        Speicher 251GB
        CPU: Intel i5
        """)

    elif wahl == "2":
        print("Quelle und Idee von Mr Robot")

    elif wahl == "3":
        print("https://github.com/AeroXPtech")

    elif wahl == "4":
        print("""
              Updates
              --------
              Neue Funktionen Hinzugefügt
              Deutsche Version Von index.py Hinzugefügt
            """)

    elif wahl == "E":
        print("Tschüss!")
        break

    else:
        print("Nicht Erlaubte Option")