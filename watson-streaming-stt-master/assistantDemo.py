import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
api = "iT9dBR0dCQs6cSNFCcChDJ5qiRlTZEiPJIWxodjPi-uy"
url = "https://api.us-south.assistant.watson.cloud.ibm.com/instances/98ba990f-9761-4e22-8078-2e9cc568b7e6"
authenticator = IAMAuthenticator(api)
assistant = AssistantV2(
    version='2021-06-14',
    authenticator = authenticator
)

assistant.set_service_url(url)
ses = assistant.create_session(
    assistant_id='ca1a5747-8f52-49d3-9b9f-2c7e17ad821e'
).get_result()
response = assistant.message(
    assistant_id='ca1a5747-8f52-49d3-9b9f-2c7e17ad821e',
   session_id=ses['session_id'],
    input={
        'message_type': 'text',
        'text': 'what'
    }
).get_result()
#print(ses['session_id'])
print(response["output"]["generic"][0]["text"])
#print(json.dumps(response, indent=2))