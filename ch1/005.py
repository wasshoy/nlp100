def extract_n_gram(sequence, n: int) -> list:
    return [sequence[i:i + n] for i in range(0, len(sequence) - n + 1)]


if __name__ == "__main__":
    text = "I am an NLPer"
    word_bi_gram = extract_n_gram(text.split(), 2)
    char_bi_gram = extract_n_gram(text.replace(" ", ""), 2)
    print(word_bi_gram)
    print(char_bi_gram)
