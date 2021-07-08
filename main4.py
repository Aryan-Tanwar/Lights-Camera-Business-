import streamlit as st

def main():

    st.title("Lights, Camera, Business!")
    teams = ["Team 1","Team 2","Team 3","Team 4"]
    teams_choice = st.sidebar.selectbox("Teams",teams)

    if teams_choice == "Team 1":

        st.subheader("Round 1")
        teamp = st.text_input("Type password for round 1 ")
        if teamp == "T1":
            st.subheader("Your Personality")
            st.write("**Vijay Malya**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type password for round 2")
        if password == "123":
            st.subheader("Your Ministry")
            st.write("**Ministry of Defence**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type password for round 3")
        if password2 == "321":
            st.subheader("Your Company")
            st.write("**HAL**")
        else:
            st.write("try again incorrect password")


    elif teams_choice == "Team 2":

        st.subheader("Round 1")
        teamp = st.text_input("Type password for round 1 ")
        if teamp == "T2":
            st.subheader("Your Personality")
            st.write("**Mehul Choksi**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type password for round 2")
        if password == "456":
            st.subheader("Your Ministry")
            st.write("**Ministry of Education**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type password for round 3")
        if password2 == "654":
            st.subheader("Your Company")
            st.write("**Byjus**")
        else:
            st.write("try again incorrect password")


    elif teams_choice == "Team 3":

        st.subheader("Round 1")
        teamp = st.text_input("Type password for round 1 ")
        if teamp == "T3":
            st.subheader("Your Personality")
            st.write("**Nirav Modi**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type password for round 2")
        if password == "789":
            st.subheader("Your Ministry")
            st.write("**Ministry of Steel**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type password for round 3")
        if password2 == "987":
            st.subheader("Your Company")
            st.write("**TATA Steel**")
        else:
            st.write("try again incorrect password")


    elif teams_choice == "Team 4":

        st.subheader("Round 1")
        teamp = st.text_input("Type password for round 1 ")
        if teamp == "T4":
            st.subheader("Your Personality")
            st.write("**Chanda Kochhar**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type password for round 2")
        if password == "91011":
            st.subheader("Your Ministry")
            st.write("**Ministry of Communication**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type password for round 3")
        if password2 == "11109":
            st.subheader("Your Company")
            st.write("**Airtel**")
        else:
            st.write("try again incorrect password")

if __name__ == '__main__':
     main()
