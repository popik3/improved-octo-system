def count_words(filename):
    try:
        with open(filename, encoding='utf-8')as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")

    else:
        words = content.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filename = 'pg11.txt'
count_words(filename)