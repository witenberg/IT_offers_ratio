# Job Offer Population Ratio Calculator

This Python application fetches IT job offers from pracuj.pl website, calculates the ratio of job offers to the population of various cities in Poland, and outputs the results to a text file.

## Features

- **Job Offer Collection**: Scrapes IT job offers from a designated website.
- **City-Specific Data**: Calculates job offer counts and ratios for cities with a population greater than 10,000.
- **Remote Job Offers**: Identifies and counts remote job offers separately.
- **Data Output**: Saves results to `city_job_ratio.txt`.

## How It Works

1. **Fetching Job Offers**: The application collects job offers from the specified website using web scraping techniques.
2. **Population Data**: Reads city population data from `population.txt`, which should be prepared and included in the project directory.
   - Data in `population.txt` is sourced from the GUS report "Powierzchnia i ludność w przekroju terytorialnym w 2022 roku (07.12.2022)".
3. **Calculating and Sorting**: Computes the ratio of job offers to city population for cities with a population greater than 10,000. Results are sorted in descending order based on the ratio.
4. **Saving Results**: Outputs city-specific job offer counts, ratios, and remote job offer count to `city_job_ratio.txt`.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Usage

1. Ensure Python and required libraries are installed.
2. Make sure there is a ready-made population.txt file in the application folder, or prepare your own file in the format 'city_name population'.
4. Run the script `main.py`.
5. View the sorted results in `city_job_ratio.txt` for city-specific job offer ratios and counts.

## Example Population File Format (`population.txt`)

