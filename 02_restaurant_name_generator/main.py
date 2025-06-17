import streamlit as st
from langchain_helper import generate_menu

def main():
    st.title("Restaurant Name Generator!")
    cusine = st.sidebar.selectbox("Pick a cuisine", ("Indian", "American", "Mexican", "Italian"))

    if cusine:
        response = generate_menu(cusine)
        st.header(response['name'])
        menu_items = response['menu_items'].split(",")
        st.write("** Menu Items **")
        for item in menu_items:
            st.write("-", item)


if __name__ == "__main__":
    main()
