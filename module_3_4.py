def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if (word.lower() in root_word.lower()) or (root_word.lower() in word.lower()):
            same_words.append(word)
    print(same_words)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
