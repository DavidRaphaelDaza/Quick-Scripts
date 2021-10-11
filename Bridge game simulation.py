#Bridge game simulation
import random

N_TILES = 18
N_PLAYERS = 16
N_ROUNDS = 1000000
SHOW_WIN_LOSS = False
RANDOMIZE_BRIDGE = False

class player:
    def __init__(self) -> None:
        self.wins=0
        self.losses=0

    def get_win_rate(self):
        if self.wins+self.losses >0:
            return(self.wins/(self.wins+self.losses))

    def win(self):
        self.wins+=1
    
    def loss(self):
        self.losses+=1

    def move(self):
        if random.random()>.5:
            return "1"
        else:
            return "0"


def create_bridge(n_tiles = N_TILES):
    bridge=""
    for i in range(n_tiles):
        if random.random()>.5:
            bridge=bridge+"1"
        else:
            bridge=bridge+"0"
    return bridge

def main():

    #define player pool
    players=[]
    for i in range(N_PLAYERS):
        players.append(player())

    if not RANDOMIZE_BRIDGE:
        bridge = create_bridge()

    for i in range(N_ROUNDS):
        
        if RANDOMIZE_BRIDGE:
            bridge = create_bridge()
        player_number = 0 

        for j in bridge:
            if j == players[player_number].move():
                pass
            else:
                player_number+=1
                if player_number>N_PLAYERS-1:
                    break
        
        for j in range(player_number):
            players[j].loss()

        for j in range(player_number,N_PLAYERS):
            players[j].win()

    
    print("WIN RATES")
    c=1

    for p in players:
        print("Player "+str(c), end=": ")
        print(p.get_win_rate())
        if SHOW_WIN_LOSS:
            print("WINS: ", p.wins, " | LOSSES: ", p.losses)
        c+=1

if __name__ == "__main__":
    main()

