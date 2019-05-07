import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
"""
Skript vytvářející seznam semínek se stránek UDHPSHudhpsh.cz
pro tematické sklizeň voleb do Evropského parlamentu 2019.
Skript prochází tabulky subjektů, kteří kandidují do voleb,
extrahuje z něj url na single page s financováním a na transparentní účet.
Vytvoří i url na webové stránky subjektu odseknutím cesty z url single page.
"""
# seznam url, ze kterých se budou semínka stahovat
urls = {
    'political_parties': 'https://registrace.udhpsh.cz/seznam/ep/2019ep',
    'individuals': 'https://registrace.udhpsh.cz/seznam/tofo/2019ep',
    'legal_entities': 'https://registrace.udhpsh.cz/seznam/topo/2019ep'
}

# otevře/vytvoří soubor seeds.txt, kam semínka bude zapisovat
with open('seeds.txt', 'w') as f:
    # postupně projde každé url
    for url in urls:
        try:
            # stáhne obsah stránky
            r = requests.get(urls[url])
        except Exception as err:
            print(f'Request error occurred: {err}')

        soup = BeautifulSoup(r.text, 'lxml')

        # cyklus projde tabulku po řádcích
        for row in soup.table.find_all('tr'):
            # uložím sloupce v jednom řádku do proměnné
            col = row.find_all('td')

            try:
                # url jsou vždy poslední dvě pole v tabulce
                # v posledním sloupci je link na stránku s financemi
                # url parser je využit k odseknutí cesty pro získání homepage
                finances = urlparse(col[-1].find('a').attrs['href'])
                domain = f'{finances.scheme}://{finances.netloc}'

                # zapíše do souboru odkaz na celé stránky subjektu
                f.write(finances.geturl() + '\n')

                # pokud subjekt uvedl adresu na single page zapíše také
                if finances.geturl() != domain:
                    f.write(domain + '\n')

            except Exception:
                # pokud není v tabulce uvedena url, pak sloupec přeskočím
                pass
            try:
                # odkaz na transparentní účet je druhý sloupec od konce
                transparent_acc = col[-2].find('a').attrs['href']
                f.write(transparent_acc + '\n')

            except Exception:
                # pokud není v tabulce uvedena url, pak sloupec přeskočím
                pass
