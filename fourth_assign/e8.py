class Player:
    player_count=0
    
    def __init__(self,name,level ):
        self.name=name
        self.level=level
        Player.player_count+=1
    def countt(self):
        print(Player.player_count)

p1=Player("Suyash",12)
print(p1.countt())
