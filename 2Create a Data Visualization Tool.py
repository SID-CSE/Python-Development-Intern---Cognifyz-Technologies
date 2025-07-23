# Level 3 :Task 2
# Task: Create a Data Visualization Tool
'''
 Build a tool that takes a dataset and generates interactive visualizations using libraries such as Matplotlib,
 Seaborn, or Plotly. This task will enhance their understanding of data visualization principles
 and plotting techniques.
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

st.title("Data Visualization Tool")

uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset Loaded!")
    st.dataframe(df.head())


    plot_type = st.selectbox("Choose Visualization Type", [
        "Histogram", "Bar Chart", "Scatter Plot", "Heatmap", "Plotly Interactive Scatter"
    ])

    if plot_type == "Histogram":
        column = st.selectbox("Select Column", df.columns)
        fig, ax = plt.subplots()
        sns.histplot(df[column], kde=True, ax=ax)
        st.pyplot(fig)

    elif plot_type == "Bar Chart":
        x = st.selectbox("X-Axis", df.columns)
        y = st.selectbox("Y-Axis", df.columns)
        fig, ax = plt.subplots()
        sns.barplot(x=df[x], y=df[y], ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    elif plot_type == "Scatter Plot":
        x = st.selectbox("X-Axis", df.columns)
        y = st.selectbox("Y-Axis", df.columns)
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[x], y=df[y], ax=ax)
        st.pyplot(fig)

    elif plot_type == "Heatmap":
        fig, ax = plt.subplots()
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    elif plot_type == "Plotly Interactive Scatter":
        x = st.selectbox("X-Axis", df.columns)
        y = st.selectbox("Y-Axis", df.columns)
        fig = px.scatter(df, x=x, y=y, title="Interactive Scatter Plot")
        st.plotly_chart(fig)
