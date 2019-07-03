class Leash:
    producer = "Zara"
    length = 0
    mass = 0
    color = "yellow"

    def __init__(self,  producer="Zara", length =120 , mass=90, color="yellow"):
        self.producer = producer
        self.length = length
        self.mass = mass
        self.color = color

    def to_string(self):
        print ("Maded: " + str(self.producer) + " Length: " + str(self.length) + " Mass: " + str(self.mass) + " Color: " + str(self.color))

    @staticmethod
    def print_static_length():
        print(str(Leash.length))

    def __del__(self):
        print 'destruct', self.producer


if name == '__main__':
    zara = Leash()
    zara.to_string()