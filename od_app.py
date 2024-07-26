import streamlit as st
import requests

def create_chat_session(api_key, external_user_id):
    create_session_url = 'https://api.on-demand.io/chat/v1/sessions'
    create_session_headers = {
        'apikey': api_key
    }
    create_session_body = {
        'pluginIds': [],
        'externalUserId': external_user_id
    }

    response = requests.post(create_session_url, headers=create_session_headers, json=create_session_body)
    response_data = response.json()
    return response_data['data']['id']

def submit_query(api_key, session_id, query):
    submit_query_url = f'https://api.on-demand.io/chat/v1/sessions/{session_id}/query'
    submit_query_headers = {
        'apikey': api_key
    }
    submit_query_body = {
        'endpointId': 'predefined-openai-gpt4o',
        'query': query,
        'pluginIds': ['plugin-1713962163', 'plugin-1716334779'],
        'responseMode': 'sync'
    }

    query_response = requests.post(submit_query_url, headers=submit_query_headers, json=submit_query_body)
    return query_response.json()

def main():
    st.title("On-Demand Agents")
    st.image("https://images.playground.com/eb88196190f54ea2ada0973ae81ebfc3.jpeg")

    # Sidebar for API key and external user ID
    st.sidebar.header("API Configuration")
    api_key = st.sidebar.text_input("Enter API Key", type="password")
    external_user_id = st.sidebar.text_input("Enter External User ID", type = "password")

    if not api_key or not external_user_id:
        st.warning("Please enter your API key and external user ID in the sidebar.")
        return

    # Create session button
    if st.button("Create Chat Session"):
        with st.spinner("Creating chat session..."):
            try:
                session_id = create_chat_session(api_key, external_user_id)
                st.session_state['session_id'] = session_id
                st.success(f"Chat session created successfully. Session ID: {session_id}")
            except Exception as e:
                st.error(f"Error creating chat session: {str(e)}")

    # Query input and submit
    if 'session_id' in st.session_state:
        query = st.text_input("Enter your query")
        if st.button("Submit Query"):
            if query:
                with st.spinner("Submitting query..."):
                    try:
                        response = submit_query(api_key, st.session_state['session_id'], query)
                        st.json(response)
                    except Exception as e:
                        st.error(f"Error submitting query: {str(e)}")
            else:
                st.warning("Please enter a query.")
    else:
        st.info("Create a chat session first before submitting queries.")

if __name__ == "__main__":
    main()
