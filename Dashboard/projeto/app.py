import streamlit as st
import pandas as pd
import numpy as np


#st.header('My Dashboard')
#st.sidebar.header('Escolha o que deseja filtrar')

#pessoas= [{'Nome': 'Caio', 'Idade': 22,}, {'Nome': 'Lucimar', 'Idade': 35,}]

#st.write(pessoas)

# Exibição de dados

#x = [[20, 90, 2, 4],
#     [30, 50, 3, 2]
#]
df = pd.DataFrame(
    np.random.rand(10, 4),
    columns=['Preço', 'Taxa de ocupação', 'Taxa de inadimplência', 'Pessoas com casas']
)

st.table(df)