/*
Name:Eunice Mwende
Reg:CT100/G/26231/25
*/


MIN_AGE = 21
MIN_INCOME = 21000

print("--- Loan Check ---")

try:
    age = int(input("Enter age: "))
    income = int(input("Enter annual income (Shillings): "))

    if age >= MIN_AGE and income >= MIN_INCOME:
        print("\nCongratulations, you qualify for a loan.")
    else:
        print("\nUnfortunately, we are unable to offer you a loan at this time.")

except ValueError:
    print("\nError: Enter valid numbers only.")

```
