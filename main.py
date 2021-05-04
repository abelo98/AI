from TicTacToe import TicTacToe

def Main():

    humanChoice = ''
    aiChoice = ''
    turn = ''

    while 1 :
        humanChoice = input('Select symbol X or O: ').lower()
        if humanChoice == 'x':
            aiChoice = 'o'
            break
        elif humanChoice == 'o':
            aiChoice = 'x'
            break
        print('')
        print('wrong choice')
        print('')

    while 1:
        turn = input('Would you like to play first (y/n): ').lower()
        if turn == 'y':
            turn = 'human'
            break
        elif turn == 'n':
            turn = 'ai'
            break
        print('')
        print('wrong choice')
        print('')

    game = TicTacToe(humanChoice,aiChoice)

    while not game.CheckFinalState() and len(game.GetEmptyCells()) > 0:
        if turn == 'human':
            game.HumanTime()
            turn = 'ai'
        else:
            game.AiTime()
            turn = 'human'

    game.Clear()
    game.Render()

    if game.Winner(-1):
        print('The human wins')
    elif game.Winner(1):
        print('The AI wins')
    else:
        print('tie')

if __name__ == '__main__':
    Main()