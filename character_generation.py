
from collections import defaultdict, deque
import random


def makeCharactersChain(file):
    character_list = []
    # Only process utf-8 characters, ignore others
    with open(file,encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip() +' '
            if line != "":
                for character in line:
                    # Not enough data to also consider capitalization, so everything lowercase
                    character_list.append(character.lower())
    return character_list


def build_character_markov(characters, n=2):
    # Store possible next characters for each n-tuple state
    model = defaultdict(list)
    # Max len to keep window constant size
    window = deque(maxlen=n)

    # initialize queue with first n letters
    for character in characters[:n]:
        window.append(character)
    # add next character after n-tuple to markov model, advance window
    for next_character in characters[n:]:
        context = tuple(window)
        model[context].append(next_character)
        window.append(next_character)
    return model

def generate(model, n=2, length=50):
    # Start at a random state
    context = random.choice(list(model.keys()))
    window = deque(context, maxlen=n)
    output = list(context)

    for _ in range(length):
        # Get the next possible letters
        options = model.get(tuple(window))
        # If there are none, it is either a unique sequence occurring only at end or error, so end the generation.
        if not options:
            break
        # Pick a random next character with equal probability (including repeats to weight certain chars)
        next_character = random.choice(options)
        output.append(next_character)
        window.append(next_character)

    return ''.join(output)


# process the all_books.txt from project gutenberg
characters = makeCharactersChain("all_books.txt")
model_order = 5
characters_model = build_character_markov(characters, n=model_order)

generated_letters = generate(characters_model, n=model_order)

for i in range(10):
    print(generate(characters_model, n=model_order, length=50))
    print('\n')

print(generated_letters)


