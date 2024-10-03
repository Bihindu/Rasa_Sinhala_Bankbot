import streamlit as st
import requests
import json

# Set page title and icon
st.set_page_config(page_title="Bank Bot", page_icon="🏦")

# Sidebar configuration
with st.sidebar:
    st.title("Chatbot Settings")
    st.info("Configure the behavior of the bank bot here.")

# Title and caption
st.title("Finance Assistant")
st.caption("🚀 A Streamlit chatbot powered by Rasa")

# Store chat messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "ඔබව සාදරයෙන් පිළිගන්නවා මෙම චැට් මෘදුකාංගය මගින් අපි ඔබට අපගේ බැංකු සේවාවන් සහ නිෂ්පාදන පිළිබඳ මාර්ගෝපදේශ සැපයීමට සතුටු වෙමු. ඔබට කිසියම් ගැටලුවක් තිබේ නම් කරුණාකර මට දැනුම් දෙන්න"}]

# Function to interact with Rasa bot
def get_bot_response(user_query):
    url = "http://localhost:5005/webhooks/rest/webhook"  # Use localhost
    payload = {"sender": "user", "message": user_query}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()
    else:
        return []
    
# Display the chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
if prompt := st.chat_input("Your message"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    with st.spinner("Processing..."):
        bot_responses = get_bot_response(prompt)
        bot_reply = " ".join(response.get("text", "") for response in bot_responses)
        if bot_reply:
            st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            st.chat_message("assistant").write(bot_reply)

# Button to clear chat history
if st.sidebar.button("Clear Chat History"):
    st.session_state.messages = [{"role": "assistant", "content": "ඔබව සාදරයෙන් පිළිගන්නවා මෙම චැට් මෘදුකාංගය මගින් අපි ඔබට අපගේ බැංකු සේවාවන් සහ නිෂ්පාදන පිළිබඳ මාර්ගෝපදේශ සැපයීමට සතුටු වෙමු. ඔබට කිසියම් ගැටලුවක් තිබේ නම් කරුණාකර මට දැනුම් දෙන්න"}]
