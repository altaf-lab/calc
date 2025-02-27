import streamlit as st

def calculator(num1, num2, opr):
    if opr == "+":
        return num1 + num2
    elif opr == "-":
        return num1 - num2
    elif opr == "*":
        return num1 * num2
    else:
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero is not allowed"

def main():
    st.title("Welcome to My Calculator...")
    number1 = st.number_input("Enter number 1:", format="%f")
    operator = st.selectbox("Select operator", ["+", "-", "*", "/"])
    number2 = st.number_input("Enter number 2:", format="%f")

    if st.button("Calculate"):
        result = calculator(number1, number2, operator)
        st.success(result)

if __name__ == "__main__":
    main()
