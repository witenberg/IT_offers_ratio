from get_it_job_offers import get_it_job_offers, city_job_count

def calculate_job_population_ratio():
    get_it_job_offers()  # Uruchamiamy zbieranie ofert pracy

    # Odczytanie populacji miast z pliku populations.txt
    population_file = "population.txt"
    city_population = {}
    with open(population_file, 'r', encoding='utf-8') as pop_file:
        for line in pop_file:
            parts = line.strip().split()
            if len(parts) >= 2:
                city = " ".join(parts[:-1])
                population = int(parts[-1])
                city_population[city] = population

    # Obliczenie współczynników ilości ofert pracy na ilość mieszkańców
    city_job_ratio = {}
    for city, job_count in city_job_count.items():
        if city in city_population and city_population[city] >= 10000:
            population = city_population[city]
            ratio = (job_count / population) * 10000
            city_job_ratio[city] = ratio

    # Sortowanie miast malejąco po współczynniku
    sorted_cities_ratio = sorted(city_job_ratio.items(), key=lambda x: x[1], reverse=True)

    # Zapis wyników do pliku tekstowego
    output_file = "city_job_ratio.txt"
    with open(output_file, 'w', encoding='utf-8') as file:
        remote_job_count = city_job_count.get("Zdalnie", 0)
        file.write(f"Liczba ofert pracy zdalnej: {remote_job_count}\n")
        file.write("\nWspółczynniki ilości ofert pracy na 10 tys. "
                   "mieszkańców dla miast z ilością mieszkańców większą, niż 10 tys. mieszkańców:\n\n")
        for city, ratio in sorted_cities_ratio:
            file.write(f"{city} - {ratio:.2f}\n")

    print(f"Wyniki zapisane do pliku: {output_file}")

