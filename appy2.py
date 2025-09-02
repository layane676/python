import streamlit as st 

st.set_page_config(
    page_title="Painel de hábitos",
    page_icon="",
    layout="wide"
)

st.title("Painel de hábitos")
st.subheader("Registre e visualize seus hábitos diários")


st.sidebar.header("Seus hábitos")
sono = st.sidebar.slider("Horas de sono", 0, 12, 8)
agua = st.sidebar.slider("Litros de água", 0, 10, 5) 
exercicio = st.sidebar.selectbox("Exercício", ["Nenhum", "Leve","Moderado","Intenso"])

st.metric("Sono", f"{sono} horas")
st.metric("Água", f"{agua} copos")
st.metric("Exercício", exercicio)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Detalhes do Sono")
    st.write("Você dormiu bem!" if sono >= 7 else "Tente dormir mais!")

with col2:
    st.header("Hidratação")
    st.write("ótimo, você se hidratou bem!" if agua >= 2 else "Tente beber mais água!")

with col3:
    st.header("Exercício")
    st.write("Bom trabalho!" if exercicio != "Nenhum" else "Tente se exercitar mais!")

with st.expander("Veja mais detalhes"):
    st.write("-Durma pelo menos 7 horas")
    st.write("-Beba pelo menos 6 copos de água")
    st.write("-Exercite-se pelo menos 3 vezes por semana")

st.markdown("----")
st.markdown("Projeto com streamlit")