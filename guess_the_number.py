import random

print("Velkommen til 'Gjett et tall'!")
print("Jeg har valgt et tall mellom 1 og 100. Klarer du å gjette det?")
secret_number = random.randint(1, 100)  # Velger et tilfeldig tall
attempts = 0  # Teller antall forsøk

while True:
    try:
        guess = int(input("Skriv inn ditt gjett: "))  # Brukeren gjetter et tall
        attempts += 1

        if guess < secret_number:
            print("For lavt! Prøv igjen.")
        elif guess > secret_number:
            print("For høyt! Prøv igjen.")
        else:
            print(f"Gratulerer! Du gjettet riktig på {attempts} forsøk.")
            break  # Avslutter løkken når tallet er gjettet
    except ValueError:
        print("Vennligst skriv inn et gyldig tall.")
