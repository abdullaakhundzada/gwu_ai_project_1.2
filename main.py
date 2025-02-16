from argparse import ArgumentParser
from algorithms import water_pitcher_solver
from utils import read_input_file

parser = ArgumentParser()

parser.add_argument("--input_file", type=str, default="data/input4.txt", 
                    help="The path to the input file containing the pater pitcher information and the target quantity.")

parser.add_argument("--bounding_coefficient", type=int, default=2, 
                    help="A coefficient to determine the boundary of the overshoot while stepping towards the final value. The maximum allowed overshoot equals to `max_pitcher_size * bounding_coefficient`, hence, the amount of water cannot pass `target_quantity + max_pitcher_size * bounding_coefficient`, making it more aligned with real-world situation")

parser.add_argument("--verbose", action="store_true", 
                    help="If set, prints the current step, previous state of the final 'infinite' pitcher, its new state after executing the current operation, along with the g-score, h-score and f-score (). ( f(n) = g(n) + h(n) )")

args = parser.parse_args()

capacities, target = read_input_file(filename=args.input_file)

print(water_pitcher_solver(
    capacities=capacities, 
    target=target,
    bounding_coefficient=args.bounding_coefficient,
    verbose=args.verbose
    ))
