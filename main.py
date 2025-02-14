from argparse import ArgumentParser
from algorithms import water_pitcher_solver
from utils import read_input_file

parser = ArgumentParser()

parser.add_argument("--input_file", type=str, default="data/input4.txt", 
                    help="The path to the input file containing the pater pitcher information and the target quantity.")

args = parser.parse_args()

capacities, target = read_input_file(args.input_file)

print(water_pitcher_solver(capacities, target))
