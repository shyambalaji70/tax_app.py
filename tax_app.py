import streamlit as st

def calculate_income_tax(income):
   
    standard_deduction = 75000  # Standard deduction for salaried individuals
    taxable_income = max(0, income - standard_deduction)  # Apply deduction

    tax_slabs = [
        (400000, 0.00),   # Up to Rs 4,00,000: 0%
        (800000, 0.05),   # Rs 4,00,001 to Rs 8,00,000: 5%
        (1200000, 0.10),  # Rs 8,00,001 to Rs 12,00,000: 10%
        (1600000, 0.15),  # Rs 12,00,001 to Rs 16,00,000: 15%
        (2000000, 0.20),  # Rs 16,00,001 to Rs 20,00,000: 20%
        (2400000, 0.25),  # Rs 20,00,001 to Rs 24,00,000: 25%
        (float('inf'), 0.30)  # Above Rs 24,00,000: 30%
    ]

    tax_payable = 0.0
    previous_limit = 0

    for limit, rate in tax_slabs:
        if taxable_income > limit:
            tax_payable += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            tax_payable += (taxable_income - previous_limit) * rate
            break

    cess = tax_payable * 0.04
    tax_payable += cess

    if taxable_income <= 1200000:
        tax_payable = 0.0
    elif taxable_income <= 1275000:
        # Calculate tax without rebate
        tax_without_rebate = tax_payable
        # Calculate excess income over Rs 12,00,000
        excess_income = taxable_income - 1200000
        # Marginal relief ensures tax payable does not exceed excess income
        tax_payable = min(tax_without_rebate, excess_income)

    return tax_payable

st.title("India Income Tax Calculator New Regime (2025)")

salary = st.number_input("Enter your annual salary (in Rs)", min_value=0, step=1000)

if st.button("Calculate Tax"):
    tax = calculate_income_tax(salary)
    taxable_income = max(0, salary - 75000)

    st.write("### Tax Details:")
    st.write(f"**Gross Salary:** Rs {salary:.2f}")
    st.write(f"**Standard Deduction:** Rs 75,000.00")
    st.write(f"**Taxable Income:** Rs {taxable_income:.2f}")
    st.write(f"**Total Tax Payable:** Rs {tax:.2f}")
