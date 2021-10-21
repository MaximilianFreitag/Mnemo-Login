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

col1.write('The following URL is the github repo where you can get started setting everything up. (Click the copy to clipboard for an easy copy/paste)')
col1.code('github.com/conradbez/streamlit-auth0')
col1.write('I also found a great stackoverflow thread that explains how you can set up secret keys within python.')
col1.code('stackoverflow.com/questions/40216311/reading-in-environment-variables-from-an-environment-file')
col1.write('Okay, lets test it. You can only see my secret application when \n logging in with google or other services.', use_column_width=True)


with col2:
       
    st.image('1515.jpg', use_column_width=True)



def secret_app():
    def show():
        st.write(
            """
            ## ✅ Secret To-do List 

            If everything went right only you as the logged in user can see the app.
            """
        )

        # Define initial state.
        if "todos" not in st.session_state:
            st.session_state.todos = [
                {"description": "Learn how to create login pages", "done": True},
                {
                    "description": "Read the [blog post about session state](https://blog.streamlit.io/session-state-for-streamlit/)",
                    "done": False,
                },
            ]

        # Define callback when text_input changed.
        def new_todo_changed():
            if st.session_state.new_todo:
                st.session_state.todos.append(
                    {
                        "description": st.session_state.new_todo,
                        "done": False,
                    }
                )

        # Show widgets to add new TODO.
        st.write(
            "<style>.main * div.row-widget.stRadio > div{flex-direction:row;}</style>",
            unsafe_allow_html=True,
        )
        st.text_input("What do you need to do?", on_change=new_todo_changed, key="new_todo")

        # Show all TODOs.
        write_todo_list(st.session_state.todos)


    def write_todo_list(todos):
        "Display the todo list (mostly layout stuff, no state)."
        st.write("")
        all_done = True
        for i, todo in enumerate(todos):
            col1, col2, _ = st.beta_columns([0.05, 0.8, 0.15])
            done = col1.checkbox("", todo["done"], key=str(i))
            if done:
                format_str = (
                    '<span style="color: grey; text-decoration: line-through;">{}</span>'
                )
            else:
                format_str = "{}"
                all_done = False
            col2.markdown(
                format_str.format(todo["description"]),
                unsafe_allow_html=True,
            )

        if all_done:
            st.success("Nice job on finishing all TODO items! Enjoy your day! ")


        
        



with col1:
    
    user_info = login_button(clientId, domain = domain)
    
    if user_info:
        st.write(f'Hi {user_info["nickname"]}')
        # st.write(user_info) # some private information here

        secret_app()

    if not user_info:
        st.write("Let's see if it works.")



