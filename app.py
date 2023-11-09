import json
import streamlit as st
import requests

st.title("Lablab.ai customer support")

search_term = st.text_input("How may I help you ?", value="",placeholder='Ask your query here')

chat_history = st.session_state.get("chat_history", [])

if st.button("Search"):
    try:
        if search_term:
            url = "https://api.vectara.io:443/v1/query"
            headers = {
                "x-api-key": 'zqt_xHGhmS1ZgQXJWm4ITnxRrMcyGoWckYtfT8oaSA',
                "customer-id": '3295781273'}
    
            payload = {
                "query": [
                    {
                    "query": search_term,
                    "queryContext": "",
                    "start": 0,
                    "numResults": 10,
                    "contextConfig": {
                        "charsBefore": 0,
                        "charsAfter": 0,
                        "sentencesBefore": 2,
                        "sentencesAfter": 2,
                        "startTag": "%START_SNIPPET%",
                        "endTag": "%END_SNIPPET%"
                    },
                    "corpusKey": [
                        {
                            "customerId": '3295781273',
                            "corpusId": '1',
                            "semantics": 0,
                            "metadataFilter": "",
                                "lexicalInterpolationConfig": {
                            "lambda": 0.025
                            },
                            "dim": []
                        }
                    ],
                    "summary": [
                        {
                            "maxSummarizedResults": 2,
                            "responseLang": "eng",
                            "summarizerPromptName": "vectara-summary-ext-v1.2.0"
                        }
                    ]
                }
            ]
        }
    
        response = requests.post(url, headers=headers, json=payload)
        search_results = json.loads(response.text)
        summary = search_results["responseSet"][0]["summary"][0]["text"]
        st.write(summary)
        chat_history.append(f"**You:** {search_term}")
        chat_history.append(f"**Bot:** {summary}")
        chat_history.append("---------------------------------------------")
                
    except:
        error_message = "enter the query first"
        st.text(error_message)
        chat_history.append(f"**You:** {search_term}")
        chat_history.append(f"**Bot:** {error_message}")
        chat_history.append("---------------------------------------------")
        
st.sidebar.title("Chat History")
chat_history_markdown = "\n\n".join(chat_history)
st.sidebar.markdown(chat_history_markdown)

st.session_state.chat_history = chat_history

