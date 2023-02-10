import streamlit as st
import psycopg2

cuisine='text'
conn = psycopg2.connect(
    host="65.108.32.173",
    database="postgres",
    user="postgres",
    password=st.secrets['section']["db_password"]
)

def update_db(name,twitter,thezos,cuisine,teia):
    with conn:
            cur = conn.cursor()
            cur.execute(f"INSERT INTO workshop (name,twitter,thezos,cuisine,teia) VALUES (%s, %s, %s, %s, %s)", (name,twitter,thezos,cuisine,teia))
            cur.close()


def main():
    if ('name' not in st.session_state) & ('country' not in st.session_state):
        username_form()


def success():
    update_db(st.session_state.name,st.session_state.twitter, st.session_state.thezos,cuisine, st.session_state.teia)
    st.success(f'Amazing {st.session_state.name}! You are now a member of the NFT community! Check others work on the "Explore" page!')
    st.balloons()




def username_form():
    with st.form(key="test"):

        st.header('Fill in the information about your first NFT')
        name = st.text_input('Input your name', key="name")

        twitter = st.text_input('Input link to your Twitter account', key="twitter")
        thezos = st.text_input('Input link to your Tezos profile', key="thezos")
        teia = st.text_input('Input link to your NFT on Teia', key="teia")





        st.form_submit_button("Submit", on_click=success)

if __name__ == "__main__":
    main()
