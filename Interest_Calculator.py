from datetime import datetime
import time

def loading():
    print("\n⏳ Processing", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")

# ============================================================
# PERSONAL FINANCE MANAGEMENT SYSTEM
# ============================================================
def header():
    print("\n" + "=" * 70)
    print("💰 PERSONAL FINANCE MANAGEMENT SYSTEM 💰")
    print("📊 Plan Smart • Save Smart • Grow Smart")
    print("=" * 70)
    print(f"📅 Date & Time : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print("🔖 Version     : v1.1")
    print("=" * 70)

def get_float(message):
    while True:
        try:
            value = float(input(message))
            if value < 0:
                print("Please enter a positive value.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# ============================================================
# INTEREST CALCULATORS
# ============================================================

def simple_interest():
    print("\n--- SIMPLE INTEREST CALCULATOR ---")

    principal = get_float("Principal Amount (₹): ")
    rate = get_float("Interest Rate (%): ")
    years = get_float("Time (Years): ")

    interest = (principal * rate * years) / 100
    total = principal + interest

    loading()
    print("\nRESULT")
    print("-" * 50)
    print(f"Principal Amount : ₹{principal:,.2f}")
    print(f"Interest Earned  : ₹{interest:,.2f}")
    print(f"Final Amount     : ₹{total:,.2f}")
    print("-" * 50)


def compound_interest():
    print("\n--- COMPOUND INTEREST CALCULATOR ---")

    principal = get_float("Principal Amount (₹): ")
    rate = get_float("Interest Rate (%): ")
    years = get_float("Time (Years): ")

    amount = principal * ((1 + rate / 100) ** years)
    interest = amount - principal

    loading()
    print("\nRESULT")
    print("-" * 50)
    print(f"Principal Amount : ₹{principal:,.2f}")
    print(f"Compound Interest: ₹{interest:,.2f}")
    print(f"Final Amount     : ₹{amount:,.2f}")
    print("-" * 50)


def fd_calculator():
    print("\n--- FIXED DEPOSIT CALCULATOR ---")

    principal = get_float("FD Amount (₹): ")
    rate = get_float("Interest Rate (%): ")
    years = get_float("Duration (Years): ")

    maturity = principal * ((1 + rate / 100) ** years)

    loading()
    print("\nFD SUMMARY")
    print("-" * 50)
    print(f"Deposit Amount : ₹{principal:,.2f}")
    print(f"Maturity Value : ₹{maturity:,.2f}")
    print(f"Interest Earned: ₹{maturity-principal:,.2f}")
    print("-" * 50)


def emi_calculator():
    print("\n--- EMI CALCULATOR ---")

    principal = get_float("Loan Amount (₹): ")
    annual_rate = get_float("Interest Rate (%): ")
    years = int(get_float("Loan Tenure (Years): "))

    monthly_rate = annual_rate / 1200
    months = years * 12

    emi = (
        principal
        * monthly_rate
        * ((1 + monthly_rate) ** months)
    ) / (((1 + monthly_rate) ** months) - 1)

    total_payment = emi * months
    interest = total_payment - principal

    loading()
    print("\nLOAN SUMMARY")
    print("-" * 50)
    print(f"Loan Amount    : ₹{principal:,.2f}")
    print(f"Monthly EMI    : ₹{emi:,.2f}")
    print(f"Total Interest : ₹{interest:,.2f}")
    print(f"Total Payment  : ₹{total_payment:,.2f}")
    print("-" * 50)


def sip_calculator():
    print("\n--- SIP CALCULATOR ---")

    monthly = get_float("Monthly Investment (₹): ")
    annual_return = get_float("Expected Return (%): ")
    years = int(get_float("Investment Period (Years): "))

    rate = annual_return / (12 * 100)
    months = years * 12

    future_value = monthly * ((((1 + rate) ** months) - 1) / rate) * (1 + rate)

    invested = monthly * months
    gain = future_value - invested

    loading()
    print("\nSIP SUMMARY")
    print("-" * 50)
    print(f"Total Invested : ₹{invested:,.2f}")
    print(f"Expected Gain  : ₹{gain:,.2f}")
    print(f"Maturity Value : ₹{future_value:,.2f}")
    print("-" * 50)


def interest_menu():
    while True:
        print("\n===== INTEREST & INVESTMENT CALCULATORS =====")
        print("1. Simple Interest")
        print("2. Compound Interest")
        print("3. Fixed Deposit (FD)")
        print("4. Loan EMI")
        print("5. SIP Calculator")
        print("6. Back")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            simple_interest()
        elif choice == "2":
            compound_interest()
        elif choice == "3":
            fd_calculator()
        elif choice == "4":
            emi_calculator()
        elif choice == "5":
            sip_calculator()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


# ============================================================
# BUDGET ANALYSIS
# ============================================================

def budget_analysis():
    print("\n--- BUDGET ANALYSIS ---")

    income = get_float("Monthly Income (₹): ")
    expenses = get_float("Monthly Expenses (₹): ")

    savings = income - expenses
    savings_percent = (savings / income) * 100

    loading()
    print("\nBUDGET REPORT")
    print("-" * 50)
    print(f"Monthly Income    : ₹{income:,.2f}")
    print(f"Monthly Expenses  : ₹{expenses:,.2f}")
    print(f"Monthly Savings   : ₹{savings:,.2f}")
    print(f"Savings Percentage: {savings_percent:.2f}%")

    if savings_percent >= 30:
        print("Status            : Excellent")
    elif savings_percent >= 15:
        print("Status            : Good")
    else:
        print("Status            : Needs Improvement")

    print("-" * 50)


# ============================================================
# BUSINESS CALCULATORS
# ============================================================

def profit_loss():
    print("\n--- PROFIT / LOSS CALCULATOR ---")

    cost = get_float("Cost Price (₹): ")
    selling = get_float("Selling Price (₹): ")

    difference = selling - cost

    loading()
    print("\nBUSINESS REPORT")
    print("-" * 50)

    if difference > 0:
        percentage = (difference / cost) * 100
        print(f"Profit Amount     : ₹{difference:,.2f}")
        print(f"Profit Percentage : {percentage:.2f}%")

    elif difference < 0:
        percentage = (abs(difference) / cost) * 100
        print(f"Loss Amount       : ₹{abs(difference):,.2f}")
        print(f"Loss Percentage   : {percentage:.2f}%")

    else:
        print("No Profit No Loss")

    print("-" * 50)


def discount_calculator():
    print("\n--- DISCOUNT CALCULATOR ---")

    price = get_float("Original Price (₹): ")
    discount = get_float("Discount Percentage (%): ")

    saved = (price * discount) / 100
    final_price = price - saved

    loading()
    print("\nDISCOUNT REPORT")
    print("-" * 50)
    print(f"Original Price : ₹{price:,.2f}")
    print(f"Discount Saved : ₹{saved:,.2f}")
    print(f"Final Price    : ₹{final_price:,.2f}")
    print("-" * 50)


# ============================================================
# SAVINGS GOAL
# ============================================================

def savings_goal():
    print("\n--- SAVINGS GOAL PLANNER ---")

    target = get_float("Target Amount (₹): ")
    months = int(get_float("Number of Months: "))

    monthly = target / months

    loading()
    print("\nGOAL REPORT")
    print("-" * 50)
    print(f"Target Amount       : ₹{target:,.2f}")
    print(f"Months Available    : {months}")
    print(f"Monthly Saving Need : ₹{monthly:,.2f}")
    print("💡 Tip: Automate this saving via SIP for consistency.")
    print("-" * 50)


# ============================================================
# MAIN MENU
# ============================================================

def main():
    while True:

        header()

        print("\n👋 Welcome back!")
        print("What would you like to do today?\n")

        print("1️⃣  Interest & Investment Calculators")
        print("2️⃣  Budget Analysis")
        print("3️⃣  Profit / Loss Calculator")
        print("4️⃣  Discount Calculator")
        print("5️⃣  Savings Goal Planner")
        print("6️⃣  Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            interest_menu()

        elif choice == "2":
            budget_analysis()

        elif choice == "3":
            profit_loss()

        elif choice == "4":
            discount_calculator()

        elif choice == "5":
            savings_goal()

        elif choice == "6":
            print("\n🎉 Thank you for using Personal Finance Management System!")
            print("💰 Keep saving, keep investing, and keep growing.")
            print("📈 Every rupee invested today builds a better tomorrow.")
            print("🌟 Wishing you financial success ahead.")
            print("👋 Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()