import requests
from bs4 import BeautifulSoup
from plyer import notification
import time
import os


def get_price(url):
    """
    The get_price function, using webscraping, returns the price of the product.

    Website used: carturesti
    """

    # Response sends a request to the entered URL and
    # stores the server's response
    response = requests.get(url)

    # Soup helps us navigate HTML data in an easy and organized way
    soup = BeautifulSoup(response.text, 'html.parser')

    # Price_element stores the location of the price in the website's HTML (carturesti)
    price_element = soup.find('span', {'class': 'pret'})

    # If price_element exists, return the price
    price_text = price_element.text.strip() if price_element else None

    # Convert the first two characters of the price to float
    price_text = float(price_text[:2]) if price_text else None

    return price_text


def notify_price_change(product_url):
    """
    The notify_price_change function sends a notification when the price of the entered product (product_url) changes.
    """

    previous_price = None

    # Continuously check the price at regular time intervals
    while True:

        # Define the current price using the get_price function above
        current_price = get_price(product_url)

        # If the get_price function returns None, then we don't have a valid price
        # and move on to the next iteration
        if current_price is not None:
            # Check if we have a previous price and if the current price
            # differs from the previous price. If this is true, then
            # the price has changed and continue with the notification.
            if previous_price is not None and current_price != previous_price:
                # Display a desktop notification
                notification.notify(
                    title='Price changed!',
                    message=f'The new price is {current_price:.2f} RON!',
                )

                # Current time
                current_time = time.strftime("%Y-%m-%d %H:%M:%S")

                # Add the information to a CSV file
                with open('price_history.csv', 'a') as csv_file:
                    csv_file.write(f'{current_time},{current_price:.2f},{product_url}\n')

            # Update the new price
            previous_price = current_price

        # Executed if get_price doesn't return any price
        else:
            print("Unable to retrieve a valid price.")

        # Check the price at certain intervals
        # (you can adjust the interval as needed)
        time.sleep(3600)  # Wait for 1 hour


if __name__ == "__main__":
    product_url = "https://carturesti.ro/carte/fahrenheit-451-2347593222?p=16"

    # Check if the CSV file exists, and if not, create it
    if not os.path.isfile('price_history.csv'):
        with open('price_history.csv', 'w') as csv_file:
            csv_file.write('Timestamp,Price,Product_URL\n')

    notify_price_change(product_url)
