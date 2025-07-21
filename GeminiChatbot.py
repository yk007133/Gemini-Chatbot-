import google.generativeai as genai
import pyttsx3

API_KEY = "Your_API_KEY"

# Initailize speech engine

engine  =  pyttsx3.init()
engine.setProperty('volume', 1)  # Set the volume level (0.0 to 1.0)
engine.setProperty('rated',175)

# Configure the genai with our Api Key

print
genai.configure(api_key = API_KEY)

# Create a generative model indtance for Google Gemini

model = genai.GenerativeModel("gemini-2.0-flash")

# Let's start a chat session with the model

chat = model.start_chat()

# Let's send a message to the model and print the response

print("\n")
response  = chat.send_message("Hello")
print("ChatBot : ", response.text)
engine.say(response.text)  # Use text-to-speech to speak the response.
engine.runAndWait()  # Wait for the speech to finish.


# Using a while loop to keep the chat going until the user types "exit"

while True:
    user_input = input("You : ")
    print("\n")  # Print a new line for better readability.
    if user_input.lower() == "exit":
        print("Bye-Bye Dear !!!")
        engine.say("Bye-Bye Dear !!!")  
        engine.runAndWait()
        break
    response = chat.send_message(user_input)
    print("ChatBot :", response.text)  # Print the model's response.
    engine.say(response.text)  # Use text-to-speech to speak the response.  
    engine.runAndWait()  # Wait for the speech to finish.




