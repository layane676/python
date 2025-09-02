import streamlit as st 

st.set_page_config(
    page_title="Horas de estudo",
    page_icon="",
    layout="wide"
)

st.title("Painel de  Estudos")
st.subheader("Registre e visualize seus hábitos diários")


st.sidebar.header("Seus hábitos")
horas = st.sidebar.slider("Horas estudadas", 0, 12, 8)
pausas = st.sidebar.slider("Pausas", 0, 10, 5) 
atividades = st.sidebar.selectbox("Tipo de atividade realizada", ["Leitura", "Revisão","Exercícios"])

st.metric("Horas estudadas", f"{horas} horas")
st.metric("Pausas", f"{pausas} pausas")
st.metric("Atividade", atividades)

with st.expander("Resultado"):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Horas estudadas")
        st.write("Você estudou bem!" if horas >= 6 else "Tente estudar mais!")
    with col2:
        st.header("Pausas")
        st.write("Você fez boas pausas!" if pausas >= 4 else "Tente fazer mais pausas!")
    with col3:
        st.header("Atividade realizada")
        st.write(atividades)
    
if horas >= 7 and pausas >= 4 and atividades != "Nenhum":
        st.balloons()
        st.success("Parabéns! Você completou suas metas de estudo.")
with st.expander("Dicas de estudos"):
    st.write("-Durma pelo menos 7 horas")
    st.write("-Beba pelo menos 6 copos de água")
    st.write("-Exercite-se pelo menos 3 vezes por semana")

st.markdown("----")
st.markdown("Projeto de estudos" if horas >= 7 and pausas >= 4 and atividades != "Nenhum" else "Você ainda não completou suas metas de estudo.")