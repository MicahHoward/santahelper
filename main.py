from openai import OpenAI

client = OpenAI()

conversation = [
                {"role": "system", "content": "You are a gift idea giving assistant who takes in chacteristics about a recipient and responds with gift ideas in one list without categories or enumeration."},
        ]

while(True):
    user_input = input()      
    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages = conversation
    )

    conversation.append({"role": "assistant", "content": response.choices[0].message.content})
    print("\n" + response.choices[0].message.content + "\n")
