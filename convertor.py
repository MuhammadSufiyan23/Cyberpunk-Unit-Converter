import streamlit as st

st.set_page_config(page_title="Cyberpunk Unit Converter", layout="centered", page_icon="🔥")

st.markdown(
    """
    <style>
    body {
        background-color: #0c0c0d;
        color: white;
        font-family: 'Arial', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #141e30, #243b55);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 40px rgba(0, 255, 255, 0.3);
    }

    h1 {
        text-align: center;
        font-size: 42px;
        color: #00ffd5;
        text-shadow: 2px 2px 15px rgba(0, 255, 213, 0.8);
        font-weight: bold;
    }

    .stButton > button {
        background: linear-gradient(90deg, #ff00ff, #00ffff);
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 14px 28px;
        border-radius: 12px;
        transition: all 0.3s ease-in-out;
        box-shadow: 0px 5px 25px rgba(0, 255, 255, 0.6);
        border: none;
        cursor: pointer;
    }

    .stButton > button:hover {
        transform: scale(1.1);
        background: linear-gradient(90deg, #ff7300, #ff00ff);
        color: black;
    }

    .glass-box {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        padding: 20px;
        border-radius: 15px;
        margin-top: 20px;
        box-shadow: 0px 5px 20px rgba(255, 255, 255, 0.2);
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #ffcc00;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e, #16213e);
        color: white;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0px 5px 15px rgba(0, 255, 255, 0.4);
        backdrop-filter: blur(12px);
     }

    .result-box {
        background: linear-gradient(135deg, rgba(0, 255, 255, 0.3), rgba(0, 0, 0, 0.7));
        backdrop-filter: blur(20px);
        padding: 15px;
        border-radius: 12px;
        margin-top: 20px;
        box-shadow: 0px 10px 25px rgba(0, 255, 255, 0.6), 0px 0px 15px rgba(255, 255, 0, 0.8);
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        color: #ffcc00;
        text-shadow: 3px 3px 10px rgba(255, 204, 0, 0.9);
    }

    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 16px;
        color: #ffcc00;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='color:white;'>🔥 Ultimate Cyberpunk Unit Converter 🔥</h1>", unsafe_allow_html=True)


st.sidebar.markdown("<h3 style='color:#00ffff; text-align:center;'>🎛 Choose Conversion Type</h3>", unsafe_allow_html=True)

conversion_type = st.sidebar.selectbox(
    "📌 Conversion Type", 
     ["Length 📏", "Weight ⚖️", "Temperature 🌡️"]
)




st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.write("🔹 **Quick Tips:**")
st.sidebar.write("📏 Length conversions are accurate up to 4 decimal places.")
st.sidebar.write("⚖️ Weight conversions follow standard metric units.")
st.sidebar.write("🌡️ Temperature formulas are precise & reliable.")
st.sidebar.markdown("<hr style='border: 1px solid #00ffff;'>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align:center; color:#ffcc00;'>🚀 Built for Speed & Accuracy! </p>", unsafe_allow_html=True)




unit_options = {
    "Length 📏": ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"],
    "Weight ⚖️": ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"],
    "Temperature 🌡️": ["Celsius", "Fahrenheit", "Kelvin"]
}



if conversion_type == "Temperature 🌡":
    value = st.number_input("Enter Value", value=0.0, step=0.1)
else:
    value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)



col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", unit_options[conversion_type])
with col2:
    to_unit = st.selectbox("To", unit_options[conversion_type])



def length_converter(value, from_unit, to_unit):
    length_units = {
        "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000,
        "Miles": 0.000621371, "Yards": 1.09361, "Inches": 39.37, "Feet": 3.28084
    }
    return (value / length_units[from_unit] * length_units[to_unit])

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "Kilogram": 1, "Grams": 1000, "Milligrams": 1000000, 
        "Pounds": 2.20462, "Ounces": 35.274
    }
    return (value / weight_units[from_unit] * weight_units[to_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    conversions = {
        ("Celsius", "Fahrenheit"): lambda x: x * 9/5 + 32,
        ("Celsius", "Kelvin"): lambda x: x + 273.15,
        ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5/9,
        ("Fahrenheit", "Kelvin"): lambda x: (x - 32) * 5/9 + 273.15,
        ("Kelvin", "Celsius"): lambda x: x - 273.15,
        ("Kelvin", "Fahrenheit"): lambda x: (x - 273.15) * 9/5 + 32,
    }
    return conversions.get((from_unit, to_unit), lambda x: x)(value)



if st.button("Convert 🔄"):
    if conversion_type == "Length 📏":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight ⚖️":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature 🌡️":
        result = temperature_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>🚀 {value} {from_unit} = <span style='color:#00ffff;'> {result:,.4f} </span> {to_unit}</div>", unsafe_allow_html=True)
    

st.markdown("<div class='footer'>🔥 Transforming Ideas into Reality – One Conversion at a Time. Because every number counts!</div>", unsafe_allow_html=True)
