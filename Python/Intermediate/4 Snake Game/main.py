class One:
    def __init__(self):
        self.camel="back"
    def gun(self):
        print("shoot")
class Two:
    def __intit__(self):
        self.dog="tail"
class Three(One):
    def __init__(self):
        super().__init__()
    def canon(self):
        super().gun()
        print("fire")

lol=Three()
print(lol.camel)
lol.canon()