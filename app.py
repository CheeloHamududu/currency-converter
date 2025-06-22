def main():
    # Exchange rates
    dollar_to_kwacha_rate = 23.14  # 1 USD = 24.07 Kwacha
    kwacha_to_dollar_rate = 0.043  # 1 Kwacha = 0.042 USD
    
    print("Welcome to Currency Converter")
    print("1. Convert Kwacha to Dollar")
    print("2. Convert Dollar to Kwacha")
    print("3. Exit")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            
            if choice == 3:
                print("Thank you for using Currency Converter. Goodbye!")
                break
                
            if choice == 1:
                amount = float(input("Enter amount in Kwacha: "))
                converted = amount * kwacha_to_dollar_rate
                print(f"{amount:.2f} Kwacha = ${converted:.2f}")
                
            elif choice == 2:
                amount = float(input("Enter amount in Dollar: $"))
                converted = amount * dollar_to_kwacha_rate
                print(f"${amount:.2f} = {converted:.2f} Kwacha")
                
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
                
            print("\nDo you want to make another conversion?")
            print("1. Yes")
            print("2. No")
            continue_choice = int(input("Enter your choice (1-2): "))
            if continue_choice == 2:
                print("Thank you for using Currency Converter. Goodbye!")
                break
                
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
