class Godzilla:
    def __init__(self, stomach_volume_max=200):
        self.stomach_volume_max = stomach_volume_max

    def eating(self, inc_volume):
        if (inc_volume / self.stomach_volume_max)*100 <= self.stomach_volume_max*0.9:
            return "Godzilla can eat"
        else:
            return "Godzilla not hungry"


new_godzilla = Godzilla()
print(new_godzilla.eating(90))