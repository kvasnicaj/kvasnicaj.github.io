from bs4 import BeautifulSoup
import requests
import csv

# vytvoření prázdného csv souboru pro zápis
csv_file = open('kontakty.csv', 'w')
csv_writer = csv.writer(csv_file, delimiter=';')

# vytvoření záhlaví v csv souboru
csv_writer.writerow(['jmeno', 'telefon', 'email', 'pracoviste'])

main_url = 'https://goo.gl/823dcr'
main_r = requests.get(main_url).text

main_soup = BeautifulSoup(main_r, 'lxml')

navigation = main_soup.find(
    id='parent-fieldname-text-9d56ac4b-d376-42fc-b079-21335cdc5375')

# cyklus prochází seznam url stažených z úvodné stránky kontaktů,
# -2 –> poslední dva odkazy jsou mimo seznam kontaktů
for url in navigation.find_all('a')[:-2]:

    # stažení html stránky s kontakty
    r = requests.get(url.attrs['href']).text
    soup = BeautifulSoup(r, 'lxml')

    # tabulka s kontaktními údaji
    table = soup.find('table', class_='listing')

    # procházení tabulky a uložení řádků do csv souboru
    for row in table.find_all('tr')[1:]:
        col = row.find_all('td')
        csv_writer.writerow([col[0].text, col[1].text,
                             col[2].text, col[3].text])

# zavření hotového csv souboru
csv_file.close()
