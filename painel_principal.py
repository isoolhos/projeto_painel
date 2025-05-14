import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Central de Dashboards", layout="wide")

st.write(f"📅 Data: {datetime.today().strftime('%d/%m/%Y')}")

# Menu lateral
opcao = st.sidebar.selectbox(
    "📂 Escolha o painel",
    ["🏠 Home", "🏥 Centro Diagnóstico", "💻 Senhas Pendentes", "📅 Ordem de Compras", "🩺 Acompanhamento de Consultas"]
)

# Página Home
if opcao == "🏠 Home":
    st.title("📊 Central de Dashboards")
    st.markdown("""
    Bem-vindo à Central de Dashboards!

    Aqui está o acesso aos painéis analíticos:
    
    - 🏥 Centro de Diagnóstico  
    - 💻 Senhas Pendentes  
    - 📅 Ordem de Compras  
    - 🩺 Acompanhamento de Consultas  

    Selecione uma das opções no menu lateral para acessar o painel desejado.
    """)

# Centro Diagnóstico
elif opcao == "🏥 Centro Diagnóstico":
    st.title("🏥 Centro Diagnóstico")
    st.write("Painel com dados e informações sobre o Centro Diagnóstico.")

    st.markdown("""
    Este painel contém informações operacionais e estratégicas do Centro Diagnóstico.
    
    Clique no botão abaixo para abrir o painel completo em uma nova aba.
    """)

    st.markdown("[🔗 Abrir Painel do Centro Diagnóstico](http://10.1.1.63:8501)", unsafe_allow_html=True)

# Senhas Pendentes
elif opcao == "💻 Senhas Pendentes":
    st.title("💻 Senhas Pendentes")
    st.write("Painel com informações sobre as Senhas Pendentes.")

    st.markdown("""
    Clique no botão abaixo para abrir o painel completo em uma nova aba.
    """)
    st.markdown("[🔗 Abrir Painel de Senhas Pendentes](http://10.1.1.63:8504)", unsafe_allow_html=True)

# Ordem de Compras
elif opcao == "📅 Ordem de Compras":
    st.title("📅 Ordem de Compras")
    st.write("Painel com informações sobre as Ordens de Compras.")

    st.markdown("""
    Clique no botão abaixo para abrir o painel completo em uma nova aba.
    """)
    st.markdown("[🔗 Abrir Painel de Ordem de Compras](http://10.1.1.63:8502)", unsafe_allow_html=True)

# Acompanhamento de Consultas
elif opcao == "🩺 Acompanhamento de Consultas":
    st.title("🩺 Acompanhamento de Consultas")
    st.write("Painel com informações sobre o acompanhamento de consultas.")

    st.markdown("""
    Clique no botão abaixo para abrir o painel completo em uma nova aba.
    """)
    st.markdown("[🔗 Abrir Painel de Acompanhamento de Consultas](http://10.1.1.63:8503)", unsafe_allow_html=True)
