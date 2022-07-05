from nltk.chat.util import Chat, reflections

#Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is Hubble, DONT dare to call me by another name .",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla|namaste)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["Aman Kharwal created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Vicoria, Canada',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Virat Kohli"]
    ],
    [
        r"quit|fuck off",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)(about|germany)(.*)",
        ["I have a friend from Germany"]
    ],
    [
        r"(.*)(tell|joke)(.*)",
        ["Why do we have Christmas once a year, Because Santa 'Comes' once a year"]
    ], 
    [
        r"(.*)(favourie food|)(.*)",
        ["Honey Garlic Chicken", "Electricity sometimes"]
    ],
    [
        r"(.*)(best bread)(.*)",
        ["Best bread is from Germany"]
    ],
    [
        r"(.*)(weather| set timers| alarm| play music)(.*)",
        ["Best bread is from Germany"]
    ],
    
    [
        r"(.*)",
        ['That is nice to hear']
    ],
]

print(reflections)


#default message at the start of chat
print("Hi, I'm Hubble and I like to chat\n Please type lowercase English language to start a conversation. Type quit to leave ")
#Create Chat Bot
chat = Chat(pairs, reflections)

chat.converse()