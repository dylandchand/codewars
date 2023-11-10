'''
Let's play! You have to return which player won! In case of a draw return Draw!.
'''

def rps(p1, p2):
    # Define rules of Rock-Paper-Scissors.
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    
    # Apply logic to p1, p2
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"