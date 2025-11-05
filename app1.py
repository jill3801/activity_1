import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simple Streamlit App", page_icon="📊")

# Title
st.title("📊 Simple Streamlit Data Explorer")

# Sidebar
st.sidebar.header("Settings")
rows = st.sidebar.slider("Number of data points", 10, 200, 50)
chart_type = st.sidebar.selectbox("Choose chart type", ["Line", "Bar", "Area"])

# Create random data
data = pd.DataFrame({
    "x": np.arange(rows),
    "y": np.random.randn(rows).cumsum()
})

# Display data
st.write("### Generated Data")
st.dataframe(data)

# Plot chart
st.write("### Chart")
if chart_type == "Line":
    st.line_chart(data.set_index("x"))
elif chart_type == "Bar":
    st.bar_chart(data.set_index("x"))
else:
    st.area_chart(data.set_index("x"))

# Add interaction
st.write("### Summary")
st.write(f"Average value: {data['y'].mean():.2f}")
st.write(f"Maximum value: {data['y'].max():.2f}")
st.write(f"Minimum value: {data['y'].min():.2f}")

# Add a button example
if st.button("Generate New Data"):
    st.experimental_rerun()
