import numpy as np


#https://phys.org/news/2019-03-key-players-methane.html#:~:text=Regardless%20of%20whether%20methane%20is,break%20this%20gas%20up%20again.
#https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4882646/
#https://byjus.com/neet-questions/are-microvilli-found-in-plant-cells/
#https://machinelearningmastery.com/simple-genetic-algorithm-from-scratch-in-python/

class Cell:
    def __init__(self, pigments, chemo_enzymes, microvili, hs_rate, methane_rate, co2_rate, water_rate, brightness, heat, epochs):
        self.pigments = pigments
        self.chemo_enzymes = chemo_enzymes 
        self.microvili = microvili
        self.hs = 0
        self.methane = 0
        self.co2 = 0
        self.water = 0
        self.light = 0
        self.atp = 0

        self.hs_rate = hs_rate
        self.methane_rate = methane_rate
        self.co2_rate = co2_rate
        self.water_rate = water_rate
        self.brightness = brightness
        self.heat = heat

        self.resources = [self.hs, self.methane, self.co2, self.water, self.light]
        self.rates = [self.hs_rate, self.methane_rate, self.co2_rate, self.water_rate, self.brightness]

        self.epochs = epochs

        self.optimal_p = .35
        self.optimal_c = .65

    def determine_spawn(self, x):
        y = 0

        # mess with spawn its kinda op rn

        if np.random.uniform() < x:
           y += 1
        else:
            y = 0

        return y

    def scaling(self, n):
        a = -30
        h = self.heat
        k = 1

        return np.max([0, a * (h - n) ** 2 + k])
        
        
    def calc_fitness(self):
        for i in range(self.epochs):
            self.resources = [self.determine_spawn(i) for i in self.rates]

            # maybe scale for heat as well?
            # maybe make less bright equal hotter since if its
            # farther from the sun it is close to thermal vent

            for n, i in enumerate(self.resources[0:3]):
                self.resources[n] += self.scaling(self.microvili)

            if self.microvili != 0:
                self.resources[-1] *= 1 / self.microvili
            else:
                self.resources[-1] = 0

            self.atp += self.pigments * (max(0, sum(self.resources[2:]))) * self.scaling(self.optimal_p)
            self.atp += self.chemo_enzymes * (sum(self.resources[0:3])) * self.scaling(self.optimal_c)

            self.atp *= self.scaling(self.optimal_p)
            self.atp *= self.scaling(self.optimal_c)

        return self.atp