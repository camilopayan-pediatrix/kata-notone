"""Describe your player and their approach."""

from notone.types import GameState


def name() -> str:
    # Return your player's name here:
    return "Harry Dicerolls"


def emoji() -> str:
    # Insert your player's emoji of choice here:
    return "🤘"


def victory_cry() -> str:
    # Insert your player's victory cry here:
    return "Best roll ever!"


def roll_again(state: GameState) -> bool:
    score_diff = abs(state.scores[0] - state.scores[1])
        
    if state.turn_rolls == 0:
        return True
    
    risk_apetite = 30 + (score_diff/9)
    turn_decay = state.turn_rolls * 10
     
    if risk_apetite - turn_decay < 0:
        return False    
    return True 
