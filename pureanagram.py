from primes import get_n_primes
from words import get_all

primes = get_n_primes(26)
encodings = {}


def encode_word(string: str) -> int:
    product = 1
    for char in string:
        product *= primes[ord(char.lower()) - ord('a')]
    return product


for word in get_all():
    enc = encode_word(word)
    if enc in encodings.keys():
        encodings[enc].append(word)
    else:
        encodings[enc] = [word]


if __name__ == "__main__":
    print("Enter a word to get its encoding.\n'*' ends execution.")
    while True:
        word = input("> ")
        if word == '*':
            break
        else:
            print(encodings[encode_word(word)])
