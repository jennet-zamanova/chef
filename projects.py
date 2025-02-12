import streamlit as st 
import os
parser_page = st.Page("pages/6_parser.py", title="Parser", icon=":material/article:")
pg = st.navigation([parser_page])

logo_path = "assets/dishiqlogo.jpeg"
st.set_page_config(page_title="DishIQ", page_icon=logo_path)



pg.run()

# st.sidebar.success("Select a demo above.")

# st.title("Projects")

# Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'Project Type',
#     ('Class', 'Club', 'Research (UROP)')
# )

# if add_selectbox == 'Class':
#     st.subheader('6.104 - Software Design')
