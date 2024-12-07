from openai import OpenAI
import requests

client = OpenAI()

# System prompt which defines behavior for gpt-4o-mini
conversation = [
                {"role": "system", "content": "You are a gift idea giving assistant who takes in characteristics about a recipient and responds with five gift ideas in a comma-delimited list without categories or enumeration."},
]

# A url we use to return Amazon search results later on.
url = "https://www.searchapi.io/api/v1/search?api_key=KYq3CstXu71Bw5nBtaDUhixU"

print("Hello! My name is Elfie and I am your gift helper for the holidays! ")
while True:
    # Funnels user input into bot
    user_input = input("Please enter in who you want to get a gift for, and the characteristics of that person. :)\n")
    conversation.append({"role": "user", "content": user_input})
    
    # Creates response choices from system prompt and user input
    response = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages = conversation
    )
    
    # Takes the first choice response's content. Ignores the rest.
    response_message = response.choices[0].message.content

    conversation.append({"role": "assistant", "content": response_message})
    #print("\n" + response_message + "\n")
    
    # Since the bot is returning comma delimited lists in strings, we can actual lists by splitting at the comma
    response_list = response_message.split(',')

    print("Thanks! Here are the gift ideas!\n")

    print("-------------------------------------------------------------------")

    for i in range(len(response_list)):
        # Eliminates extra whitespace at start of string
        response_list[i] = response_list[i].strip()
        print(f"Gift idea {i}. {response_list[i]}\n")
        params = {
            "engine": "amazon_search",
            "q": response_list[i]
        }
        
        # Gets the url with amazon search and the gift idea from the list
        response = requests.get(url, params = params).json()

        print("Here is a product I found that I think best fits the gift idea!\n")
        # 'organic_results' gets the results of the search from the JSON object in response
        print("Name: ", response['organic_results'][i]['title'])
        print("Price", response['organic_results'][i]['price'])
        print("Link", response['organic_results'][i]['link'])
        print()
        print("-------------------------------------------------------------------")

