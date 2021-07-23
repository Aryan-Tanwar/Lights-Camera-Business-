import streamlit as st

def main():

    st.title("Lights, Camera, Business!")
    teams = ["Team A","Team B","Team C","Team D","Team E","Team F","Team G","Team H"]
    teams_choice = st.sidebar.selectbox("Teams",teams)

    if teams_choice == "Team A":

        st.header("Team A")
        st.subheader("Round 1")
        teamp = st.text_input("Type password for round 1 ")
        if teamp == "23056":
            st.subheader("Your Personality")
            st.write("**Mehul Choksi**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type password for round 2")
        if password == "49743":
            st.subheader("Your Ministry")
            st.write("**Ministry of Electronics and IT**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type password for round 3")
        if password2 == "24957":
            st.subheader("Your Company")
            st.write("**Infosys**")
        else:
            st.write("try again incorrect password")


    elif teams_choice == "Team B":

        st.header("Team B")
        st.subheader("Round 1")
        teamp = st.text_input("Type password for round 1 ")
        if teamp == "35943":
            st.subheader("Your Personality")
            st.write("**Vijay Mallya**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type password for round 2")
        if password == "29569":
            st.subheader("Your Ministry")
            st.write("**Ministry of Agriculture**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type password for round 3")
        if password2 == "49679":
            st.subheader("Your Company")
            st.write("**Bajaj finance**")
        else:
            st.write("try again incorrect password")


    elif teams_choice == "Team C":

        st.header("Team C")
        st.subheader("Round 1")
        teamp = st.text_input("Type password for round 1 ")
        if teamp == "85062":
            st.subheader("Your Personality")
            st.write("**Chanda Kochar**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type password for round 2")
        if password == "23952":
            st.subheader("Your Ministry")
            st.write("**Ministry of Electronics and IT**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type password for round 3")
        if password2 == "94527":
            st.subheader("Your Company")
            st.write("**Reliance Enterprises**")
        else:
            st.write("try again incorrect password")


    elif teams_choice == "Team D":

        st.header("Team D")
        st.subheader("Round 1")
        teamp = st.text_input("Type password for round 1 ")
        if teamp == "94572":
            st.subheader("Your Personality")
            st.write("**Ramalinga Raju**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type password for round 2")
        if password == "29749":
            st.subheader("Your Ministry")
            st.write("**Ministry of Finance**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type password for round 3")
        if password2 == "97457":
            st.subheader("Your Company")
            st.write("**Airtel**")
        else:
            st.write("try again incorrect password")


    elif teams_choice == "Team E":

        st.header("Team E")
        st.subheader("Round 1")
        teamp = st.text_input("Type password for round 1 ")
        if teamp == "38234":
            st.subheader("Your Personality")
            st.write("**Subrata Roy**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type password for round 2")
        if password == "86840":
            st.subheader("Your Ministry")
            st.write("**Ministry of Commerce and industry**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type password for round 3")
        if password2 == "56935":
            st.subheader("Your Company")
            st.write("**Airtel**")
        else:
            st.write("try again incorrect password")


    elif teams_choice == "Team F":

        st.header("Team F")
        st.subheader("Round 1")
        teamp = st.text_input("Type password for round 1 ")
        if teamp == "44848":
            st.subheader("Your Personality")
            st.write("**Anil Ambani**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type password for round 2")
        if password == "78790":
            st.subheader("Your Ministry")
            st.write("**Ministry of Defence**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type password for round 3")
        if password2 == "47747":
            st.subheader("Your Company")
            st.write("**Airtel**")
        else:
            st.write("try again incorrect password")


    elif teams_choice == "Team G":

        st.header("Team G")
        st.subheader("Round 1")
        teamp = st.text_input("Type password for round 1 ")
        if teamp == "56959":
            st.subheader("Your Personality")
            st.write("**Sanjay Bhandari**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type password for round 2")
        if password == "47775":
            st.subheader("Your Ministry")
            st.write("**Ministry of Education**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type password for round 3")
        if password2 == "68868":
            st.subheader("Your Company")
            st.write("**Airtel**")
        else:
            st.write("try again incorrect password")


    elif teams_choice == "Team H":

        st.header("Team H")
        st.subheader("Round 1")
        teamp = st.text_input("Type password for round 1 ")
        if teamp == "56886":
            st.subheader("Your Personality")
            st.write("**Usha Ananthasubramanian**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type password for round 2")
        if password == "85853":
            st.subheader("Your Ministry")
            st.write("**Ministry of Finance**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type password for round 3")
        if password2 == "59993":
            st.subheader("Your Company")
            st.write("**Airtel**")
        else:
            st.write("try again incorrect password")


if __name__ == '__main__':
     main()
