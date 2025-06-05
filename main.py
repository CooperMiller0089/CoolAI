from text_utils import count_words, reverse_text

def main():
    text = "Hello world! Codex is amazing."
    print("Original Text:", text)
    print("Word Count:", count_words(text))
    print("Reversed Text:", reverse_text(text))

if __name__ == "__main__":
    main()
