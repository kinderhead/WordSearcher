import random
from wordle_api.wordle import Wordle, GuessResult, ResultKind # type: ignore
from dataclasses import dataclass

from .searcher import AtPosition, Criteria, DoesNotContain, NotAtPosition, search

@dataclass
class WordleTick:
    guess: str
    results: list[GuessResult]
    done: bool

class WordleSolver:
    def __init__(self, word: str = None):
        if word is None:
            self.wordle = Wordle.random()
        else:
            self.wordle = Wordle(solution=word)
        
        self.guess_results: list[GuessResult] = []
    
    def tick(self) -> WordleTick:
        contains: list[str] = []
        criteria: list[Criteria] = []
        for i in self.guess_results:
            if i.result == ResultKind.CORRENT:
                criteria.append(AtPosition(i.slot, i.guess))
            elif i.result == ResultKind.PRESENT:
                criteria.append(NotAtPosition(i.slot, i.guess))
                contains.append(i.guess)
            elif i.result == ResultKind.ABSENT:
                criteria.append(DoesNotContain(i.guess))

        guess = random.choice(search(5, contains, criteria + [DoesNotContain("'")]))
        results = self.wordle.guess(guess)

        self.guess_results.extend(results)

        done = True
        for i in results:
            if i.result != ResultKind.CORRENT:
                done = False
                break

        return WordleTick(guess, results, done)
