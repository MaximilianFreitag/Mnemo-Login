import streamlit as st
from auth0_component import login_button
import os
from dotenv import load_dotenv


st.set_page_config(
        page_title='Mnemo Login',
        page_icon="🔒"
        )



load_dotenv()
clientId = os.getenv('clientId')
domain = os.getenv('domain')




st.title('Building a login page with Auth0')
st.write('\n')
st.write('\n')


col1, col2 = st.columns(2)

col1.header('')

col1.write('The following URL is the github repo where you can get started setting everything up.')

col1.code('github.com/conradbez/streamlit-auth0')

col1.write('You can only see my secret application when \n logging in with google or other services.', use_column_width=True)



with col2:
       
    st.image('1515.jpg', use_column_width=True)



with col1:
    
    user_info = login_button(clientId, domain = domain)
    
    if user_info:
        st.write(f'Hi {user_info["nickname"]}')
        # st.write(user_info) # some private information here


    if not user_info:
        st.write("Let's see if it works.")