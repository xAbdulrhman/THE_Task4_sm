# just MY NOTe  
{   "S T T"
  "apikey": "z9-Ao8G4QQ6URj2c3rkBnL-0UgNbXXO0XlMxk7Pu5j60",
  "iam_apikey_description": "Auto-generated for key 73f75b6c-22fa-41cb-9532-05026a9809e7",
  "iam_apikey_name": "Auto-generated service credentials",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/4ce47ad923054d1693f19c2e7c4ceafe::serviceid:ServiceId-ffb8316a-282a-49f1-81f5-7e7df35652d7",
  "url": "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/4217f0db-5cb7-4d00-8197-8991422134e6"
}


{   "T T S"

"APIKey": "3OHnFd7yyQnq3xCqDsbXrEFzMTE2-XFcN3mh0qcf5pim"

"URL" "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/63e4a94b-7946-4be9-9fe4-8c05a1516f04"

}

import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('{apikey}')
assistant = AssistantV2(
    version='2021-06-14',
    authenticator = authenticator
)

assistant.set_service_url('{url}')

response = assistant.message(
    assistant_id='{assistant_id}',
    session_id='{session_id}',
    input={
        'message_type': 'text',
        'text': 'Hello'
    }
).get_result()

print(json.dumps(response, indent=2))