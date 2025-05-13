import streamlit as st
from datetime import datetime


st.set_page_config(page_title="Central de Dashboards", layout="wide")

st.write(f"📅 Data: {datetime.today().strftime('%d/%m/%Y')}")

# Opção de escolher o painel na barra lateral
opcao = st.sidebar.selectbox("Escolha o painel", ["Home", "Centro Diagnóstico", "Escalas de Atendimento", "Acompanhamento de Consultas"])

# Lógica para exibir o painel correspondente
if opcao == "Home":
    st.title("📊 Central de Dashboards")
    st.markdown("""
    Bem-vindo à Central de Dashboards!

    Aqui está o acesso aos painéis analíticos:
    
    - 🏥 Centro de Diagnóstico  
    - ☎️📠 Escalas de Atendimento  
    - 🩺 Acompanhamento de Consultas  

    Selecione uma das opções no menu lateral para acessar o painel desejado.
    """)

elif opcao == "Centro Diagnóstico":
    st.title("🏥 Centro Diagnóstico")
    st.write("Painel com dados e informações sobre o centro diagnóstico.")
    st.markdown("[Abrir Painel Centro Diagnóstico](http://10.1.1.63:8501)", unsafe_allow_html=True)

elif opcao == "Escalas de Atendimento":
    st.title("☎️📠 Escalas de Atendimento")
    st.write("Painel com informações sobre as escalas de atendimento.")
    st.markdown("[Abrir Escalas de Atendimento](http://10.1.1.63:8502)", unsafe_allow_html=True)

elif opcao == "Acompanhamento de Consultas":
    st.title("🩺 Acompanhamento de Consultas")
    st.write("Painel com informações sobre o acompanhamento de consultas.")
    st.markdown("[Abrir Acompanhamento de Consultas](http://10.1.1.63:8503)", unsafe_allow_html=True)

    opcao = st.sidebar.selectbox(
    "📂 Escolha o painel",
    ["🏠 Home", "🏥 Centro Diagnóstico", "📅 Escalas de Atendimento", "🩺 Acompanhamento de Consultas"]
)


