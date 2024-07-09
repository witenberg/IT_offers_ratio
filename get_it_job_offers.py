import requests
from bs4 import BeautifulSoup

city_job_count = {}  # Słownik przechowujący liczbę ofert dla każdego miasta


def get_it_job_offers():
    # URL bazowy do wyszukiwania ofert pracy w IT na OLX
    base_url = "https://www.olx.pl/praca/informatyka/"

    # Inicjalizacja zmiennych
    page = 1
    total_offers = 0  # Całkowita liczba znalezionych ofert
    seen_offers = set()  # Zbiór przechowujący unikalne URL-e ofert
    no_new_offers = 0  # Licznik stron bez nowych ofert, aby przerwać pętlę

    while True:
        # Tworzenie pełnego URL-a strony, uwzględniającego numer strony (jeśli większy niż 1)
        url = f"{base_url}?page={page}" if page > 1 else base_url

        # Pobieranie strony HTML z OLX
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Błąd podczas pobierania danych: {response.status_code}")
            break

        # Analiza HTML przy użyciu BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        job_offers = soup.find_all('div', class_='css-1sw7q4x')

        if not job_offers:
            break  # Przerwanie pętli, jeśli nie ma więcej ofert na stronie

        new_offers_found = False

        for offer in job_offers:
            offer_link = offer.find('a', href=True)
            if offer_link:
                offer_url = offer_link['href']
                if offer_url not in seen_offers:
                    new_offers_found = True
                    total_offers += 1
                    seen_offers.add(offer_url)

                    city_tag = offer.find('span', class_='css-d5w927')
                    if city_tag:
                        city = city_tag.text.strip().split(',')[0]
                        if city in city_job_count:
                            city_job_count[city] += 1
                        else:
                            city_job_count[city] = 1

        if not new_offers_found:
            no_new_offers += 1
        else:
            no_new_offers = 0

        if no_new_offers >= 2:
            break  # Przerwanie pętli, jeśli dwie kolejne strony nie mają nowych ofert

        page += 1  # Przejście do następnej strony



