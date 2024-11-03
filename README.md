# python_projects
Description:
This cryptocurrency converter program allows users to input a fiat currency or cryptocurrency unit (e.g., USD, EUR, ETH) and return its current value compared to Bitcoin (BTC). It fetches real-time exchange rate data from the CoinGecko public API, which provides accurate cryptocurrency market data, including rates for hundreds of fiat and crypto units relative to Bitcoin.

How to Use:
Here’s a detailed step-by-step guide on running and using a Python program that allows users to input a currency code and retrieve its value compared to Bitcoin using a public API, specifically CoinGecko’s free API.
Step 1: Set Up Your Environment
1.	Install Required Packages:
2.	Sign Up for API Access (Optional):
Step 2: Write the Program
Step 3: Run the Program
To run the program:
1.	Save the Script:
2.	Execute the Program:
3.	Enter Currency Code:
Step 4: Understanding the Output

Technical Details:
1.	Function Definition:
Function get_exchange_rate: Encapsulating the code that fetches and prints ex-change rate information into a function (get_exchange_rate) makes the program more modular and reusable. Now, you can call this function whenever you need to get an exchange rate, making the code easier to maintain and test.
2.	Error Handling:
The try-except block with raise_for_status() catches HTTP errors and handles cases where the API request might fail due to connectivity issues or invalid URLs.
Return False on failure: By returning False if an exception occurs, the function can signal that an error occurred, allowing the main program to handle this case (e.g., by letting the user try again).
3.	Loop for User Input:
The while loop allows users to input multiple currency codes and exit when they are done. This design allows users to try different codes without restarting the program.
Case Insensitivity: Using .lower() on the currency_code lookup and .upper() on the user input ensures the currency code lookup is case-insensitive, which reduc-es the chance of user error.
4.	Improved Readability:
Comments: Added comments clarify each section's purpose, helping future devel-opers (or yourself) understand the code at a glance.
Code Structure: Splitting functionality into smaller, purpose-specific sections (fetching data, handling errors, looping input) improves readability.
