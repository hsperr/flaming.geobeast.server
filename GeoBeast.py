class GeoBeast(object):
    def __init__(self, line):
        self.name, self.probability, self.life, self.attack, self.defense = line.strip().split(' ')
        self.probability = int(self.probability)
        self.life = int(self.life)
        self.attack = int(self.attack)
        self.defense = int(self.defense)
    def __str__(self):
        return ':'.join([str(x) for x in (self.name, self.probability,
            self.life, self.attack, self.defense)])
    def __repr__(self):
        return ':'.join([str(x) for x in (self.name, self.probability, self.life, self.attack,
            self.defense)])
