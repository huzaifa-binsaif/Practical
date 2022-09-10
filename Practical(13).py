class waifu :
    def __init__(self, init_name, init_age, init_hair_colour):
        self.name = init_name
        self.age = init_age
        self.color = init_hair_colour
        self.friends = []
    def add_friend(self,new_friend):
        if new_friend not in self.friends:
            self.friends.append(new_friend)
def youngest_waifu(waifus):
        youngest = waifus[0]
        youngest_age = waifus[0].age
        for waifu in waifus:
            if waifu.age < youngest_age:
                youngest = waifu
                youngest_age = waifu.age
        return youngest
zero_tsu = waifu('Zero Two', 16 ,'pink')
violet_evergarden = waifu('Violet Evergarden', 14, 'blond')
asuna = waifu('Asuna', 19, 'ginger')
emilia = waifu('Emilia', 19, 'gray')
kaori_miyazono = waifu('Kaori Miyazono', 14, 'blond')
violet_evergarden.add_friend(zero_tsu)
my_waifu = [zero_tsu, violet_evergarden, asuna, emilia, kaori_miyazono]
for friend in violet_evergarden.friends :
    print(friend.name)
print (youngest_waifu(my_waifu).name)
