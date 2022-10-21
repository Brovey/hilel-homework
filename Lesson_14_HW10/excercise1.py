class Godzilla:
    def __init__(self, stomach_volume=0, stomach_volume_max=200):
        self.stomach_volume_max = stomach_volume_max
        self.stomach_volume = stomach_volume

    def eating(self, inc_volume):
        if self.stomach_volume + inc_volume <= self.stomach_volume_max*0.9:
            self.stomach_volume += inc_volume
            print(self.stomach_volume)
        elif inc_volume > self.stomach_volume_max:
            print(f"Godzilla cant eat more then {self.stomach_volume_max} kg")

        elif self.stomach_volume >= self.stomach_volume_max*0.9:
            print("Godzilla can't eat anymore")


new_godzilla = Godzilla()
