import requests
import json
import pyperclip


def get_exchange_rate(currency_code):
    url = "https://api.coingecko.com/api/v3/exchange_rates"
    headers = {"accept": "application/json"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()

        # Get rates and find the requested cryptocurrency
        rates = data.get("rates", {})
        currency_info = rates.get(currency_code.lower())  # Use .lower() to match keys in the JSON response

        if currency_info:
            name = currency_info.get("name")
            unit = currency_info.get("unit")
            value = currency_info.get("value")

            # Format output and print it
            output = f"Name: {name}\nUnit: {unit}\nValue: {value}"
            print(output)

            # Copy to clipboard
            pyperclip.copy(output)
            print("Exchange rate details copied to clipboard!")
            return True  # Return True to indicate successful retrieval
        else:
            print(f"No data found for currency code: {currency_code}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False  # Return False if there was an error


# Loop to allow the user to try again if they enter an incorrect currency code
while True:
    currency_code = input("Enter the currency code to get details or 'exit' to quit: ").upper()
    if currency_code == "EXIT":
        print("Exiting the Program")
        break
    if get_exchange_rate(currency_code):
        break
