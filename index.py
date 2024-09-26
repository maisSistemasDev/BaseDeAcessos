import streamlit as st
from styles import SideBar, LoginForm, Body
from styles.BaseStyles import CSS, BaseStyles
from controllers.Auth import Session


session = Session()

def loginPage():
    
    #Styles
    view = LoginForm.AppView()
    submit = LoginForm.SubmitButton()
    container = LoginForm.Box()
    container_ext = LoginForm.Box2()
    container.css = CSS({'max-width':'500px !important',
                         'text-align':'center', 
                         'background':'#31333f !important'})
    h1 = BaseStyles()
    h1.target = 'h1'
    h1.css.props('color','#FFD700')
    h1.css.props('font-weight',"400")
    h1.set_style()
    
    p = BaseStyles()
    p.target = '.st-emotion-cache-jkfxgf'
    p.css.props('color','#fff')
    p.set_style()
    
    container.set_style()
    
    container_ext.css = CSS({'display':'flex','align-items':'center'})
    container_ext.set_style()
    
    submit.container.css = CSS({'display':'flex !important', 'justify-content':'center !important'}) 
    submit.css = CSS({'background':'#4a1ca6 !important', 'color':'#fff !important', 'border-color':'#fff !important'})
    submit.set_style()
    submit.target += ':hover'
    submit.css = CSS({'background':'#694ea0 !important', 'color':'#fff !important', 'border-color':'#fff !important'})
    submit.set_style()
    ##
    
    login = st.Page("./pages/page_login.py", default=True)

    pg = st.navigation([login],position='hidden')

    pg.run()


if(not session.token):
    loginPage()
else:
    acessos = st.Page("./pages/acessos.py", default=True)
    pg = st.navigation([acessos],position='hidden')
    pg.run()


