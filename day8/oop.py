class House:
    window=10
    color="red"
    door=3
    def __init__(self,window=10,color='pink',door=4):
        self.window=window
        self.color=color 
        self.door=door
        print('I was call first')
    def ghar(self):
        color ="green"
        print('mero ghar ko color',self.color)
    def set_color(self, color):
        self.color=color
# ram_house = House()
# print(ram_house.color)

# hari = House()
# print(hari.color)
# hari.color="green"
# print(hari.color)

# Gita = House()
# Gita.color="pink"
# print(Gita.color)


bipana = House()
bipana.set_color("yellow")
print(bipana.color)
bipana.ghar()