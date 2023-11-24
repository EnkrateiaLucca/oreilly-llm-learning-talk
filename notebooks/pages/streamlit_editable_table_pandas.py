import streamlit as st
import pandas as pd

def create_table(num_rows):
    data = {'Column 1': range(1, num_rows+1),}
    df = pd.DataFrame(data)
    return df

def main():
    st.title("Editable Table App")
    # Slider to select the number of rows
    num_rows = st.slider("Number of Rows", min_value=1, max_value=10, value=5)
    # Create the table
    df = create_table(num_rows)
    # Display the table
    st.table(df)
    

if __name__ == "__main__":
    main()