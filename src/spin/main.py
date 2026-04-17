import random
import time
from typing import List, Annotated
import spin.popflash as pf
import spin.wheel as won

import typer
from rich.progress import track

app = typer.Typer(help="A popflash helper for rolling out users")


@app.command()
def spin(
        name: Annotated[str, typer.Argument()] = "fragworks",
        spins: Annotated[int, typer.Option(help="Number of users to spin")] = 0,
        wheel: Annotated[bool, typer.Option(help="Use Wheel Of Names Visual Spinner")] = False,
        drop: Annotated[list[str] | None, typer.Option(help="Drop a specific user from the spin list")] = None,
        move: Annotated[bool, typer.Option(help="INACTIVE Moves rolled players from last match to waiting room")] = False
     #   lastMatch: Annottate[]
    ):
    """
    Extract the names from last popflash match.
    """
    playersInLobby = pf.getActivePlayers(name)
    print(playersInLobby)
    lastMatchLink = pf.getLastMatch(name)
    print(lastMatchLink)
    lastMatchPlayerNames = pf.getLastMatchPlayerNames(lastMatchLink)
    print(lastMatchPlayerNames)

    playersToSpinFrom = lastMatchPlayerNames

    if drop:
        for d in drop:
            playersToSpinFrom.pop(d)
    
    if wheel:
        won.populateWheelOfNames(playersToSpinFrom)
    
    if spins and not wheel:
        for spin in range(spins):
            spunUser = random.choice(playersToSpinFrom)
            print(f"Congrats {spunUser}, you have been spun out for the next match")
        total = 0
        for value in track(range(100), description="Spinning and idiot..."):
            #Fake Processing time
            time.sleep(0.01)
            total += 1
        print(f"Processed {total} things.")
        #TODO Hook this up.

    ## TODO check how many players left from the last scrim
    ## TODO check 
    
# pf.closeBrowser()
# won.closeBrowser()

if __name__ == "__main__":
    app()
