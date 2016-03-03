#!/bin/env python

from numpy import random
import pandas as pd

class Generator(object):

    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.people = {'name' : [], 'height' : [], 'city' : []}
        self.cities = {
            'name' : [
                'Berkeley',
                'Denver',
                'Mexico City',
                'Amsterdam',
                'Los Angeles'
            ],
            'height' : [
                52,
                1730,
                2250,
                -2,
                71
            ]
        }

    def output_cities(self, fp_cities):
        pd.DataFrame(self.cities).to_csv(fp_cities, index=False)

    def output_people(self, fp_people):
        self.people['height'] = list(random.normal(1.5, 0.25, 1000))
        for i in range(0, 1000):
            self.people['city'].append(self.cities['name'][random.randint(0, len(self.cities))])
            self.people['name'].append(''.join([self.alphabet[i] for i in random.randint(0, len(self.alphabet), 6)]).title())
        pd.DataFrame(self.people).to_csv(fp_people, index=False)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--fp-cities')
    parser.add_argument('--fp-people')
    args = parser.parse_args()

    generator = Generator()
    if args.fp_cities:
        generator.output_cities(args.fp_cities)
        print("Cities written to {}".format(args.fp_cities))
    if args.fp_people:
        generator.output_people(args.fp_people)
        print("People randomized and written to {}".format(args.fp_people))
