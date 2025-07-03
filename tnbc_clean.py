import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network

@st.cache_data
def load_data():
    return pd.read_csv("tnbc_kg_triplets_chemical_biotech_other.csv")

kg_df = load_data()

# App config
st.set_page_config(layout="wide")
st.title("TNBC Clinical Trials Explorer")

# Sidebar filters
with st.sidebar:
    st.header("Filters")

    category = st.radio(
        "Therapy Type",
        ["BIOTECH", "CHEMICAL", "OTHER"],
        index=0
    )

    relation_options = sorted(kg_df['Relation'].unique())
    relations = st.multiselect(
        "Relationships",
        options=relation_options,
        default=[relation_options[0]] if relation_options else []
    )

# Filter data
filtered_df = kg_df[
    (kg_df['Relation'].isin(relations)) &
    (kg_df['Source'].str.startswith(f"{category}_TRIAL"))
]

# Main display
tab1, tab2 = st.tabs(["Data View", "Knowledge Graph"])

with tab1:
    st.dataframe(filtered_df, height=500)

with tab2:
    g = nx.Graph()
    for _, row in filtered_df.iterrows():
        g.add_node(row['Source'], size=15, color="#1f77b4")
        g.add_node(row['Target'], size=10, color="#ff7f0e")
        g.add_edge(row['Source'], row['Target'])
    
    net = Network(height="600px", width="100%", notebook=False)
    net.from_nx(g)
    net.repulsion(node_distance=150)
    net.save_graph("tnbc_kg.html")
    st.components.v1.html(open("tnbc_kg.html").read(), height=620)
