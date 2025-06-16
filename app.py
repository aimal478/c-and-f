import streamlit as st

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit UI
st.title("🌡️ Temperature Converter")
st.write("Convert between Celsius and Fahrenheit")

# Conversion selection
conversion = st.radio("Choose conversion direction:", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

# Input based on choice
if conversion == "Celsius to Fahrenheit":
    celsius = st.number_input("Enter temperature in Celsius", format="%.2f")
    fahrenheit = celsius_to_fahrenheit(celsius)
    st.success(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")

else:
    fahrenheit = st.number_input("Enter temperature in Fahrenheit", format="%.2f")
    celsius = fahrenheit_to_celsius(fahrenheit)
    st.success(f"{fahrenheit:.2f}°F = {celsius:.2f}°C")

