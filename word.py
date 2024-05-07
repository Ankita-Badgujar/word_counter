def count_words(text):
    """
    Counts the number of words in the provided text.

    :param text: The input text as a string.
    :return: The number of words in the text as an integer.
    """
    # Split the text into a list of words based on whitespace
    words = text.split()
    
    # Count the number of words (length of the list)
    word_count = len(words)
    
    return word_count

def main():
    """
    Main function to handle user input, word counting, and output.
    """
    # Prompt the user to enter a sentence or paragraph
    text = input("Please enter a sentence or paragraph: ").strip()
    
    # Error handling for empty input
    if not text:
        print("Error: You didn't enter any text.")
        return
    
    # Count the number of words in the provided text
    word_count = count_words(text)
    
    # Display the word count to the console
    print(f"The text contains {word_count} words.")

if __name__ == "__main__":
    main()
