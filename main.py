def verify_denum(denum):
    if denum <= 0:
        print("\n#ERROR# Impossible de mettre une valeur égale ou inférieure à 0\n")
        return False

    if denum.is_integer():
        return True

    return False


def verify_mark(mark):
    if mark > 0:
        print("\n#ERROR# Impossible de mettre une valeur inférieure à 0\n")
        return False

    return True


def get_valid_input(text):
    value = input(text)
    if not value.replace('.', '', 1).isdigit():
        return get_valid_input(text)

    return float(value)


def convert_note():
    note, denum_bef, denum_aft = (get_valid_input(text) for text in (
        "\nQuelle est cette note? ", "Sur combien est cette note? ", "Sur combien la voulez-vous? "
    ))
    result = (note * denum_aft) / denum_bef

    if result.is_integer():
        result = int(result)

    print(f"Cela donnerait donc : {result}\n")


is_running = True

while is_running:
    choix = int(input("----------MENU---------- \n 1 - Convertir une note \n 2 - Quitter \nQue voulez-vous faire? "))

    if choix == 1:
        convert_note()

    elif choix == 2:
        is_running = False

    else:
        print("#ERREUR#")
