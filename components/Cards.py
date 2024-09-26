import streamlit as st

def acessos(name:str, user:str, password:str, cor="#f0f0f5"):
    # Criar o card com informações
    st.markdown(f"""
    <div style="border: 1px solid #d3d3d3; border-radius: 5px; padding: 20px; margin: 10px; background-color: {cor};">
        <h2 style="color: #1c83e1;">{name.upper()}</h2>
        <h3 style="color: #333;">Usuário: <span id="user">{user}</span> 
            <i class="fas fa-copy" onclick="copyToClipboard('user')" style="cursor:pointer; color: #007bff;"></i>
        </h3>
        <h3 style="color: #333;">Senha: <span id="senha">{password}</span> 
            <i class="fas fa-copy" onclick="copyToClipboard('senha')" style="cursor:pointer; color: #007bff;"></i>
        </h3>
    </div>

    <script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>
    <script>
    function copyToClipboard(elementId) {{
        var text = document.getElementById(elementId).textContent;
        navigator.clipboard.writeText(text).then(function() {{
            alert('Texto copiado: ' + text);
        }}, function(err) {{
            console.error('Erro ao copiar: ', err);
        }});
    }}
    </script>
    """, unsafe_allow_html=True)
