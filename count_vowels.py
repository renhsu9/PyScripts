# count total vowels in a word

def count_vowel(word):
    """ count total vowels """
    vowel_count = 0
    for ch in word:
        if ch in "aeiouAEIOU":
            vowel_count += 1
    return vowel_count
def main():
    word = input("Enter a word:")
    total_vowels = count_vowel(word)
    print(word, "has",total_vowels,"vowels.")

main()