def converter():
    translation_eng_to_morse = {
        'a': '.-', 'k': '-.-', 'u': '..-',
        'b': '-...', 'l': '.-..', 'v': '...-',
        'c': '-.-.', 'm': '--', 'w': '.--',
        'd': '-..', 'n': '-.', 'x': '-..-',
        'e': '.', 'o': '---', 'y': '-.--',
        'f': '..-.', 'p': '.--.', 'z': '--..',
        'g': '--.', 'q': '--.-', 'å': '.--.-',
        'h': '....', 'r': '.-.', 'ä': '.-.-',
        'i': '..', 's': '...', 'ö': '---.',
        'j': '.---', 't': '-'
    }

    translation_morse_to_eng = {value: key for key, value in translation_eng_to_morse.items()}
    
    morse_code = []
    eng_words = []
    user_input = input("Write a message: ").lower()
    
    for char in user_input:
        if char == ' ':
            morse_code.append('   ')  
        elif char in translation_eng_to_morse:
            morse_code.append(translation_eng_to_morse[char] + ' ')
    
    morse_message = ''.join(morse_code)
    print("Morse code:", morse_message)

    words = morse_message.split('   ')  
    
    for word in words:
        morse_chars = word.split()
        eng_word = ''
        for morse_char in morse_chars:
            if morse_char in translation_morse_to_eng:
                eng_word += translation_morse_to_eng[morse_char]
        eng_words.append(eng_word)

    eng_message = ' '.join(eng_words)
    print("English:", eng_message)

converter()
