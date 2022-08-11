import wordsearcher
from rich.console import Console
from wordle_api.wordle import ResultKind # type: ignore

wordle = wordsearcher.WordleSolver()

console = Console()

while True:
    res = wordle.tick()

    for i in range(5):
        if res.results[i].result == ResultKind.CORRENT:
            console.print(res.guess[i], end="", style="white on green")
        elif res.results[i].result == ResultKind.PRESENT:
            console.print(res.guess[i], end="", style="white on #FFA500")
        else:
            console.print(res.guess[i], end="")
    print()

    if res.done:
        break
