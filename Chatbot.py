from nltk.chat.util import Chat, reflections

pairs = [
    ["My name is (.*)", ["Hello %1, How are you today?"]],
    ["(hi|hello|hey|holla|hola)", ["Hello", "Hey there", "Hi"]],
    ["(.*) in (.*) is fun", ["%1 in %2 is indeed fun"]],
    ["(.*)(location|city) ?", "Tokyo, Japan"],
    ["(.*) created you?", ["I was created by Will from the NLTK library"]],
    ["How is the weather in (.*)", ["The weather in %1 is amazing like always"]],
    ["(.*)help(.*)", ["I can help you"]],
    ["(.*) your name?", ["I'm a chatbot, and my name is PyBot"]],
]

my_dummy_reflections = {"go": "gone", "hello": "hey there"}

chat = Chat(pairs, reflections)
chat.converse()
