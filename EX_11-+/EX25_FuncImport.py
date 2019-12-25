def break_words(stuff):
    """break words"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sort words"""
    return sorted(words)

def print_first_word(words):
    """prints first word after removal"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints last word after removal"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentences):
    """Returns sorted sentence"""
    words = break_words(sentences)
    return sort_words(words)

def print_first_and_last(sentence):
    """prints first and last words of sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_first_word(words)

def print_first_and_last_sorted(sentence):
    """sorts, then prints first and last words"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
