# Currency Converter Application

A simple command-line application to convert between Zambian Kwacha (ZMW) and US Dollar (USD).

## Features

- Convert from Kwacha to Dollar
- Convert from Dollar to Kwacha
- Current exchange rates:
  - 1 USD = 24.07 Kwacha
  - 1 Kwacha = 0.042 USD

## Requirements

- Python 3.x

## How to Use

1. Run the application:
   ```
   python app.py
   ```

2. Select an option from the menu:
   - Option 1: Convert Kwacha to Dollar
   - Option 2: Convert Dollar to Kwacha
   - Option 3: Exit the application

3. Enter the amount you want to convert when prompted.

4. View the conversion result.

5. Choose whether to make another conversion or exit.

## Example Usage

```
Welcome to Currency Converter
1. Convert Kwacha to Dollar
2. Convert Dollar to Kwacha
3. Exit
Enter your choice (1-3): 1
Enter amount in Kwacha: 1000
1000.00 Kwacha = $42.00

Do you want to make another conversion?
1. Yes
2. No
Enter your choice (1-2): 1
Enter your choice (1-3): 2
Enter amount in Dollar: $50
$50.00 = 1203.50 Kwacha

Do you want to make another conversion?
1. Yes
2. No
Enter your choice (1-2): 2
Thank you for using Currency Converter. Goodbye!
```

## Updating Exchange Rates

To update the exchange rates, modify the following variables in the `app.py` file:
- `dollar_to_kwacha_rate`: The amount of Kwacha equal to 1 USD
- `kwacha_to_dollar_rate`: The amount of USD equal to 1 Kwacha