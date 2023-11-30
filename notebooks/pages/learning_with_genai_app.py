import streamlit as st
import pandas as pd
import plotly.express as px

# Initialize a sample dataframe
initial_data = {
    'Column1': [1, 2, 3, 4],
    'Column2': [4, 3, 2, 1]
}
df = pd.DataFrame(initial_data)

# Streamlit app layout
st.title("Editable Dataframe and Plotly Plot")

# Creating two columns
col1, col2 = st.columns(2)

# Column 1: Editable DataFrame
with col1:
    st.header("Editable DataFrame")
    # Streamlit function to display and edit dataframe
    df = st.data_editor(df, num_rows="dynamic")

# Column 2: Plot of the DataFrame
with col2:
    st.header("Plot of Data") 
    # Check if DataFrame is not empty
    if not df.empty:
        # Plotting the data using Plotly
        fig = px.line(df, labels={'value': 'Values', 'index': 'Index'}, title='Interactive Plot')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No data to plot!")


function = st.selectbox("Select a function", ["x**2", "x**3", "2x"]) 
if not df.empty:
    if function=="x**2":
        df = df**2
    elif function=="x**3":
        df = df**3
    elif function=="2x":
        df = df*2
    # Plotting the data using Plotly
    fig = px.line(df, labels={'value': 'Values', 'index': 'Index'}, title='Interactive Plot')
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write("No data to plot!")

# Save changes (if needed)
if st.button('Save Changes'):
    # Perform actions to save the changes, like updating a database, file, etc.
    st.write("Changes saved!")

