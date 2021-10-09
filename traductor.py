import requests
from pprint import pprint
 
skey = 'a8a3e891ba0c401abaead8bac1b38182'
##
endpoint = 'https://eastus.api.cognitive.microsoft.com/'
sentiment_url = endpoint + "/translate-cs-ufgt.cognitiveservices.azure.com/"

documents ={
    "documents": 
        {
            "id": "1",
            "language": "es",
            "text": "Sé que estás en el cielo sonriendo, mientras nos observas cuando rezamos por ti."
        }
}
 
_headers = {"Ocp-Apim-Subscription-Key": skey}
_response=requests.post(sentiment_url, headers=_headers, json=documents)
sentimientos = _response.json()
 
pprint(sentimientos)
 
print(sentimientos['documents'])

print(sentimiento['documents'][0]['sentences'][0]['sentiment'])


