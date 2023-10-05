import streamlit as st
import pandas as pd
import numpy as np
import datetime


#st.header('My Dashboard')
#st.sidebar.header('Escolha o que deseja filtrar')

#pessoas= [{'Nome': 'Caio', 'Idade': 22,}, {'Nome': 'Lucimar', 'Idade': 35,}]

#st.write(pessoas)

# Exibição de dados

#x = [[20, 90, 2, 4],
#     [30, 50, 3, 2]
#]



# if st.sidebar.button("Exibir gráfico"):
#     df = pd.DataFrame(
#         np.random.randn(10, 4),
#         columns=['Preço', 'Taxa de ocupação', 'Taxa de inadimplência', 'Pessoas por casas']
    
# )   
#     st.bar_chart(df)

# check = st.sidebar.checkbox("Aceito")

# if check:
#     st.write("maracado")

# opcao = st.sidebar.radio(
#     "Seleciona uma opção",
#     ("Preço", "Taxa de ocupação")
# )
# if opcao == "Preço":
#     df = pd.DataFrame(
#          np.random.randn(10, 1),
#          columns=['Preço']
#     )
#     st.bar_chart(df)
# elif opcao == "Taxa de ocupação":
#     df = pd.DataFrame(
#          np.random.randn(10, 1),
#          columns=['Taxa de ocupação']
#     )
#     st.line_chart(df)

# opcao = st.sidebar.selectbox(
#     "Selecione uma opção",
#     ("Preço", "Taxa de ocupação")
# )

# if opcao == "Preço":
#     df = pd.DataFrame(
#         np.random.randn(10,1),
#         columns=["Preço"]
#     )
#     st.line_chart(df)
# elif opcao == "Taxa de ocupação":
#     df = pd.DataFrame(
#         np.random.randn(10, 1),
#         columns=["Taxa de ocupação"]
#     )
#     st.bar_chart(df)

# opcao = st.sidebar.slider(
#     "Preço máximo e mínimo",
#     1.0, 100.0, (25.0, 75.0)
# )
# print(opcao)

# opcao = st.sidebar.text_input(
#     "Digite o seu texto"
  
# )
# print(opcao)

# opcao = st.sidebar.number_input(
#     "Digite sua idade",
# )
# print(opcao)

opcao = st.sidebar.date_input(
    "Digite sua idade",
    datetime.date(1990, 1, 1)
)
print(opcao)