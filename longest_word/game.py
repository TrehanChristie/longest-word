import random
import string
import enchant

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = random.choices(string.ascii_letters.upper(),k=9)
        # return self.grid

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        # self.word = word
        eng_dictionary = enchant.Dict("en_US")
        len_word = len(word)
        sorted_word = sorted(word)
        sorted_grid = ''.join(sorted(self.grid))
        return True if eng_dictionary.check(word) and sorted_word == sorted_grid[:len_word+1] else False
        # and self.sorted(word) == self.sorted(grid)


if __name__ == "__main__":
    game = Game()
    print(game.grid)
    print(game.is_valid(word = "four"))
    # print(test)
