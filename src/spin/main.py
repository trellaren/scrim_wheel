import random
import time
from typing import List, Annotated
import spin.popflash as pf
import spin.wheel as won
import pyttsx3

import typer
from rich.progress import track

app = typer.Typer(help="A popflash helper for rolling out users")


@app.command()
def spin(
        name: Annotated[str, typer.Argument()] = "fragworks",
        spins: Annotated[int, typer.Option(help="Number of users to spin")] = 0,
        wheel: Annotated[bool, typer.Option(help="Use Wheel Of Names Visual Spinner")] = False,
        drop: Annotated[list[str] | None, typer.Option(help="Drop a specific user from the spin list. Can be specified multiple times to drop multiple users, e.g. --drop Alice --drop Bob")] = None,
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
            match = next(
                (p for p in playersToSpinFrom if p.lower() == d.lower()),
                None
            )
            if match:
                playersToSpinFrom.remove(match)
            else:
                print(f"Warning: '{d}' not found in the player list and will be ignored.")
    
    if wheel:
        won.populateWheelOfNames(playersToSpinFrom)
    
    engine = pyttsx3.init()
    if spins and not wheel:
        for spin in range(spins):
            spunUser = random.choice(playersToSpinFrom)
            playersToSpinFrom.remove(spunUser)
            print(f"Congrats {spunUser}, you have been spun out for the next match")
            engine.say(f"Congrats {spunUser}, you have been spun out for the next match")
        total = 0
        
        engine.runAndWait()
        for value in track(range(100), description="Spinning an idiot..."):
            #Fake Processing time
            time.sleep(0.01)
            total += 1
        print(f"Processed {total} things.")
        print(playersToSpinFrom)
        #TODO Hook this up.

    ## TODO check how many players left from the last scrim
    ## TODO check 
    
# pf.closeBrowser()
# won.closeBrowser()

if __name__ == "__main__":
    app()
