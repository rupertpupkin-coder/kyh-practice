from uppgift36.pwstrength import compute_strength

if __name__ == '__main__':

    while True:
        password = input("Ange lösenord: ")
        res, passed = compute_strength(password)
        if passed:
            if res == 0:
                print(f"Antal poäng: {res}. Svagt lösenord men godkänt.")
            if res == 1:
                print(f"Antal poäng: {res} Bättre kan du.")
            if res > 1:
                print(f" Antal poäng: {res}. Bra lösenord")
            break
        print("Ogiltigt lösenord! Försök igen :)")




