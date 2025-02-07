import os
import webbrowser
import platform

def main():
    # Kitörli a képernyőt mielőtt elindulna a program
    if platform.system == "windows":
        os.system("cls")
    else:
        os.system("clear")

    # Menu
    print("Üdvözlöm, ma mit szeretne számolni?\n")
    print("-----------------------------------")
    print("[1] Dolgozat százalék")
    print("[2] Számológép")
    print("[3] E-Kréta")
    print("[4] Notesz")
    print("[5] Kilépés")
    print("-----------------------------------")
    # Megadhatod választásod
    x = input("~ Add meg a választásod: ")
    match x:
        case "1":
            # Számítások ._.
            maxp = float(input("\nA dolgozat max pontszáma: "))
            elert = float(input("\nAz elért pontszám: "))
            szamolas = float(elert / maxp * 100)
            print(f"\nA dolgozat {szamolas}%-os lett\n")
            if szamolas >= 91:
                print("A dolgozat 5-ös lett.")
            elif szamolas >= 78:
                print("A dolgozat 4-es lett.")
            elif szamolas >= 65:
                print("A dolgozat 3-as lett.")
            elif szamolas >= 40:
                print("A dolgozat 2-es lett.")
            else:
                print("A dolgozat 1-es lett.")
            input("\nNyomjon egy ENTER gombot, hogy vissza lépjen a menübe.")
            main()
        case "2":
            print("")
            elso = float(input("Add meg az első számot: \n"))
            masodik = float(input("Add meg a második számot: \n"))
            muvelet = input("Add meg a műveletet: \n")
            match muvelet:
                case "+":
                    print(f"-----------------------------------\nAz eredmény: {elso + masodik}")
                    input("\nNyomjon egy ENTER gombot, hogy vissza lépjen a menübe.")
                    main()
                    
                case "-":
                    print(f"-----------------------------------\nAz eredmény: {elso - masodik}")
                    input("\nNyomjon egy ENTER gombot, hogy vissza lépjen a menübe.")
                    main()
                
                case "*":
                    print(f"-----------------------------------\nAz eredmény: {elso * masodik}")
                    input("\nNyomjon egy ENTER gombot, hogy vissza lépjen a menübe.")
                    main()   

                case "/":
                    print(f"-----------------------------------\nAz eredmény: {elso / masodik}")
                    input("\nNyomjon egy ENTER gombot, hogy vissza lépjen a menübe.")
                    main()    

                case _:
                    main()          

        case "3":
            webbrowser.open("https://www.e-kreta.hu/")
            main()
        case "4":
            lista = input("\nMit szeretne jegyzetelni a noteszbe?: ")
            print("-----------------------------------")
            nev = input("A fájl neve amibe elszeretné menteni: ")
            with open(f"{nev}.txt", "w") as f:
                f.write(lista + "\n")
                print("\nFigyelmeztetés: Be kell zárnia a segédet, hogy megtudja nézni a tartalmát a szövegnek.")
                input("\nNyomjon egy ENTER gombot, hogy vissza lépjen a menübe.")
                main()               
        case "5":
            exit
        case _:
            main()

if __name__ == "__main__":
    main()