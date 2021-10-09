import requests
from pprint import pprint
 
skey = '80f6c7351ed248adbee8201987b423ef'
endpoint = 'https://westus.api.cognitive.microsoft.com/'
sentiment_url = endpoint + "/text/analytics/v3.0/sentiment"

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


