import streamlit as st

st.set_page_config(
    page_title="Projeto de Estilização Streamlit", 
    page_icon="",
    layout="wide"
)


st.title("Projeto de Estilização de Streamlit")
st.subheader("Exemplo de como organizar e estilizar um site")

st.sidebar.header("Filtros")
st.sidebar.checkbox("Ativar tema escuro", key="tema")
st.sidebar.slider("Selecione valor", 0, 100, 25)

st.metric("Vendas","R$50.000","+5%")
st.metric("Usuários","1.200","-2%")


col1, col2,col3 = st.columns(3)

with col1:
    st.header("Coluna 1")
    st.success("Tudo certo!")
    st.button("Clique aqui")


with col2:
    st.header("Coluna 2")
    st.warning("Atenção!")
    st.radio("Escolha um item",["Opção A","Opção B","Opção C"])

with col3:
    st.header("Coluna 3")
    st.info("Informação útil")
    st.selectbox("Escolha um item",["Item 1", "Item 2", "Item 3"])

with st.expander("Veja mais detalhes"):
    st.write("Aqui dentro você pode colocar informações adicionais, gráficos ou tabelas")
    st.checkbox("Ativar detalhe extra")
    st.text_input("Digite algo interessante")

st.markdown (
    """
    <div style= 'background-color:#f9f9f9; padding: 10px; border-radius: 5px'>
    <h4 style='color: #FF5733;'> Texto colorido com estilo personalizado </h4>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")
st.markdown(" Exemplo simples de estilização do Streamlit sem lógica complexa")