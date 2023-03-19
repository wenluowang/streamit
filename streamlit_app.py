import streamlit as st
import pandas as pd

def main():
    st.title('Excel File Viewer')

    # Add a file uploader button to read an Excel file
    uploaded_file = st.file_uploader("Upload Excel file", type="xlsx")

    if uploaded_file:
        # Read the uploaded Excel file into a pandas dataframe
        df = pd.read_excel(uploaded_file, engine='openpyxl')

        # Display the uploaded data in a table
        st.dataframe(df)

if __name__ == '__main__':
    main()