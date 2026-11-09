# Sistema de vendas
# Seção cadastrar vendas
    # campo vendedor
    # campo produto
    # campo quantidade
    # campo valor
    # botão cadastrar vendas
        # quando clicar no botão -> adicionar venda na tabela
# Seção vendas cadastradas
    # tabela com vendas
# Seção dashboard
    # card/métrica -> faturamento total
    # gráfico de barra/coluna -> venda por vendedor
    # gráfico de pizza -> venda por produto


import streamlit as st
import pandas as pd
import plotly.express as px

tabela_vendas = pd.read_csv('vendas.csv')

# Passo 1: Criar a tela do sistema
st.write('# Sistema de Vendas')

# Passo 2: Criar o formulário de cadastro
# Passo 3: Salvar a venda na base de dados
st.sidebar.write('## Cadastrar Vendas')
data = st.sidebar.date_input('Data')
vendedor = st.sidebar.selectbox('Vendedor', ['Ana', 'Bruno', 'Carla'])
produto = st.sidebar.selectbox('Produto', ['Celular', 'Notebook', 'Fone'])
quantidade = st.sidebar.number_input('Quantidade', step=1)
valor = st.sidebar.number_input('Valor')
botao_cadastrar = st.sidebar.button('Cadastrar Venda')
# lógica de cadastro
if botao_cadastrar:
    if quantidade <= 0:
        st.warning('Informe uma quantidade maior que zero')
    elif valor <= 0:
        st.warning('Informe um valor maior que zero')
    else:
        nova_venda = [str(data), vendedor, produto, quantidade, valor]
        ultima_linha = len(tabela_vendas)
        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv('vendas.csv', index=False)
        st.success('Venda cadastrada!')

# Passo 4: Mostrar a base de dados na tela
st.write('## Vendas Cadastradas')
st.dataframe(tabela_vendas)


# Passo 5: Criar o dashboard com os gráficos
st.write('## Dashboard')

# Card - faturamento (formato brasileiro: 383.050,00)
faturamento = tabela_vendas['valor'].sum()
faturamento_br = f'{faturamento:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
st.metric('Faturamento Total', f'R$ {faturamento_br}')

# Gráfico - venda por vendedor
grafico1 = px.bar(tabela_vendas, x='vendedor', y='valor', color='produto')
st.plotly_chart(grafico1)

# Gráfico - venda por produto
grafico2 = px.pie(tabela_vendas, names='produto', values='valor', hole=0.3)
st.plotly_chart(grafico2)
