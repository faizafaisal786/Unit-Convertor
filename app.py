import streamlit as st
from pint import UnitRegistry

# Initialize Pint unit registry
ureg = UnitRegistry()

# Set page config
st.set_page_config(
    page_title="Unit Converter",
    page_icon="📏",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        font-size: 1.2em;
    }
    .stTextInput>div>div>input {
        font-size: 1.2em;
        padding: 0.5em;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("📏 Unit Converter")
st.markdown("Convert between different units of measurement easily!")

# Define available units by category
unit_categories = {
    "Length": ["meter", "kilometer", "centimeter", "millimeter", "inch", "foot", "yard", "mile"],
    "Mass": ["gram", "kilogram", "milligram", "pound", "ounce"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Volume": ["liter", "milliliter", "gallon", "quart", "pint", "cup"],
    "Time": ["second", "minute", "hour", "day", "week", "month", "year"],
    "Area": ["square meter", "square kilometer", "square foot", "square inch", "acre", "hectare"]
}

# Create two columns for input and output
col1, col2 = st.columns(2)

with col1:
    # Input value
    input_value = st.number_input("Enter value", value=1.0, step=0.1)
    
    # Category selection
    selected_category = st.selectbox("Select category", list(unit_categories.keys()))
    
    # From unit selection
    from_unit = st.selectbox("From", unit_categories[selected_category])

with col2:
    # To unit selection
    to_unit = st.selectbox("To", unit_categories[selected_category])
    
    # Convert button
    if st.button("Convert"):
        try:
            # Create quantity with input value and from unit
            quantity = input_value * ureg(from_unit)
            
            # Convert to target unit
            result = quantity.to(to_unit)
            
            # Display result
            st.success(f"**Result:** {result.magnitude:.6g} {to_unit}")
            
            # Show conversion formula
            st.info(f"**Conversion:** {input_value} {from_unit} = {result.magnitude:.6g} {to_unit}")
            
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Add some helpful information
st.markdown("""
    ### Tips:
    - Select the appropriate category for your conversion
    - Enter the value you want to convert
    - Choose the source and target units
    - Click Convert to see the result
    """)

# Add information section
with st.expander("About"):
    st.write("""
    This unit converter allows you to convert between different units of measurement.
    It supports various categories including length, mass, temperature, time, volume, and area.
    The converter uses the Pint library to ensure accurate conversions.
    """)

# Footer
st.markdown("""
    <div style='position: fixed; bottom: 0; width: 100%; text-align: center; padding: 1rem; background-color: #f8f9fa;'>
        <p style='color: #666; margin: 0;'>Built with Streamlit and Pint</p>
    </div>
""", unsafe_allow_html=True) 