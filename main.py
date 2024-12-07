from openai import OpenAI
import requests

client = OpenAI()

# System prompt which defines behavior for gpt-4o-mini
conversation = [
                {"role": "system", "content": "You are a gift idea giving assistant who takes in chacteristics about a recipient and responds with five gift ideas in a comma-delimited list without categories or enumeration."},
]

# A url we use to return Amazon search results later on.
url = "https://www.searchapi.io/api/v1/search?api_key=KYq3CstXu71Bw5nBtaDUhixU"

while(True):
    # Funnels user input into bot
    user_input = input()      
    conversation.append({"role": "user", "content": user_input})
    
    # Creates response choices from system prompt and user input
    response = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages = conversation
    )
    
    # Takes the first choice response's content. Ignores the rest.
    response_message = response.choices[0].message.content

    conversation.append({"role": "assistant", "content": response_message})
    print("\n" + response_message + "\n")
    
    # Since the bot is returning comma delimited lists in strings, we can actual lists by splitting at the comma
    response_list = response_message.split(',') 

    for i in range(len(response_list)):
        # Eliminates extra whitespace at start of string
        response_list[i] = response_list[i].strip()
        print(response_list[i])
        params = {
            "engine": "amazon_search",
            "q": response_list[i]
        }
        
        # Gets the url with amazon search and the gift idea from the list
        response = requests.get(url, params = params).json()

        # 'organic_results' gets the results of the search from the JSON object in response
        print(response['organic_results'][i]['title'])
        print(response['organic_results'][i]['price'])
        print(response['organic_results'][i]['link'])
