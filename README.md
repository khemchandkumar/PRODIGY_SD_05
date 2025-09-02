# 🛒 E-commerce Tablet Product Scraper

A Python web scraper that extracts tablet product information from test e-commerce websites. This tool collects product names, prices, and ratings, then exports the data to a CSV file for further analysis.

## 📋 Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Code Structure](#code-structure)
- [Important Notes](#important-notes)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- Scrapes tablet product data from https://webscraper.io test site
- Extracts three key data points: product names, prices, and star ratings
- Robust error handling for missing or malformed data
- Automatic CSV export with organized data structure
- Clean, readable code with proper exception handling

## 🛠 Technologies Used

- **Python 3.x**
- **BeautifulSoup4** - HTML parsing and web scraping
- **Requests** - HTTP library for web requests
- **Pandas** - Data manipulation and CSV export
- **lxml** - XML and HTML parser

## 📦 Prerequisites

Before running this project, make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## 🚀 Installation

1. Clone this repository:
   ``` bash
   git clone https://github.com/khemchandkumar/web-scraping.git
   ```
   ``` bash
   cd web-scraping
   ```

2. Install the required Python packages:
   ``` bash
   pip install requests beautifulsoup4 pandas lxml
   ```

## 💻 Usage

1. Run the Python script:
   ```bash
   python web-scraping.py
   ```

2. The script will:
- Connect to the target website
- Extract tablet product data
- Save the results to a CSV file
- Display a success message

3. Find your data in the generated `tablets.csv` file

## 📊 Output

The scraper generates a CSV file with the following columns:
- **Product Name**: The name/title of the tablet
- **Price**: The listed price of the product
- **Rating**: Number of stars (1-5 rating system)

Sample output:
```
Product Name,Price,Rating
Galaxy Tab S7,299.99,4
iPad Pro 12.9,999.99,5
Surface Pro 8,849.99,4
```

## 🏗 Code Structure

```
web-scraping.py
├── Import required libraries
├── Initialize data storage lists
├── Define target URL
├── HTTP request and response handling
├── HTML parsing with BeautifulSoup
├── Data extraction loop
├── Error handling for missing elements
├── DataFrame creation and CSV export
└── Exception handling for network issues
```

## ⚠️ Important Notes

- This scraper is designed specifically for the webscraper.io test site
- The script includes error handling for missing product information
- **Always respect robots.txt** and website terms of service when scraping
- For production use, consider adding delays between requests
- Update the CSV file path in the script to match your local directory structure

## 🔧 Customization

To adapt this scraper for other websites:
1. Update the `url` variable with your target website
2. Modify the CSS selectors to match the target site's HTML structure
3. Adjust the data extraction logic as needed
4. Update error handling for site-specific requirements

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

If you have any questions or suggestions, feel free to reach out or open an issue on GitHub.

---

**Note**: This project is for educational purposes. Always ensure you have permission to scrape websites and respect their terms of service.
