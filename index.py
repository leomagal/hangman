#import random
#import string
import hangman
import os
from flask import Flask, \
                    request, \
                    render_template, \
                    url_for, \
                    redirect, \
                    flash
                    
                    
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def initialize():
    WORDLIST_FILENAME = "./resources/words.txt"
    wordlist = hangman.loadWords(WORDLIST_FILENAME)
    return redirect(url_for('start_game', wordlist=wordlist))
    
@app.route('/start')
def start_game(wordlist):
    secretWord = hangman.chooseWord(wordlist).lower()
    hangman.hang(secretWord)
    return None

if __name__ == '__main__':
    #app.debug = True
    #app.secret_key = 'MySecretKey'
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT',5000)))