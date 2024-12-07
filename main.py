from openai import OpenAI
import requests

client = OpenAI()

conversation = [
                {"role": "system", "content": "You are a gift idea giving assistant who takes in chacteristics about a recipient and responds with gift ideas in one comma-delimited list without categories or enumeration."},
]


url = "https://www.searchapi.io/api/v1/search?api_key=KYq3CstXu71Bw5nBtaDUhixU"

while(True):
    user_input = input()      
    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages = conversation
    )
    
    response_message = response.choices[0].message.content

    conversation.append({"role": "assistant", "content": response_message})
    print("\n" + response_message + "\n")
    
    
    response_list = response_message.split(',') 
    for i in range(len(response_list)):
        response_list[i] = response_list[i].strip()
        print(response_list[i])
        
    params = {
        "engine": "amazon_search",
        "q": response_list[0]
    }
    response = requests.get(url, params = params)
    print(response.json()['organic_results'][0]['link'])
