'''
Name: Santiago Jara
Date: 01/18/2024
Sources: ChatGPT
'''

import random

def lj_get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    word = random.choice(words)
    return word

def lj_get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    word = random.choice(words)
    return word

def lj_get_verb(quantity, tense):
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    word = random.choice(words)
    return word

def lj_get_preposition():
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off",
                    "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    return random.choice(prepositions)

def lj_get_prepositional_phrase(quantity):
    preposition = lj_get_preposition()
    determiner = lj_get_determiner(quantity)
    noun = lj_get_noun(quantity)
    prepositional_phrase = f"{preposition} {determiner} {noun}"
    return prepositional_phrase

def lj_make_sentence(quantity, tense):
    determiner = lj_get_determiner(quantity)
    noun = lj_get_noun(quantity)
    verb = lj_get_verb(quantity, tense)
    prepositional_phrase1 = lj_get_prepositional_phrase(quantity)
    prepositional_phrase2 = lj_get_prepositional_phrase(quantity)
    sentence = f"{determiner.capitalize()} {noun} {verb} {prepositional_phrase1} {prepositional_phrase2}."
    return sentence

def main():
    # a. single past
    print(lj_make_sentence(1, "past"))
    # b. single present
    print(lj_make_sentence(1, "present"))
    # c. single future
    print(lj_make_sentence(1, "future"))
    # d. plural past
    print(lj_make_sentence(2, "past"))
    # e. plural present
    print(lj_make_sentence(2, "present"))
    # f. plural future
    print(lj_make_sentence(2, "future"))

if __name__ == "__main__":
    main()
