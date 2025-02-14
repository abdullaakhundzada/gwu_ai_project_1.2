import unittest
from algorithms import water_pitcher_solver  # Assuming you saved as water_pitcher_astar.py
from utils import read_input_file
import os

project_path = os.path.dirname(os.path.realpath(__file__))
data_path    = os.path.join(project_path, "data")

class TestWaterPitcherAStar(unittest.TestCase):

    def test_input1(self):
        capacities, target = read_input_file(os.path.join(data_path, "input1.txt"))
        self.assertEqual(water_pitcher_solver(capacities, target), 4) 

    def test_input2(self):
        capacities, target = read_input_file(os.path.join(data_path, "input2.txt"))
        self.assertEqual(water_pitcher_solver(capacities, target), -1) 

    def test_input3(self):
        capacities, target = read_input_file(os.path.join(data_path, "input3.txt"))
        self.assertEqual(water_pitcher_solver(capacities, target), -1) 

    def test_input4(self):
        capacities, target = read_input_file(os.path.join(data_path, "input4.txt"))
        self.assertEqual(water_pitcher_solver(capacities, target), 18) 

    def test_no_capacity_target_zero(self):
        capacities, target = [], 0
        self.assertEqual(water_pitcher_solver(capacities, target), 0)

    def test_no_capacity_target_nonzero(self):
        capacities, target = [], 5
        self.assertEqual(water_pitcher_solver(capacities, target), -1)

    def test_target_is_zero_with_capacities(self):
        capacities, target = [2, 5], 0
        self.assertEqual(water_pitcher_solver(capacities, target), 0)

if __name__ == '__main__':
    unittest.main() 