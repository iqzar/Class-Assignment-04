def play():
  user = input("Enter your choice btw r for rock, p for paper, s for scissors: ")
  computer = random.choice(['r','p','s'])

  if user == computer:
    return "Its a tie"

  if is_win(user, computer):
    return "You won"

  return "You lost"

def is_win(player, opponent):

    if(player == 'r' and opponent == 's') or (player == 's' or opponent == 'p') or (player == 'p' or opponent == 'r'):
      return True

print(play())