# -*- coding: utf-8 -*-
from collections import defaultdict
from GeoBeast import GeoBeast
import unicodedata
import random

class GeoBeastRepository(object):
    def __init__(self, beast_filename='beasts.list'):
            self.loc2beasts = self.load_beasts(beast_filename)

    def load_beasts(self, filename):
        #TODO load regex beasts correctly
        loc2beasts=defaultdict(set)
        with open(filename) as f:
            for line in f:
                if line.strip() == '':
                    continue
                if '#' in line:
                    locations = line.strip()[1:]
                else:
                    for location in locations.split(', '):
                        loc2beasts[location].add(GeoBeast(line))
        return loc2beasts


    def get_possible_beast_spawns(self, formatted_address):
        #2 Chome-4-13 Higashiōi, Shinagawa-ku, Tōkyō-to, Japan
        #4 Chome-12 Higashishinagawa, Shinagawa-ku, Tōkyō-to 140-8687, Japan
        try:
            formatted_address = formatted_address.decode('utf-8')
        except:
            pass

        formatted_address = unicodedata.normalize('NFD', formatted_address)
        formatted_address = formatted_address.encode('ascii', 'ignore')

        print formatted_address
        possible_beasts = set()
        beast_locations = set()
        for adr_part in formatted_address.split(', '):
            for part in adr_part.split(' '):
                if part in self.loc2beasts:
                    beast_locations.add(part)
                    possible_beasts.update(self.loc2beasts[part])

        print 'Possible beasts:', len(possible_beasts)
        print 'Possible from:', ' '.join(beast_locations)
        return possible_beasts

    def get_spawn(self, possible_beasts, no_spawn_chance=0.0):
        no_spawn = 0.01*random.randint(1, 100)
        print 'No Spawn Chance:', no_spawn_chance, ' drew: ', no_spawn
        if no_spawn<=no_spawn_chance:
            return None

        possible_beasts = sorted(possible_beasts, key=lambda x: (-x.probability, x.name))
        total_spawn_probability = sum(mon.probability for mon in possible_beasts)
        random_number =  random.randint(0, total_spawn_probability)
        print 'Total Probability Mass: '+str(total_spawn_probability)+' drew: '+str(random_number)
        print 'Beasts: '+' '.join([mon.name+':'+str(mon.probability) for mon in possible_beasts])
        
        for beast in possible_beasts:
                random_number-=beast.probability
                if random_number<=0:
                    return beast
        assert False

    def get_spawn_for_address(self, address):
        print 'Getting Spawn for address', address
        possible_beasts =  self.get_possible_beast_spawns(address)
        return self.get_spawn(possible_beasts)

    def print_spawn_distribution(self, num_tries):
        spawns = defaultdict(int)
        possible_beasts =  self.get_possible_beast_spawns('Higashiōi, Shinagawa-ku, Tōkyō-to, Japan')
        for i in xrange(num_tries):
            spawn =  self.get_spawn(possible_beasts)
            spawns[str(spawn)]+=1
        print spawns
