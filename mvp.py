import streamlit as st
from main import calcular
import pandas as pd


valor_compra = (st.text_input('Valor de Compra'))
cartao = st.selectbox('Pagamento no cartão?', ['Sim', 'Não'])
comissao = st.selectbox('Quem vendeu?', ['Vendedora', 'Supervisora', 'Gerente', 'Sem_comissão'])

st.table(pd.DataFrame(calcular(valor_compra, cartao, comissao), index=['0']))