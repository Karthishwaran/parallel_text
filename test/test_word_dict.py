from utils.positive_words import positive_words
from utils.negative_words import negative_words
from utils.neutral import neutral_words

sample_sentences = [
    "The concert was lively, but the seating was uncomfortable, and the snacks were overpriced.",
    "She nailed the interview; her confidence showed, although some answers were a bit vague.",
    "The coffee tasted excellent, but the music was too loud and the chairs were wobbly.",
    "I tried a new pizza place—it was decent, but the crust was too thick for my liking.",
    "The hike was refreshing, yet it started raining halfway and we had to turn back.",
    "He aced the coding test, although his explanations weren’t very clear.",
    "The festival was crowded, the food was mediocre, but the performances were superb.",
    "I ordered a burger, but got a salad instead; the server apologized and fixed it quickly.",
    "The book was interesting, but the ending felt rushed and unsatisfying.",
    "I went shopping for shoes and ended up buying a jacket instead.",
    "The teacher was enthusiastic, but the lesson moved too fast for most students.",
    "My phone battery died, but at least I got a picture of the sunset before it happened.",
    "The team played well, but missed several easy chances and lost the match.",
    "The dessert was delicious and beautifully presented, even though the main course was a disappointment.",
    "She learned a lot from the workshop, but wished it had lasted longer.",
    "He argued his point skillfully, but some evidence was lacking.",
    "The garden looked beautiful after the rain, but the bugs were everywhere.",
    "I felt relieved after submitting my assignment, despite being nervous at first.",
    "The movie had great special effects, but the plot was predictable and boring.",
    "The week started badly, but things improved after Wednesday and ended on a high note."
]

def positive_check(word):
    return word in positive_words


def negative_check(word):
    return word in negative_words


def neutral_check(word):
    return word in neutral_words

for sentence in sample_sentences:
    words = sentence.split()
    for test_word in words:
        is_positive = positive_check(test_word)
        is_negative = negative_check(test_word)
        is_neutral = neutral_check(test_word)
        print(test_word)
        print(f'\t is positive = {is_positive}')
        print(f'\t is negative = {is_negative}')
        print(f'\t is neutral = {is_neutral}')
