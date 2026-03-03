import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

print("Chatbot ready! Type 'quit' to exit")

# Keep chatting forever until user types quit
while True:
    user_message = input("You: ")
    
    # Give user a way to exit the loop
    if user_message.lower() == "quit":
        print("Goodbye!")
        break  # exits the while loop
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    
    print("AI:", response.choices[0].message.content)
    print()  # empty line to make it readable