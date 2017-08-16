"""
CP1404 Practical Extension
Gopher Population Simulator
Simulate the population of gophers over a 10 year period and display each years population size
"""

import random


def main():
    """Population calculation program"""
    population = 1000  # initial population
    birth_lower = 100  # 10%
    birth_upper = 200  # 20%
    death_lower = 50  # 5%
    death_upper = 250  # 25%
    year = 10  # number of years
    year_count = 0
    dead = 0
    born = 0
    print("Welcome to the Gopher Population Simulator!")
    print("Starting population: {}".format(population))
    for number in range(year):
        dead = calculate_deaths(population, death_lower, death_upper)
        born = calculate_births(population, birth_lower, birth_upper)
        year_count += 1
        print("Year {}".format(year))
        print("*****")
        print("{} gophers were born. {} died".format(born, dead))
        print("Population: {}".format(population))


def calculate_deaths(population, lower, upper):
    """calculate the amount of deaths based on a random value"""
    percent_dead = random.randrange(lower, upper)
    dead = population - percent_dead
    return dead


def calculate_births(population, lower, upper):
    """calculate the amount of births based on a random value"""
    percent_born = random.randrange(lower, upper)
    born = population + percent_born
    return born


main()
