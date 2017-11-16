import pandas as pd
# stažený .csv soubor jsem v excelu očistil o záznamy bez čísla,
# o faxi a o MD,RD a nastavení delimiteru na ','
# TODO dodělat základní vyčištění do tohoto skriptu


def numberize(linka):
    """ funkce, která vytvoří z čísla linky telefonní číslo,
    prázdné pole nechá prázdné a celá čísla zachová.
    + Odstraní přebytečné mezery."""
    linka = str(linka).strip()

    if linka is None:
        return None
    if len(linka) == 3:
        return ('+420221663' + linka)
    if len(linka) == 5:
        return ('+420281013' + linka[2:])
    if len(linka) > 5:
        return linka


# cesta k csv souboru
csv_file = '~/Documents/Python/kontakty-upravene.csv'

# načtu upravený csv soubor do dataframu
df = pd.read_csv(csv_file, header=0, delimiter=';')

# rozdělení telefonních linek do sloupců
df2 = df['telefon'].str.split(',', expand=True)

# spojení dataframů do jednoho
contacts = pd.concat([df, df2], axis=1)

# smazaní starého sloupce s telefonními linkami
contacts.drop('telefon', axis=1, inplace=True)

# počet sloupců s telefonními linkami - sloupce jmeno, email a pracoviste
NumberOfColumns = len(contacts.columns) - 3

# přejmenování sloupců
for i in range(0, NumberOfColumns):
    if i == 0:
        contacts.rename(columns={0: 'telefon'}, inplace=True)
    else:
        contacts.rename(columns={i: 'telefon' + str(i)}, inplace=True)

# přepsaní hodnot ve sloupcích z linky na telefonní čísla
for index, row in contacts.iterrows():
    for i in range(0, NumberOfColumns):
        if i == 0:
            contacts.loc[index, 'telefon'] = numberize(row['telefon'])
        else:
            contacts.loc[index, 'telefon' + str(i)] = numberize(row['telefon' + str(i)])

# zapis do csv
contacts.to_csv('kontakty-s-telefony.csv', index=False)
