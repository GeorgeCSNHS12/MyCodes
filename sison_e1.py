# filename      : sison_e1.py
# author        : George William Sison
# description   : This is a python program that prints contents of a dictionary
#                 in a specific format.

data = { 
        "myName" : "George William M. Sison",
        "mySpiritAnimal" : "Cat",
        "myReason" : "I'm an apathetic person and energy conserver just like a cat",
        "myHobby" : "play MMORPGs and watch Animes",
        "myFutureProfession" : "Software Developer"
}

message = "I am {}.\n" \
        "My spirit animal is {},\n" \
        "because {}.\n" \
        "When not in school, I love to {}.\n" \
        "I dream of being a/an {} in the future."

print(message.format(data["myName"], data["mySpiritAnimal"], data["myReason"], data["myHobby"], data["myFutureProfession"]))
#print("I am {}.".format(data["myName"]), "My spirit animal is {},".format(data["mySpiritAnimal"]), "because {}.".format(data["myReason"]), sep = "\n")
#print("When not in school, I love to {}.".format(data["myHobby"]), "I dream of being a/an {} in the future.".format(data["myFutureProfession"]), sep = "\n")
