# Google Restaurant Data Scraper

## Project Overview
This project is a Python-based web scraping tool that collects restaurant data from Google search results for a specified region. The script uses Selenium and BeautifulSoup to extract restaurant details such as names, ratings, addresses, and phone numbers and stores them in a CSV file.

## Features
- Scrapes restaurant details from Google search results.
- Extracted details include:
  - Restaurant Name
  - Rating
  - Address
  - Phone Number
- Saves the data into a structured CSV file.

## Technologies Used
- Python
- Selenium
- BeautifulSoup
- pandas

## Installation and Setup

### Prerequisites
1. **Python 3.9+**
2. Install the required Python libraries:
   ```bash
   pip install selenium beautifulsoup4 pandas
   ```
3. Download the ChromeDriver that matches your version of Google Chrome:
   - [ChromeDriver - WebDriver for Chrome](https://sites.google.com/chromium.org/driver/)
   - Add ChromeDriver to your system PATH or specify the path in the script.

### Cloning the Repository
Clone the repository from GitHub:
```bash
git clone https://github.com/<your-username>/google-restaurant-scraper.git
cd google-restaurant-scraper
```

### Running the Script
1. Open the terminal or command prompt.
2. Run the script:
   ```bash
   python app.py
   ```
3. The scraped data will be saved in a file named `restaurants.csv` in the project directory.

## How It Works
1. The script launches a Chrome browser instance using Selenium.
2. It searches Google for restaurants in the specified region (e.g., "Downtown Toronto").
3. The page content is parsed using BeautifulSoup to extract relevant restaurant details.
4. Data is stored in a structured format using pandas and saved to a CSV file.

## File Structure
```
.
├── app.py                # Main script for scraping
├── requirements.txt      # Required Python packages
├── restaurants.csv       # Sample output file
└── README.md             # Project documentation
```

## Example Output
| Name                | Rating | Address             | Phone        |
|---------------------|--------|---------------------|--------------|
| Restaurant A        | 4.5    | 123 Main St         | (123) 456-7890 |
| Restaurant B        | 4.2    | 456 Elm St          | (987) 654-3210 |

## Notes
- Ensure you have the correct version of ChromeDriver for your Chrome browser.
- Avoid running the scraper too frequently to comply with Google's Terms of Service.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
- Tushar Lahekar  
  GitHub: [tusharlahekar](https://github.com/tusharlahekar)
