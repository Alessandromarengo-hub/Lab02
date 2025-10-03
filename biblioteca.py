def carica_da_file(file_path):
    """Carica i libri dal file"""
    try:
        file = open(file_path)
    except FileNotFoundError:
        print("None")

    n_sezioni = int(file.readline())
    biblioteca = []
    for i in range(n_sezioni):
        sezione = []
        biblioteca.append(sezione)

    for line in file:
        linea = line.strip().split(",")
        libro = []
        for dato in linea:
            libro.append(dato)

        indice = int(libro[4])-1
        biblioteca[indice].append(libro)

    return(biblioteca)
    file.close()
    # TODO


def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    elenco_titoli = []
    n_sezioni = 0
    for sezione in biblioteca:
        n_sezioni = n_sezioni +1
        for libro in sezione:
            elenco_titoli.append(libro[0])
    if titolo in elenco_titoli or sezione > n_sezioni:
        return False
    else:
        try:
            file2 = open(file_path)
        except FileNotFoundError:
            return False
        stringa = titolo + "," + autore + "," + anno + "," + pagine + "," + sezione + "\n"
        file2.write(stringa)
        file2.close()
        biblioteca = carica_da_file(file_path)
        return True

    # TODO


def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    elenco_titoli = []
    for sezione in biblioteca:
        for libro in sezione:
            elenco_titoli.append(libro[0])
    if titolo in elenco_titoli:
        for sezione in biblioteca:
            for libro in sezione:
                if libro[0] == titolo:
                    print(" ".join(libro))
                    return True

    else:
        return False
    # TODO


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    elenco_titoli = []
    if sezione > (len(biblioteca)+1):
        return False
    else:
        section = biblioteca[sezione]
        for libro in section:
            elenco_titoli.append(libro[0])

        finale = sorted(elenco_titoli)
        return(sezione, finale)
    # TODO


def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

