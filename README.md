# Price Tracker

This Python application tracks the price of a specific product on a website (in this case, carturesti.ro) and notifies the user when the price changes. It utilizes web scraping techniques to retrieve the current price of the product and compares it to the previous price. If a change is detected, the application sends a desktop notification with the updated price. Additionally, it maintains a record of price changes in a CSV file for historical reference.

## Development Environment

This application was developed using Python.

## Dependencies

Before running the application, ensure you have the following libraries installed:

- Requests
- BeautifulSoup4
- Plyer

You can install these dependencies using the following command:

```bash
pip install requests
```
```bash
pip install beautifulsoup4
```
```bash
pip install plyer
```

## Usage

To use the application effectively, follow these steps:

1. Clone this repository to your local machine.
2. Ensure Python is installed on your system.
3. Install the required dependencies using the provided command.
4. Open the script in your preferred Python IDE.
5. Inspect the website of the product you want to track and identify the HTML element containing the price information.
6. Modify the script to target the specific HTML element by replacing the `product_url` variable with the URL of the product and adjusting the HTML element targeting code accordingly.
7. Run the script.
8. The application will continuously monitor the price of the product and notify you whenever it changes.
9. You can view the price change history in the `price_history.csv` file.
