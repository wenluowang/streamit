import streamlit as st
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar

def create_chart(df, product):
    countries = df['Country'].tolist()
    data = df[product].tolist()
    chart = (
        Bar()
        .add_xaxis(countries)
        .add_yaxis(product, data)
        .set_global_opts(title_opts=opts.TitleOpts(title=f'Number of Customers by Country and {product}'))
    )
    return chart

def main():
    st.title('Customer Data')

    # Add a file uploader button to read an Excel file
    uploaded_file = st.file_uploader("Upload Excel file", type="xlsx")

    if uploaded_file:
        # Read the uploaded Excel file into a pandas dataframe
        df = pd.read_excel(uploaded_file, engine='openpyxl')

        # Display the uploaded data in a table
        st.dataframe(df)

        # Allow the user to select a product
        product = st.selectbox('Select Product', df.columns[1:])

        # Create a chart using Pyecharts
        chart = create_chart(df, product)

        # Display the chart
        st_pyecharts(chart)

if __name__ == '__main__':
    main()
