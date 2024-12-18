# Presentation Link:

https://drive.google.com/file/d/1tyP1YS1FjF9CtMoa56VMw_Mvic5E15FK/view?usp=sharing

# Author information:

This software was written by Elise Reynolds, Micah Howard, and Brevin Tating and interfaces with GPT-4o mini, a creation of OpenAI.

# License information:

This software is released under GNU General Public License v3.0, which is included in the file 'LICENSE'.

# User Manual:

Dependencies:
openai, requests

Santa Helper is an interface to ChatGPT 4omini that exists to help the Santa in each of us, as we prepare for the holiday season. Our problem is to find interesting and relevant gift ideas based off of user provided information about a recipients demographics, interests, and hobbies. Calling ChatGPT itself to perform this fails in that it does not adequately create a personality that it is giving to, and thus gives bad gift ideas.

In order for Santa Helper to work on your local machine, you must have an OpenAI API key defined as an enviorment variable 'OPENAI_API_KEY' and a SearchAPI API key defined in the enviorment variable 'SEARCHAPI_API_KEY'. This is necessary to keep your API keys on your machine and not on the internet. See https://www.immersivelimit.com/tutorials/adding-your-openai-api-key-to-system-environment-variables if you are having trouble with the API keys,

The dependencies must be installed locally on your computer before you can run the script. We recommend you use a python virtual enviorment and use pip to install them. See https://www.geeksforgeeks.org/python-pip/ if you are having trouble with pip and https://docs.python.org/3/library/venv.html if you are having trouble managing virtual enviorments.

Once the dependencies are installed and the API keys are in the enviorment variables, all you need to do is run main.py (Enter 'python main.py' or python3 main.py into your console), and then enter information about your gift recipient. To exit the program, enter in 'exit'.

# Success Criteria

Our success criteria is that Santa Helper should be able to take information about a gift recipient (age, gender, hobbies, interests, and shared experiences) and respond with gift ideas that are relevant, fun, and thoughtful, so as to inspire the user Santa to give the best gifts possible.

Evaluated by ChatGPT on a scale from 0-10, our program got a 7.8.

# Citations:

https://www.searchapi.io/docs/amazon-search
https://www.geeksforgeeks.org/openai-python-api/
