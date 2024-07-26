import requests

# Replace with your actual API key and external user ID
api_key = 'xxx'
external_user_id = 'xxx'

# Create Chat Session
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

# Extract session ID from the response
session_id = response_data['data']['id']

# Submit Query
submit_query_url = f'https://api.on-demand.io/chat/v1/sessions/{session_id}/query'
submit_query_headers = {
    'apikey': api_key
}
submit_query_body = {
    'endpointId': 'predefined-openai-gpt4o',
    'query': 'List 3 male blue shirts from Amazon India',
    'pluginIds': ['plugin-1713962163', 'plugin-1716334779'],
    'responseMode': 'sync'
}

query_response = requests.post(submit_query_url, headers=submit_query_headers, json=submit_query_body)
query_response_data = query_response.json()

# Print the response from the query
print(query_response_data)
