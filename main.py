from solutions.aoc_1 import increase, window_function
from solutions.aoc_10 import syntax_1, syntax_2
from solutions.aoc_11 import Octopus_1, Octopus_2
from solutions.aoc_12 import paths_1, paths_2
from solutions.aoc_13 import origami_1, origami_2
from solutions.aoc_14 import polymerization_1, polymerization_2
from solutions.aoc_15 import chiton_1, chiton_2
from solutions.aoc_16 import star_1, star_2
from solutions.aoc_2 import submarine, submarine_with_aim
from solutions.aoc_3 import calc_power_rate, search
from solutions.aoc_4 import bingo_1, bingo_2
from solutions.aoc_5 import vents_1, vents_2
from solutions.aoc_6 import lanternfish
from solutions.aoc_7 import crabs_1, crabs_2
from solutions.aoc_8 import segment_1, segment_2
from solutions.aoc_9 import basins_1, basins_2


def read_in(filename):
    return open(filename).read().splitlines()


# input_ = list(map(int, read_in('inputs/1.txt')))
# print('Problem 1 A: ' + str(increase(input_)))
# print('Problem 1 B: ' + str(window_function(input_)))
#
# input_ =  list(read_in('inputs/2.txt'))
# print('Problem 2 A: ' + str(submarine(input_)))
# print('Problem 2 B: ' + str(submarine_with_aim(input_)))
#
# input_ = list(read_in('inputs/3.txt'))
# print('Problem 3 A: ' + str(calc_power_rate(input_)))
# print('Problem 3 B: ' + str(search(input_)))
#
# input_ = list(read_in('inputs/4.txt'))
# print('Problem 4 A: ' + str(bingo_1(input_)))
# print('Problem 4 B: ' + str(bingo_2(input_)))
#
# input_ = list(read_in('inputs/5.txt'))
# print('Problem 5 A: ' + str(vents_1(input_)))
# print('Problem 5 B: ' + str(vents_2(input_)))
#
# input_ = list(read_in('inputs/6.txt'))
# print('Problem 6 A: ' + str(lanternfish(input_, 80)))
# print('Problem 6 B: ' + str(lanternfish(input_, 256)))
#
#
# input_ = list(read_in('inputs/7.txt'))
# sample = list(read_in('inputs/sample_7.txt'))
# print('Problem 7 A Sample: ' + str(crabs_1(sample)))
# print('Problem 7 A: ' + str(crabs_1(input_)))
# print('Problem 7 B Sample: ' + str(crabs_2(sample)))
# print('Problem 7 B: ' + str(crabs_2(input_)))
#
#
# input_ = list(read_in('inputs/8.txt'))
# sample = list(read_in('inputs/sample_8.txt'))
# print('Problem 8 A Sample: ' + str(segment_1(sample)))
# print('Problem 8 A: ' + str(segment_1(input_)))
# print('Problem 8 B Sample: ' + str(segment_2(sample)))
# print('Problem 8 B: ' + str(segment_2(input_)))
#
# input_ = list(read_in('inputs/9.txt'))
# sample = list(read_in('inputs/sample_9.txt'))
# print('Problem 9 A Sample: ' + str(basins_1(sample)))
# print('Problem 9 A: ' + str(basins_1(input_)))
# print('Problem 9 B Sample: ' + str(basins_2(sample)))
# print('Problem 9 B: ' + str(basins_2(input_)))
#
# input_ = list(read_in('inputs/10.txt'))
# sample = list(read_in('inputs/sample_10.txt'))
# print('Problem 10 A Sample: ' + str(syntax_1(sample)))
# print('Problem 10 A: ' + str(syntax_1(input_)))
# print('Problem 10 B Sample: ' + str(syntax_2(sample)))
# print('Problem 10 B: ' + str(syntax_2(input_)))
#
# input_ = list(read_in('inputs/11.txt'))
# sample = list(read_in('inputs/sample_11.txt'))
# print('Problem 11 A Sample: ' + str(Octopus_1(sample)))
# print('Problem 11 A: ' + str(Octopus_1(input_)))
# print('Problem 11 B Sample: ' + str(Octopus_2(sample)))
# print('Problem 11 B: ' + str(Octopus_2(input_)))
#
# input_ = list(read_in('inputs/12.txt'))
# sample = list(read_in('inputs/sample_12.txt'))
# print('Problem 12 A Sample: ' + str(paths_1(sample)))
# print('Problem 12 A: ' + str(paths_1(input_)))
# print('Problem 12 B Sample: ' + str(paths_2(sample)))
# print('Problem 12 B: ' + str(paths_2(input_)))


# input_ = list(read_in('inputs/13.txt'))
# sample = list(read_in('inputs/sample_13.txt'))
# print('Problem 13 A Sample: ' + str(origami_1(sample)))
# print('Problem 13 A: ' + str(origami_1(input_)))
# print('Problem 13 B Sample: ' + str(origami_2(sample)))
# print('Problem 13 B: ' + str(origami_2(input_)))

# input_ = list(read_in('inputs/14.txt'))
# sample = list(read_in('inputs/sample_14.txt'))
# print('Problem 14 A Sample: ' + str(polymerization_1(sample)))
# print('Problem 14 A: ' + str(polymerization_1(input_)))
# print('Problem 14 B Sample: ' + str(polymerization_2(sample)))
# print('Problem 14 B: ' + str(polymerization_2(input_)))

input_ = list(read_in('inputs/15.txt'))
sample = list(read_in('inputs/sample_15.txt'))
print('Problem 15 A Sample: ' + str(chiton_1(sample)))
print('Problem 15 A: ' + str(chiton_1(input_)))
print('Problem 15 B Sample: ' + str(chiton_2(sample)))
print('Problem 15 B: ' + str(chiton_2(input_)))

# input_ = list(read_in('inputs/16.txt'))
# sample = list(read_in('inputs/sample_16.txt'))
# print('Problem 16 A Sample: ' + str(star_1(sample)))
# print('Problem 16 A: ' + str(star_1(input_)))
# print('Problem 16 B Sample: ' + str(star_2(sample)))
# print('Problem 16 B: ' + str(star_2(input_)))