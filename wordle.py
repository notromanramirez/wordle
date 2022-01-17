"""
Created on Sun Jan 16 13:08:34 2022
@author: Roman Ramirez, rr8rk@virginia.edu
"""

# from collections import defaultdict
import random

def color_str(color, s, spacing=0):
    retVal = ''
    
    if color == 'g':
        retVal += Color.GREEN
    elif color == 'y':
        retVal += Color.YELLOW
    elif color == 'r':
        retVal += Color.RED
    else:
        retVal += Color.ENDC
        
    retVal += ' ' * spacing + s + ' ' * spacing + Color.ENDC + ' ' * spacing
    return retVal


        
def txt_to_list():
    valid_words = list()
            
    with open('files/valid_words.txt', 'r') as f:
        for v in f.readlines():
            valid_words.append(v.strip().upper())
            
    valid_guesses = list(valid_words)    
            
    with open('files/valid_guesses.txt', 'r') as f:
        for v in f.readlines():
            valid_guesses.append(v.strip().upper())
            
    return valid_guesses, valid_words

class Color():
    ENDC = '\033[m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    RED = '\033[41m'
        

class Board():

    GREEN = '\U0001F7E9'
    YELLOW = '\U0001F7E8'
    BLACK = '\U00002B1B'

    def __init__(self, answer=None):
        self.valid_guesses, self.valid_words = txt_to_list()
        if answer:
            self.answer = answer.upper()
        else:
            self.answer = self.valid_words[random.randrange(0, len(self.valid_words))]
        self.guesses = list()
        self.guess = None
        self.end_game = False
        
        self.greens = set()
        self.yellows = set()
        self.reds = set()
        
    def turn(self):
        self.guess= ''
        while self.guess not in self.valid_guesses:
            print(f'Turn: {len(self.guesses) + 1}', end='\n')
            self.guess = input('Make a guess: ').upper()
        
        self.guesses.append(self.guess)
        
        print(self.update())
        print(self.print_keyboard())
        
    def play(self):

        title = ['    Wordle!', 'By Roman Ramirez']

        print('-' * max([len(i) for i in title]))
        for line in title:
            print(line)
        print('-' * max([len(i) for i in title]))
        print()
        
        while not self.end_game:
            
            if self.guess == self.answer:
                self.end_game = True
                print(f"The word was {self.answer.lower()}. You win!")
                self.win_screen()
            elif len(self.guesses) == 6:
                self.end_game = True
                print(f"The word was {self.answer.lower()}. You lost!")
            else:
                self.turn()
                
    def print_keyboard(self):
        LETTERS = 'QWERTYUIOP_ASDFGHJKL_ZXCVBNM'
        output = '\n'
        for v in LETTERS:
            
            if v == '_':
                output += '\n'
            elif v in self.greens:
                output += color_str('g', v, spacing=1)
            elif v in self.yellows:
                output += color_str('y', v, spacing=1)
            elif v in self.reds:
                output += color_str('r', v, spacing=1)
            else:
                output += color_str('b', v, spacing=1)
        output += '\n'
                    
        return output
        
    def update(self):
        output = '\n'
        for guess in self.guesses:
            for i, v in enumerate(guess):
                
                if v == self.answer[i]:
                    output += color_str('g', v, spacing=1)
                    self.greens.add(v)
                elif v in self.answer:
                    output += color_str('y', v, spacing=1)
                    self.yellows.add(v)
                else:
                    output += color_str('b', v, spacing=1)
                    self.reds.add(v)
            output += '\n'
                    
        return output[:-2]
    
    def win_screen(self):
        output = '\n' + '-' * 10 + "OUTPUT" + '-' * 10 + '\n\n'
        output += f'Wordle {len(self.guesses)}/6\n\n'
        for guess in self.guesses:
            for i, v in enumerate(guess):
                
                if v == self.answer[i]:
                    output += Board.GREEN
                elif v in self.answer:
                    output += Board.YELLOW
                else:
                    output += Board.BLACK
                    
            output += '\n'
                    
        print(output)
        

def main():
    Board().play()

if __name__=='__main__':
    main()