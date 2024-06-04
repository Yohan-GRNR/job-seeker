# Job Listings Scraper using SerpAPI

This repository contains a Python script to scrape job listings from Google Jobs using the SerpAPI. The script fetches job listings for a specified search term and location, and saves the results in a CSV file.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/Yohan-GRNR/Job-Seeker.git
    cd Job-Seeker
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Setup your SerpAPI key:**
    - Obtain an API key from [SerpAPI](https://serpapi.com/).
    - Save the API key in a file located at `../API keys/serpai.txt`.

## Usage

1. **Modify the search parameters:**
    - Edit the `search_term`, `search_location`, and `search_radius` variables in the script to suit your needs.
    - Example:

        ```python
        search_term = "data analyst"
        search_location = "Geneva, Switzerland"
        search_radius = 20
        ```

2. **Run the script:**

    ```sh
    python scrape_jobs.py
    ```

3. **View the results:**
    - The results are saved in a CSV file named `DB_data-analyst.csv`.

## Features

- **Pagination:** Fetches multiple pages of results.
- **Error Handling:** Stops fetching if there are no more results.
- **Data Normalization:** Normalizes nested JSON data.
- **Data Persistence:** Saves results to a CSV file, appending new data and removing duplicates.

## Contributing

Contributions are welcome! Please create a pull request or open an issue for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Note:** Ensure you comply with SerpAPI's terms of use and respect the scraping rules of the websites you are accessing.

For any questions or issues, feel free to open an issue in this repository. Happy scraping !