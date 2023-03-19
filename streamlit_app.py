import streamlit as st
import pandas as pd

def main():
    st.title('CSV File Viewer')

    # Add a file uploader button to read a CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type="csv")

    if uploaded_file:
        # Read the uploaded CSV file into a pandas dataframe
        df = pd.read_csv(uploaded_file, encoding='gb18030')

        # Display the uploaded data in a table
        st.dataframe(df)

if __name__ == '__main__':
    main()