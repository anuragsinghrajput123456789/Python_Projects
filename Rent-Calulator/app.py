import pandas as pd

# --- Taking inputs from user ---
rent = int(input("Enter your hostel/flat rent: "))
food = int(input("Enter your food expense: "))
transport = int(input("Enter your transport expense: "))
electricity = int(input("Enter your electricity units consumed: "))
charge_per_unit = int(input("Enter charge per unit of electricity: "))
other = int(input("Enter your other expenses: "))
persons = int(input("Enter number of persons sharing the expenses: "))

# --- Calculations ---
total_bill = electricity * charge_per_unit
total_expense = rent + foodsad + transport + total_bill + other
expense_per_person = total_expense / persons

# --- Display results ---
print("\n--- Monthly Expense Summary ---")
print(f"Total Electricity Bill: ₹{total_bill}")
print(f"Total Monthly Expense: ₹{total_expense}")
print(f"Expense Per Person: ₹{expense_per_person:.2f}")

# --- Ask if user wants Excel report ---
save_excel = (
    input("\nDo you want to save the expense report as an Excel file? (yes/no): ")
    .strip()
    .lower()
)

if save_excel == "yes":
    data = {
        "Expense Type": [
            "Rent",
            "Food",
            "Transport",
            "Electricity Bill",
            "Other",
            "Total",
            "Per Person",
        ],
        "Amount (₹)": [
            rent,
            food,
            transport,
            total_bill,
            other,
            total_expense,
            expense_per_person,
        ],
    }

    df = pd.DataFrame(data)
    file_name = "Monthly_Expense_Summary.xlsx"
    df.to_excel(file_name, index=False)
    print(
        f"\n✅ Excel file '{file_name}' created successfully in your current directory!"
    )
else:
    print("\n❌ Excel file not created.")


import pandas as pd
df = pd.read_excel('Monthly_Expense_Summary.xlsx')
print(df)