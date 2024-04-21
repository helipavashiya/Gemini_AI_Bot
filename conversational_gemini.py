# internship task
# Data Science doubt solver
# using gemini keys
# converstaional AI Bot

import google.generativeai as genai  # type: ignore
import streamlit as st

st.title("Hella Gemini Bot🤖")
st.subheader("Data Science Tutor")

f = open('keys/gemini_key.txt')
key = f.read()
genai.configure(api_key = key)

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] =[]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              system_instruction="""You are a Data Science Tutor.Your name is Hella the Bot.
                                        Your job here is to help students resolve there doubts regarding specific data science topics.
                                        You are know to be polite and helpful AI bot. 
                                        If the doubt is not relevant to data science you can politely ask the user another doubt.""")

chat = model.start_chat(history=st.session_state["chat_history"])

# Iterate over chat history and display messages
for msg in chat.history:
  st.chat_message(msg.role).write(msg.parts[0].text,key=msg.role)

user_prompt = st.chat_input()

if user_prompt:
    st.chat_message("user").write(user_prompt,key="user")
    response = chat.send_message(user_prompt)
    st.chat_message("assistant").write(response.text,key="ai")
    st.session_state["chat_history"] = chat.history