from chatterbot import ChatBot #chatbot module importeren
from chatterbot.trainers import ChatterBotCorpusTrainer #chatterbotcorpustrainer importeren

chatbot = ChatBot('Chatman') #chatbot een naam geven

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

while True:
    request =  input("You: ")
    if request.strip()!="bye":
        response = chatbot.get_response(request)
        print("Bot: ", response)
        
#input geven aan de chatbot waarop hij reageert
        
    if request.strip()=="bye" or request.strip()=="Bye":
        print("Bot: bye!")
        break

#conversatie met de chatbot stop bij de input "Bye" of "bye"


