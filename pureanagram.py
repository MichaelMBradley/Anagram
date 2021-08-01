from primes import get_n_primes
from words import get_all

primes = get_n_primes(26)
words = get_all()


def encode_word(string: str) -> int:
    product = 1
    for char in string:
        product *= primes[ord(char.lower()) - ord('a')]
    return product


if __name__ == "__main__":
    print("Enter a word to get its encoding.\n'*' ends execution.")
    while True:
        word = input("> ")
        if word == '*':
            break
        else:
            print(encode_word(word))
