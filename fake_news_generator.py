import random

subjects = [
    "Local politician",
    "Bengaluru startup",
    "Village head",
    "Bollywood actor",
    "Indian scientist",
    "School principal",
    "Auto-rickshaw driver",
    "Temple priest",
    "Cricket team captain",
    "Retired postman"
]

actions = [
    " announces free WiFi for cows",
    " launches app to detect samosa crispiness",
    " declares Monday a 'national pajama day'",
    " trains parrots to deliver weather reports",
    " bans honking after sunset",
    " starts coconut bowling league",
    " introduces chai breaks every 15 minutes",
    " builds world's largest jalebi",
    " opens floating vegetable market",
    " creates perfume that smells like rain"
]

places_or_things = [
    " in a remote Kerala village",
    " inside a Mumbai local train",
    " at the Kumbh Mela",
    " on the rooftop of a Delhi mall",
    " during the IPL opening ceremony",
    " inside a Chennai tea shop",
    " on the banks of the Ganga",
    " in the middle of Jaipur's Pink City",
    " at an abandoned cinema hall",
    " inside a luxury sleeper bus"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places_or_things)
    
    headline = f"BREAKING NEWS: {subject}{action}{place}"
    print("\n" + headline)
    
    user_input = input("\nDo you want to generate another headline? (yes/no) ").strip().lower()
    if user_input == "no":
        break

print("\nThanks for using the Fake News Headline Generator. Have a fun day!")

        