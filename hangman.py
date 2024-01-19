import PySimpleGUI as sg
import random


def hangman():
    # Wide choice of themes
    themes = ["cars", "pets", "trees", "countries"]

    theme = sg.popup_get_text(
        'Choose a theme', 'Enter one of the themes: ' + ', '.join(themes))

    # Define word list based on the chosen theme
    word_lists = {
        "cars": ["ford", "toyota", "honda", "bmw", "mercedes", "tesla"],
        "pets": ["dog", "cat", "fish", "bird", "hamster", "turtle"],
        "trees": ["oak", "pine", "maple", "cedar", "birch", "redwood"],
        "countries": ["usa", "china", "india", "brazil", "russia", "germany"]
    }

    if theme not in word_lists:
        sg.popup_error('Invalid theme selected. Exiting.')
        return

    word_list = word_lists[theme]
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    display = list("_" * word_length)
    attempts = 6

    layout = [
        [sg.Text('Guess the word:', font=('Times New Roman', 18))],
        [sg.Text(' '.join(display), key='-WORD-',
                 size=(30, 1), font=('Times New Roman', 14))],
        [sg.InputText(size=(15, 2), key='-GUESS-')],
        [sg.Button('Guess', size=(8, 1), button_color=('#FEF9E7', '#7FB3D5')), sg.Button(
            'Exit', size=(10, 1), button_color=('#F9E79F', '#CD6155'))],
        [sg.Text(f'Attempts left: {attempts}',
                 key='-ATTEMPTS-', font=('Times New Roman', 12))]
    ]

    window = sg.Window('Hangman', layout, size=(600, 460))

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Guess':
            guess = values['-GUESS-'].lower()
            if guess in display:
                sg.popup(f'You\'ve already guessed {guess}')
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
            if guess not in chosen_word:
                attempts -= 1
                window['-ATTEMPTS-'].update(f'Attempts left: {attempts}')
            window['-WORD-'].update(' '.join(display))
            if attempts == 0:
                sg.popup(
                    f'Sorry, you ran out of attempts. The word was {chosen_word}.')
                break
            if "_" not in display:
                sg.popup('Congratulations! You\'ve guessed the word.')
                break

    window.close()


hangman()


hangman()
