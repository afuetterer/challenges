from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    try:
        with open(DICTIONARY, 'r') as f:
            words = [word.strip() for word in f.readlines()]
    except IOError as e:
        raise e
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_value = 0
    for char in word:
        char_value = LETTER_SCORES.get(char.upper(), 0)
        word_value += char_value
    return word_value

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()
    max_value = 0
    best_word = None
    for word in words:
        word_value = calc_word_value(word)
        if word_value > max_value:
            max_value = word_value
            best_word = word
    return best_word

if __name__ == "__main__":
    pass # run unittests to validate
