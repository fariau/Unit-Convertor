import streamlit as st

# 🚀 App title
st.title("🔄 Unit Converter")

# Unit conversion types
conversion_types = ["📏 Length", "🌡️ Temperature", "⚖️ Weight"]

# User chooses conversion type
conversion_choice = st.selectbox("🎯 Choose conversion type:", conversion_types)

# Length conversion
if conversion_choice == "📏 Length":
    length_units = ["Meters", "Kilometers", "Feet", "Inches", "Centimeters"]
    input_value = st.number_input("📐 Enter length value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("🔄 Convert from:", length_units)
    to_unit = st.selectbox("➡️ Convert to:", length_units)

    # Conversion dictionary (values are in meters)
    length_conversion = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Inches": 0.0254,
        "Centimeters": 0.01
    }

    if st.button("🔢 Convert"):
        result = input_value * (length_conversion[from_unit] / length_conversion[to_unit])
        st.success(f'✅ {input_value} {from_unit} is equal to {result:.2f} {to_unit} 🎉')

# Weight conversion
elif conversion_choice == "⚖️ Weight":
    weight_units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    input_value = st.number_input("⚖️ Enter weight value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("🔄 Convert from:", weight_units)
    to_unit = st.selectbox("➡️ Convert to:", weight_units)

    # Conversion dictionary (values are in kilograms)
    weight_conversion = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495
    }

    if st.button("🔢 Convert"):
        result = input_value * (weight_conversion[from_unit] / weight_conversion[to_unit])
        st.success(f'✅ {input_value} {from_unit} is equal to {result:.2f} {to_unit} 🎉')

# Temperature conversion
elif conversion_choice == "🌡️ Temperature":
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
    input_value = st.number_input("🌡️ Enter temperature value:", format="%.2f")
    from_unit = st.selectbox("🔄 Convert from:", temperature_units)
    to_unit = st.selectbox("➡️ Convert to:", temperature_units)

    def convert_temperature(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        elif from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32

    if st.button("🔢 Convert"):
        result = convert_temperature(input_value, from_unit, to_unit)
        st.success(f'✅ {input_value} {from_unit} is equal to {result:.2f} {to_unit} 🎉')
