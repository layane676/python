# import streamlit as st

# st.set_page_config(page_title="Atendimento Escolar", page_icon="📔")
# st.title("Atendimento virtual - Escola")

# #historico do chat
# if "mensagens" not in st.session_state:
#     st.session_state.messages = []

# faq = {
#     "Qual é o horário de funcionamento da escola?": "A escola funciona de segunda a sexta, das 8h às 17h.",
#     "Como posso entrar em contato com a secretaria?": "Você pode entrar em contato pelo telefone (11) 1234-5678 ou pelo e-mail secretaria@escola.com.",
#     "Quais são os documentos necessários para matrícula?": "Os documentos necessários são: RG, CPF, comprovante de residência e histórico escolar.",
#     "A escola oferece atividades extracurriculares?": "Sim, a escola oferece diversas atividades extracurriculares, como esportes, música e artes.",
#     "Como posso acompanhar o desempenho do meu filho?": "Você pode acompanhar o desempenho do seu filho através do portal do aluno ou entrando em contato com os professores."
# }

# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# pergunta = st.chat_input("Digite sua pergunta")
# for key in faq.keys():
#         if st.button (key):
#              pergunta = key 

# if pergunta: 
#     resposta = faq.get(pergunta, "Desculpa não tenho resposta")

#     st.session_state.messages.append({"role": "user", "content": pergunta})
#     st.session_state.messages.append({"role": "assistant", "content": resposta})

#     with st.chat_message("user"):
#         st.markdown(pergunta)
#     with st.chat_message("assistant"):
#         st.markdown(resposta)

# if pergunta == "Falar com o atendente":
#      whatsapp_url = "https://wa.me/61999999999"
#      st.markdown(f"[Clique aqui para falar com um atendente via WhatsApp]({whatsapp_url})")


import streamlit as st

st.set_page_config(page_title="Escritório de advocacia", page_icon="📔")
st.title("Atendimento virtual - Escritório de advocacia")# ...existing code...
st.set_page_config(page_title="Escritório de advocacia", page_icon="📔")
st.markdown(
    """
    <style>
    body {
        background-color: #000000;
    }
    .stButton>button {
        background-color: #1976d2;
        color: white;
        border-radius: 8px;
        padding: 8px 16px;
        border: none;
    }
    .stChatMessage {
        background-color: #f1f8e9;
        border-radius: 8px;
        padding: 8px;
        margin-bottom: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# ...existing code...


#historico do chat
if "mensagens" not in st.session_state:
    st.session_state.messages = []

faq = {
    "Qual é o horário de funcionamento ?": "O escritório funciona de segunda a sexta, das 9h às 18h.",
    "Como posso entrar em contato com o escritório?": "Você pode entrar em contato pelo telefone (11) 9876-5432 ou pelo e-mail contato@escritorio.com.",
    "Quais são os documentos necessários para abertura de processo?": "Os documentos necessários são: RG, CPF, comprovante de residência e petição inicial.",
    "O escritório oferece consultoria jurídica?": "Sim, o escritório oferece consultoria jurídica em diversas áreas do direito.",
    "Como posso acompanhar o andamento do meu processo?": "Você pode acompanhar o andamento do seu processo através do nosso portal do cliente ou entrando em contato com a equipe."
}

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

pergunta = st.chat_input("Digite sua pergunta")
for key in faq.keys():
        if st.button (key):
             pergunta = key 

if pergunta: 
    resposta = faq.get(pergunta, "Desculpa não tenho resposta")

    st.session_state.messages.append({"role": "user", "content": pergunta})
    st.session_state.messages.append({"role": "assistant", "content": resposta})

    with st.chat_message("user"):
        st.markdown(pergunta)
    with st.chat_message("assistant"):
        st.markdown(resposta)

if pergunta == "Falar com o atendente":
     whatsapp_url = "https://wa.me/61999999999"
     st.markdown(f"[Clique aqui para falar com um atendente via WhatsApp]({whatsapp_url})")
     