from controllers.Access import Access
import streamlit as st
from components import Cards


acc = Access()
res  = acc.get()
for card in res.json():
    print(card)
    Cards.acessos(card.get('banco'), card.get('usuario'), card.get('senha'))
    


