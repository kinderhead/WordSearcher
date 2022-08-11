from english_words import english_words_lower_set # type: ignore
from abc import ABC, abstractmethod

class Criteria(ABC):
    @abstractmethod
    def valid(self, word: str) -> bool:
        pass

class AtPosition(Criteria):
    def __init__(self, pos: int, c: str):
        if len(c) != 1:
            raise ValueError("c must be a single character")
        
        self.pos = pos
        self.c = c
    
    def valid(self, word: str) -> bool:
        return word[self.pos] == self.c

class NotAtPosition(AtPosition): 
    def valid(self, word: str) -> bool:
        return not super().valid(word)

class DoesNotContain(Criteria):
    def __init__(self, c: str):
        self.c = c
    
    def valid(self, word: str) -> bool:
        return self.c not in word

def search(length: int = None, contains: list[str] = [], criteria: list[Criteria] = []) -> list[str]:
    results: list[str] = []

    for i in english_words_lower_set:
        if length is not None and len(i) != length:
            continue

        c = True
        for e in contains:
            if e not in i:
                c = False
                break
        if not c:
            continue
        for x in criteria:
            if not x.valid(i):
                c = False
                break
        if not c:
            continue

        results.append(i)

    return results
