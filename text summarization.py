import requests

url = "https://textanalysis-text-summarization.p.rapidapi.com/text-summarizer"

payload = '''{
    \"url\": \"http://en.wikipedia.org/wiki/Automatic_summarization\",
    \"text\": \"\",
    \"sentnum\": 8
}'''
headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "b867d9678bmsh2d951fb9f63d77cp171c1cjsn24a285e0276a",
    'x-rapidapi-host': "textanalysis-text-summarization.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
