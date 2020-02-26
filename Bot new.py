from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?", ]
    ],
    [
        r"fine",
        ["Ok, How can I help you ?", ]
    ],
    [
        r"what is your name ?",
        ["My name is Lemniscate and I'm a chatbot", ]
    ],
    [
        r"Hi how are you|how are you ?",
        ["I'm doing good How about You", ]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind", ]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "Alright :)", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude Seriously you are asking me this?", ]

    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse", ]

    ],
    [
        r"(.*) created ?",
        ["Gopi sahane created me using Python's NLTK library ", "top secret ;)", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Hyderabad, Telangana', ]
    ],
    [
       r"thank you|thanks|thnk u|thank you Lemniscate|thnks",
       ["it's my pleasure to assist you (.*)", ]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always", "Too hot man here in %1", "Too cold man here in %1",
         "Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.", ]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2", "Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ", ]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football", ]
    ],
    [
        r"who is your fav. (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"quit|bye",
        ["BBye take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
]


def Lemniscate():
    print(
        "Hi, I'm Lemniscate and I chat alot ;) Please type lowercase English language to start a conversation. Type quit to leave ")  # default message at the start


chat = Chat(pairs, reflections)
chat.converse()
if __name__ == "__main__":
    Lemniscate()