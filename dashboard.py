"""
MudraForge Streamlit Dashboard.
Visualizes recorded gesture data, training metrics, and gesture mapping configurations.
"""

import streamlit as st


def main() -> None:
    # TODO: Add dataset explorer and class distribution charts
    # TODO: Add model training and evaluation controls
    st.set_page_config(page_title="MudraForge Dashboard", layout="wide")
    st.title("MudraForge Dashboard")


if __name__ == "__main__":
    main()
