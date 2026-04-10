print("------------------")
print("     Index.py     ")
print("    by techx32    ")
print("------------------")

while True:
    print("\n1 - Fake Neofetch")
    print("2 - Github")
    print("3 - Infos")
    print("4 - Exit")

    choice = input("You Choose: ")

    if choice == "1":
        print("""
        user@kali
        ---------
        OS: Kali Linux
        RAM: 8GB (2GB used)
        Storage: 251GB
        CPU: Intel i5
        """)

    elif choice == "2":
        print("\nhttps://github.com/AeroXPtech")

    elif choice == "3":
        print("\nNew Features Soon")

    elif choice == "4":
        print("\nGood Bye!")
        break

    else:
        print("\nInvalid choice!")
