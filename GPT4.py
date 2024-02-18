from openai import OpenAI
from dotenv import dotenv_values

api_key = dotenv_values(".env")

client = OpenAI(
    # This is the default and can be omitted
    api_key=api_key["OPENAI_API_KEY"],
)

# Initialize the conversation with a system message and a user message
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
]

while True:
    # Get a message from the user
    user_message = input("User: ")
    
    # Check if the user typed "exit"
    if user_message.lower() == "exit":
        break

    # Add the user's message to the conversation
    conversation.append({"role": "user", "content": user_message})

    # Generate a response using the conversation history
    response = client.chat.completions.create(
        model="gpt-4",
        messages=conversation
    )

    # Extract the assistant's message from the response
    assistant_message = response.choices[0].message.content

    # Print the assistant's message
    print("Assistant: ", assistant_message)

    # Add the assistant's message to the conversation
    conversation.append({"role": "assistant", "content": assistant_message})

    # Save the conversation to a .txt file in the Chats directory
    filename = "Chats/" + conversation[1]['content'] + ".txt"  # Use the first user message as the filename
    with open(filename, 'w') as f:
        for message in conversation:
            f.write(f"{message['role']}: {message['content']}\n")