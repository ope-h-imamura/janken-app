import streamlit as st
import random
 
st.title("じゃんけんゲーム")
st.write("コンピュータとじゃんけんをしよう！")
st.sidebar.write("バージョン: 1.0.0")
 
hands = {"グー": "✊", "チョキ": "✌️", "パー": "🖐️"}
user_choice = st.selectbox("あなたの手を選んでください", list(hands.keys()))
 
if st.button("じゃんけん！"):
    computer_choice = random.choice(list(hands.keys()))
    st.write(f"あなた: {hands[user_choice]} {user_choice}")
    st.write(f"コンピュータ: {hands[computer_choice]} {computer_choice}")
 
    if user_choice == computer_choice:
        st.warning("引き分け！")
    elif (user_choice == "グー" and computer_choice == "チョキ") or \
         (user_choice == "チョキ" and computer_choice == "パー") or \
         (user_choice == "パー" and computer_choice == "グー"):
        st.success("あなたの勝ち！")
    else:
        st.error("コンピュータの勝ち...!!")
