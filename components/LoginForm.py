import streamlit as st
from typing import Callable

class LoginForm:

    def __init__(self, on_submit:Callable,callback:Callable,username_label="Usuário", password_label="Password", title:str|None=None):
        self.payload:dict = {}
        self.username_label = username_label
        self.password_label = password_label
        self.submit = None
        self.title = title
        self.on_sumbit = on_submit
        self.callback = callback
        self.form = st.form("Login", border=True)
        
    def render(self):

        if(self.title):
            self.form.title(self.title, anchor=False)
        self.payload["username"] = self.form.text_input(label=self.username_label,key="username")
        self.payload["password"] = self.form.text_input(label=self.password_label, key="password")
        self.submit = self.form.form_submit_button("Enviar")
        if(self.submit):
            with st.status("Verificando suas credenciais...") as status:
                result = self.on_sumbit(self.payload)
                self.callback(result)




