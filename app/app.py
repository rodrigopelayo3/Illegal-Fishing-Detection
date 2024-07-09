import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Custom CSS for background color, larger fonts, and reduced padding/margins
# Custom CSS for background color, larger fonts, and reduced padding/margins
def set_bg_hack():
    st.markdown(
        """
        <style>
        .stApp {
            background: #041f3d; /* Darker ocean blue background */
            padding: 0;
            margin: 0;
        }
        .sidebar .sidebar-content {
            background: #0a3d62; /* Slightly lighter blue for sidebar */
            padding: 10px; /* Reduced padding for sidebar */
        }
        .css-1d391kg p {
            font-size: 20px; /* Increase font size for paragraphs */
        }
        .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3, .css-1d391kg h4, .css-1d391kg h5, .css-1d391kg h6 {
            font-size: 24px; /* Increase font size for headers */
        }
        .css-1y0tads {
            padding: 1rem 2rem; /* Adjust padding for main container */
            max-width: 100%; /* Use full width */
        }
        .css-18e3th9 {
            padding: 1rem; /* Adjust padding for sidebar */
            max-width: 100%; /* Use full width */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_hack()


# Set up the Streamlit app
st.title('Detecting Illegal Fishing')
st.markdown('### Map displaying the vessels that went missing by AIS from 2017 to 2019')



# Read the HTML file and embed it in the Streamlit app
with open('map.html', 'r') as file:
    map_html = file.read()

# Display the HTML string in Streamlit
st.components.v1.html(map_html, width=800, height=500)

# Conversion functions
def km_to_m(km):
    return km * 1000

def nm_to_m(nm):
    return nm * 1852

# User interaction section
st.sidebar.header('Please pick up your Parameters')

# User input guide
st.sidebar.markdown("""
### Input Guide:
- **Gap Hours:** 12 - 200
- **Distance to Marine Protected Area (km):** 31 - 4593
- **Vessel Class:** Choose from the dropdown
- **Flag:** Choose from the dropdown
- **Model:** Choose from the dropdown
""")

# Essential user input fields
gap_hours = st.sidebar.number_input('Gap Hours', min_value=12, max_value=200, value=23)
distance_to_mpa_km = st.sidebar.number_input('Distance to a Marine Protected Area (km)', min_value=31.0, max_value=4593.0, value=1945.93)
vessel_class = st.sidebar.selectbox('Vessel Class', ['drifting_longlines', 'squid_jigger', 'trawlers', 'tuna_purse_seines'])

# Mapping of flags
flag_mapping = {
    "CHN": "China",
    "TWN": "Taiwan",
    "ESP": "Spain",
    "USA": "United States",
    "KOR": "South Korea",
    "FRA": "France",
    "JPN": "Japan",
    "VUT": "Vanuatu",
    "ECU": "Ecuador",
    "LKA": "Sri Lanka",
    "RUS": "Russia",
    "PRT": "Portugal",
    "SYC": "Seychelles",
    "PAN": "Panama",
    "ARG": "Argentina",
    "AUS": "Australia",
    "PHL": "Philippines",
    "FSM": "Micronesia",
    "ZAF": "South Africa",
    "NZL": "New Zealand",
    "BLZ": "Belize",
    "MEX": "Mexico",
    "FJI": "Fiji",
    "PNG": "Papua New Guinea",
    "CUW": "Curacao",
    "MUS": "Mauritius",
    "GBR": "United Kingdom",
    "NOR": "Norway",
    "MHL": "Marshall Islands",
    "IRL": "Ireland",
    "SEN": "Senegal",
    "VEN": "Venezuela",
    "REU": "Reunion",
    "GHA": "Ghana",
    "SLB": "Solomon Islands",
    "NAM": "Namibia",
    "SLV": "El Salvador",
    "CAN": "Canada",
    "FLK": "Falkland Islands",
    "GTM": "Guatemala",
    "MYS": "Malaysia",
    "KIR": "Kiribati",
    "CPV": "Cape Verde",
    "COK": "Cook Islands",
    "FRO": "Faroe Islands",
    "URY": "Uruguay",
    "EST": "Estonia",
    "BRA": "Brazil",
    "UKR": "Ukraine",
    "COL": "Colombia",
    "ITA": "Italy",
    "ALB": "Albania",
    "DEU": "Germany",
    "KEN": "Kenya",
    "SMR": "San Marino",
    "DNK": "Denmark",
    "VCT": "Saint Vincent and the Grenadines",
    "IRN": "Iran",
    "AGO": "Angola",
    "GEO": "Georgia",
    "PER": "Peru",
    "IDN": "Indonesia",
    "SHN": "Saint Helena",
    "CIV": "Ivory Coast",
    "NIC": "Nicaragua",
    "KNA": "Saint Kitts and Nevis",
    "BEL": "Belgium",
    "MOZ": "Mozambique",
    "MWI": "Malawi",
    "NRU": "Nauru",
    "COM": "Comoros",
    "GNB": "Guinea-Bissau",
    "ISL": "Iceland",
    "GRL": "Greenland",
    "LTU": "Lithuania",
    "GIN": "Guinea",
    "CXR": "Christmas Island",
    "NCL": "New Caledonia",
    "ATF": "French Southern Territories",
    "TUV": "Tuvalu",
    "CHL": "Chile",
    "TZA": "Tanzania",
    "POL": "Poland",
    "GNQ": "Equatorial Guinea",
    "OMN": "Oman",
    "IND": "India",
    "CYP": "Cyprus",
    "WSM": "Samoa",
    "CMR": "Cameroon",
    "NGA": "Nigeria",
    "YEM": "Yemen",
    "PYF": "French Polynesia",
    "LVA": "Latvia",
    "GRC": "Greece",
    "NLD": "Netherlands",
    "MLT": "Malta",
    "TCA": "Turks and Caicos Islands",
    "AFG": "Afghanistan",
    "IRQ": "Iraq",
    "MDG": "Madagascar"
}

# Create a list of tuples for the dropdown
flag_options = [(code, f"{code} - {country}") for code, country in flag_mapping.items()]

# Create the flag dropdown
selected_flag = st.sidebar.selectbox('Flag', flag_options, format_func=lambda x: x[1])[0]

# Encode the selected flag
flag_encoder = LabelEncoder()
flag_encoder.fit([option[0] for option in flag_options])
flag_encoded = flag_encoder.transform([selected_flag])[0]

# Dropdown to select the model
model_choice = st.sidebar.selectbox('Select Model', ['Logistic Regression', 'Random Forest', 'XGBoost', 'MLP'])

# Hidden menu for additional parameters
expander = st.sidebar.expander("Adjust Advanced Parameters")
with expander:
    st.markdown("""
    ### Advanced Input Guide:
    - **Distance to High Risk Zone (km):** 9.34 - 4370.62
    - **Distance Event Start to End (km):** 0 - 19434.12
    - **Distance Difference from Shore (km):** -1984 - 2027
    - **Tonnage per Meter:** 0.68 - 139.86
    """)
    
    distance_to_high_risk_zone_km = st.number_input('Distance to High Risk Zone (km)', min_value=9.34, max_value=4370.62, value=1332.32)
    distance_event_start_to_end_km = st.number_input('Distance Event Start to End (km)', min_value=0.0, max_value=19434.12, value=76.58)
    distance_difference_from_shore_km = st.number_input('Distance Difference from Shore (km)', min_value=-1984.0, max_value=2027.0, value=-3.0)
    tonnage_per_meter = st.number_input('Tonnage per Meter', min_value=0.68, max_value=139.86, value=13.21)

# Vessel class encoding
vessel_class_encoding = {
    'drifting_longlines': [1, 0, 0, 0],
    'squid_jigger': [0, 1, 0, 0],
    'trawlers': [0, 0, 1, 0],
    'tuna_purse_seines': [0, 0, 0, 1]
}

vessel_class_encoded = vessel_class_encoding[vessel_class]

# Map the model choice to the corresponding file name
model_files = {
    'Logistic Regression': 'LogisticRegression.pkl',
    'Random Forest': 'RandomForest.pkl',
    'XGBoost': 'XGBoost.pkl',
    'MLP': 'MLP_Neural_Networks.pkl'
}

# Load the selected model and scaler
model_file = model_files[model_choice]
model = joblib.load(model_file)
scaler = joblib.load('scaler.pkl')

# Prepare the input data for prediction
features_to_scale = [
    gap_hours,
    km_to_m(distance_to_high_risk_zone_km),
    km_to_m(distance_to_mpa_km),
    km_to_m(distance_event_start_to_end_km),
    km_to_m(distance_difference_from_shore_km),
    tonnage_per_meter
]

# Scale the input data
#features_to_scale_scaled = scaler.transform([features_to_scale])

# Combine scaled and unscaled features
#input_data = features_to_scale_scaled[0].tolist() + vessel_class_encoded + [flag_encoded]

# Make a prediction
#prediction = model.predict([input_data])

# Function to make a prediction
def make_prediction():
    # Scale the input data
    features_to_scale_scaled = scaler.transform([features_to_scale])

    # Combine scaled and unscaled features
    input_data = features_to_scale_scaled[0].tolist() + vessel_class_encoded + [flag_encoded]

    # Make a prediction
    prediction = model.predict([input_data])
    return prediction[0]

# Reference table for explaining predictions
reference_table = """
| Rank | Vessel Type        | Known IUU Risk Level | Average Speed                              | Average Fishing Time | Description                                                                                                                                                |
|------|--------------------|----------------------|--------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1    | Trawlers           | High                 | 10-12 knots (18.5-22.2 km/h or 11.5-13.8 mph) | 12-18 hours per day  | **IUU Risk**: Frequently engage in illegal fishing in restricted areas and overfishing. **Description**: Trawlers are heavily associated with IUU fishing due to their large catch capacity and operations in restricted zones. |
| 2    | Tuna Purse Seiners | High                 | 12-15 knots (22.2-27.8 km/h or 13.8-17.3 mph) | 4-8 hours per set    | **IUU Risk**: Known for illegal fishing in marine protected areas and exceeding quotas. **Description**: Tuna purse seiners are large and highly mobile, often implicated in unreported fishing activities. |
| 3    | Drifting Longlines | Medium to High       | 8-10 knots (14.8-18.5 km/h or 9.2-11.5 mph)  | 24-48 hours per set  | **IUU Risk**: Involved in bycatch and unreported catches, especially of endangered species. **Description**: Operate in vast ocean areas, making them a significant concern for IUU fishing, particularly for high-value species like tuna and swordfish. |
| 4    | Squid Jiggers      | Medium               | 10-12 knots (18.5-22.2 km/h or 11.5-13.8 mph) | 6-12 hours per night | **IUU Risk**: Often fish in international waters with weak regulations. **Description**: Typically implicated in IUU fishing where squid populations are not well-regulated, leading to overfishing and unreported catches. |
| 5    | Other              | Variable             | Varies widely depending on vessel type       | Variable             | **IUU Risk**: Includes smaller, artisanal boats and other less common vessel types. **Description**: The IUU risk in this category depends on the specific type of vessel and fishing practice, with smaller boats often involved due to lack of monitoring, especially in developing regions. |
"""

st.html("""<hr style="height:5px;border:none;color:#333;background-color:#FFFFFF;" /> """)
# Display user inputs
st.subheader('User Inputs')
st.write('Gap Hours:', gap_hours)
st.write('Distance to a Marine Protected Area (km):', distance_to_mpa_km)
st.write('Vessel Class:', vessel_class)
st.write('Flag:', selected_flag)
st.write('Model:', model_choice)



# Prediction button
if st.button('Predict'):
    prediction = make_prediction()
    
    # Display the prediction result with explanation
    st.subheader('IUU Prediction')
    st.write('Your predicted class is:', prediction, 'indicating that your event is:')
    
    if prediction == 1:
        st.markdown("""
            **Illegal**
            
            This event is marked as illegal due to the following reasons:
            - **Vessel Class:** Certain vessel classes are highly associated with illegal fishing activities.
            - **Distance to Marine Protected Area:** Vessels close to Marine Protected Areas are more likely to engage in illegal fishing activities.
            - **Gap Hours:** Long offline periods can indicate illegal activities, such as avoiding detection.
        """)
    else:
        st.markdown("""
            **Not Illegal**
            
            This event is marked as not illegal based on the current inputs. However, please note that this is based on the model's prediction and should be further verified.
        """)
        
        
st.html("""<hr style="height:5px;border:none;color:#333;background-color:#FFFFFF;" /> """)
# Display the reference table
st.subheader('Get to know more')
st.markdown(reference_table)

# Display the advanced parameters if the user has modified them
if expander.expanded:
    st.subheader('Advanced Parameters')
    st.write('Distance to High Risk Zone (km):', distance_to_high_risk_zone_km)
    st.write('Distance Event Start to End (km):', distance_event_start_to_end_km)
    st.write('Distance Difference from Shore (km):', distance_difference_from_shore_km)
    st.write('Tonnage per Meter:', tonnage_per_meter)
