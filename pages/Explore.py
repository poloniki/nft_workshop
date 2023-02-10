import streamlit as st
import psycopg2
import pandas as pd
conn = psycopg2.connect(
    host="65.108.32.173",
    database="postgres",
    user="postgres",
    password= 'NQRLGaAjR44JM5Zk' #st.secrets["db_password"]
)

df = pd.read_sql_query("SELECT * FROM workshop", conn)
df = df.drop(columns=['cuisine'])
df.columns = ['Name', 'Twitter', 'Tezos', 'Teia']
st.write(df.style.format({'Twitter': '<a href="{}" target="_blank">Twitter</a>', 'Tezos': '<a href="{}" target="_blank">Tezos</a>', 'Teia': '<a href="{}" target="_blank">NFT</a>'}).render(), unsafe_allow_html=True)
