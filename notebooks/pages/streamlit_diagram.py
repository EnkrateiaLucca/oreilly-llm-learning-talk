import streamlit as st
import pandas as pd
import plotly.express as px

# Initialize a sample dataframe
initial_data = {
    'Column1': [1, 2, 3, 4],
    'Column2': [4, 3, 2, 1],
    'Column3': [2, 3, 4, 1]  # Adding an extra column for the scatter plot
}
df = pd.DataFrame(initial_data)

# Streamlit app layout
st.title("Editable DataFrame, Plotly Plot, and Interactive Diagram")

# Creating two columns
col1, col2 = st.columns(2)

# Column 1: Editable DataFrame
with col1:
    st.header("Editable DataFrame")
    # Streamlit function to display and edit dataframe
    df = st.data_editor(df, num_rows="dynamic")

# Column 2: Plot of the DataFrame and Diagram
with col2:
    st.header("Plot of Data")
    # Check if DataFrame is not empty
    if not df.empty:
        # Plotting the data using Plotly
        fig = px.line(df, labels={'value': 'Values', 'index': 'Index'}, title='Interactive Line Plot')
        st.plotly_chart(fig, use_container_width=True)
        
        # Scatter Plot Diagram
        st.header("Interactive Scatter Plot Diagram")
        scatter_fig = px.scatter(df, x='Column1', y='Column2', size='Column3', color='Column3', 
                                 labels={'Column1': 'Column 1', 'Column2': 'Column 2', 'Column3': 'Column 3'}, 
                                 title='Interactive Scatter Plot')
        st.plotly_chart(scatter_fig, use_container_width=True)
    else:
        st.write("No data to plot!")

# Save changes (if needed)
if st.button('Save Changes'):
    # Perform actions to save the changes, like updating a database, file, etc.
    st.write("Changes saved!")
