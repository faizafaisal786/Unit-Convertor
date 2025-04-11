# Unit Converter

A modern, Google-style unit converter built with Python and Streamlit. Convert between different units of measurement easily!

## Features

- Convert between various units of measurement including:
  - Length (meters, kilometers, inches, feet, etc.)
  - Mass (grams, kilograms, pounds, ounces)
  - Temperature (Celsius, Fahrenheit, Kelvin)
  - Volume (liters, milliliters, gallons, etc.)
  - Time (seconds, minutes, hours, etc.)
  - Area (square meters, square feet, acres, etc.)
- Clean and intuitive user interface
- Real-time conversion
- Error handling for invalid conversions

## Installation

1. Clone this repository or download the files
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)
3. Select the category and units you want to convert between
4. Enter the value you want to convert
5. Click "Convert" to see the result

## Deployment

This app is deployed on Streamlit Cloud. You can access it at:
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://faizafaisal786-unit-convertor-app-xxxxxx.streamlit.app)

To deploy your own version:
1. Fork this repository
2. Go to [Streamlit Cloud](https://share.streamlit.io/)
3. Click "New app"
4. Select your forked repository
5. Set the main file path to `app.py`
6. Click "Deploy!"

## Requirements

- Python 3.7+
- Streamlit
- Pint (for unit conversions)

## License

This project is open source and available under the MIT License. 