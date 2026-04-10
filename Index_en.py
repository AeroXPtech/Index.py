print("     ----------------------")
print("     -      Index.py      -")
print("     -     by Techx32     -")
print("     ----------------------")

while True:
    print("\n---------------------------------")
    print("             Welcome!            ")
    print("\n1 - Neofetch                   ")
    print("2 - Source                       ")
    print("3 - Github                       ")
    print("4 - Updates")
    print("---------------------------------")
    print("E - Exit                         ")
    print("---------------------------------")

    wahl = input(">>> ")

    if wahl =="1":
        print("""
        user@kali
        ---------
        OS: Kali Linux
        RAM: 16GB (2GB used)
        Storage 251GB
        CPU: Intel i5
        """)

    elif wahl == "2":
        print("Source or Inspo By Mr Robot")

    elif wahl == "3":
        print("https://github.com/AeroXPtech")

    elif wahl == "4":
        print("""
              Updates
              --------
              Added More Features
              Added German Index.py version
            """)

    elif wahl == "E":
        print("Good Bye!")
        break

    else:
        print("INVALID OPTION")
