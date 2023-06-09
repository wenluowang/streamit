import streamlit as st
import pandas as pd
from googletrans import Translator

def translate_country_names(df):
    translator = Translator()

    # Create a new column to store the translated country names
    df['Country (EN)'] = df['国家'].apply(lambda x: translator.translate(x, dest='en').text)

    return df

def main():
    st.title('CSV File Viewer')

    # Add a file uploader button to read a CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type="csv")

    if uploaded_file:
        # Read the uploaded CSV file into a pandas dataframe
        df = pd.read_csv(uploaded_file, encoding='gb18030')

        # Translate the country names and add a new column to the dataframe
        df = translate_country_names(df)

        # Display the uploaded data in a table
        st.dataframe(df)

if __name__ == '__main__':
    main()