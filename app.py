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
import streamlit as st

# Function definitions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# App title and style
st.set_page_config(page_title="Temperature Converter", page_icon="🌡️", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 12px;
    }
    .stButton>button {
        color: white;
        background-color: #ff7f50;
        border-radius: 8px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main'>", unsafe_allow_html=True)

# Title and description
st.markdown("<h1 style='color: #ff4500;'>🌡️ Temperature Converter</h1>", unsafe_allow_html=True)
st.write("Easily convert between Celsius and Fahrenheit with this interactive tool.")

# Layout with columns
col1, col2 = st.columns(2)
with col1:
    st.image("https://img.icons8.com/fluency/96/temperature.png", width=80)
with col2:
    conversion = st.radio("Select conversion direction:", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])

# Input and conversion
if conversion == "Celsius to Fahrenheit":
    celsius = st.number_input("Enter temperature in Celsius:", format="%.2f", step=0.1)
    if st.button("Convert to Fahrenheit"):
        fahrenheit = celsius_to_fahrenheit(celsius)
        st.success(f"🌡️ {celsius:.2f}°C is **{fahrenheit:.2f}°F**")

else:
    fahrenheit = st.number_input("Enter temperature in Fahrenheit:", format="%.2f", step=0.1)
    if st.button("Convert to Celsius"):
        celsius = fahrenheit_to_celsius(fahrenheit)
        st.success(f"🌡️ {fahrenheit:.2f}°F is **{celsius:.2f}°C**")

st.markdown("</div>", unsafe_allow_html=True)

