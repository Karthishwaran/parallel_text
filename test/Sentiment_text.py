from utils.positive_word import positive_words
from utils.negative_word import negative_words
from utils.neutral_word import neutral_words
def score_paragraph(paragraph):

    paragraph_score = 0
    sentences = paragraph.split(".")
    for i,sentence in enumerate(sentences):
        sentence_score = score_sentence(sentence)

        # TODO: replace print with storage
        print(f"Sentence {i} , Score is {sentence_score}")
        paragraph_score += sentence_score
    return paragraph_score

def score_sentence(sentence:str):

    res = 0
    words = sentence.split()
    for i,word in enumerate(words):
        word_score = analyze_word(word)
        # TODO: replace print with storage
        print(f"Word {i} , Score is {word_score}")
        res += word_score
    return res

def analyze_word(word):

    is_positive = positive_check(word)
    is_negative = negative_check(word)
    if is_positive:
        return 1
    if is_negative:
        return - 1
    return 0

def positive_check(word):
    return word in positive_words

def negative_check(word):
    return word in negative_words
