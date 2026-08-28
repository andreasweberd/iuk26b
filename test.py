# Kommentar
def essen(snack):
    print(f'Auf dem Schulweg esse ich : {snack}')
    print("lol, ich habe Hunger und esse mein Käsebrot auf dem Schulweg.")


# Kommentar
if __name__ == "__main__":
    print("Schulmorgen beginnt.")
    print("Ich ziehe mich an und gehe los.")

    mein_brot = "Käsebrot"
    x = 0
    while x < 10:
        x += 1
        essen(mein_brot)
        print("OHHH SO GUT! Ich liebe mein Käsebrot.")
    mein_brot = "Schokoriegel"
    essen(mein_brot)
    print("In der Klasse hinsetzen.")
