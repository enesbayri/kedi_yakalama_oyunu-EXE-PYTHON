import play

cat = play.new_text('=^.^=')

@play.when_key_pressed('space', 'enter') # if either the space key or enter key are pressed...
def do(key):
    if key == 'enter':
        cat.words = '=-.-='
    if key == 'space':
        cat.words = '=*_*='

play.start_program()