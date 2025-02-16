# Water Pitcher Problem Solver (A* Algorithm)

## Description

This project implements a solution to the Water Pitcher problem using the A* search algorithm.  The goal is to find the minimum number of steps to reach a target quantity of water in an initially empty "infinite" capacity pitcher, using a given set of pitchers with specific capacities. Each step consists of either pouring water into the infinite pitcher from one of the given pitchers or pouring water out from the infinite pitcher using one of the given pitchers.

## Files Description

**Project Directory:**
```bash
gwu_ai_project_1.2
├── algorithms.py
├── data
│   ├── input1.txt
│   ├── input2.txt
│   ├── input3.txt
│   └── input4.txt
├── main.py
├── README.md
├── test.py
└── utils.py
```

*   **`algorithms.py`**: Contains the core A* search algorithm implementation (`water_pitcher_solver`) and the heuristic function (`heuristic`).
*   **`utils.py`**:  Provides utility functions, currently including `read_input_file` for parsing input files.
*   **`main.py`**:  The main entry point of the program. It parses command-line arguments, reads the input, and runs the `water_pitcher_solver` to output the result.
*   **`test.py`**: Contains unit tests using the `unittest` library to verify the correctness of the `water_pitcher_solver` function for various input scenarios.
*   **`data/`**:  Directory containing input text files (`input1.txt`, `input2.txt`, `input3.txt`, `input4.txt`) as described in the problem specification. These files are used for testing and demonstration.
*   **`README.md`**:  This file, basically.

## How to Run

1.  **Clone the repository:**

    ```bash
    git clone <https://github.com/abdullaakhundzada/gwu_ai_project_1.2>
    cd gwu_ai_project_1.2
    ```

2.  **Run the `main.py` script:**

    You can execute the solver using the `main.py` script. By default, it uses `data/input4.txt` as input. You can specify a different input file using the `--input_file` argument:

    ```bash
    python main.py
    ```

    You may want to see the description of the argument parsing. Then run:
    
    ```bash
    python main.py --help
    ```

    Which would give the description:
    ```
    usage: main.py [-h] [--input_file INPUT_FILE]
               [--bounding_coefficient BOUNDING_COEFFICIENT] [--verbose]

    options:
    -h, --help            show this help message and exit
    --input_file INPUT_FILE
                            The path to the input file containing the water pitcher information and the target quantity.
                            
    --bounding_coefficient BOUNDING_COEFFICIENT
                            A coefficient to determine the boundary of the overshoot while towards the final value. The maximum allowed overshoot equals to `max_pitcher_size * bounding_coefficient`, hence, the amount of water cannot pass `target_quantity + max_pitcher_size * bounding_coefficient`, making it more aligned with real-world situation

    --verbose             If set, prints the current step, previous state of the final 'infinite' pitcher, its new state after executing the current operation, along with the g-score, h-score and f-score (). ( f(n) = g(n) + h(n) )
    ```

    To use a different input file (e.g., `input1.txt`):

    ```bash
    python main.py --input_file data/input1.txt
    ```

    To use a different bounding coefficient (e.g., `3`):

    ```bash
    python main.py --bounding_coefficient 3
    ```

    To print the steps:

    ```bash
    python main.py --verbose
    ```

    Or just combine everything together for custom test case:
    ```bash 
    python main.py --verbose --input_file data/input1.txt --bounding_coefficient 3
    ```


    The output will be the minimum number of steps required to reach the target quantity, or `-1` if no path exists.

## Algorithm Explanation (Brief)

This project utilizes the **A* search algorithm** to find the shortest path. A* is an informed search algorithm that efficiently explores possible states by using a heuristic function to estimate the cost to reach the goal from the current state.

*   **State:**  Represented by the current quantity of water in the "infinite" pitcher (an integer).
*   **Actions:**  Pouring water into or out of the "infinite" pitcher using any of the pitchers with given capacities. Each action counts as one step.
*   **Heuristic Function:**  The heuristic function `heuristic(capacities, current_amount, target)` estimates the minimum steps remaining by considering only the largest pitcher. It calculates the difference between the `target` and `current_amount` and divides it by the `max_capacity` (and taking the ceiling). This heuristic is admissible as it never overestimates the remaining steps. (Further explanation is provided in the explanation document).
*   **A* Search:** The algorithm maintains a priority queue of states to explore, prioritized by the f-score (f = g + h), where g is the steps taken so far, and h is the heuristic estimate.

## Test Cases

Unit tests are implemented in `test.py` using the `unittest` framework. These tests cover:

*   The provided sample input files (`input1.txt`, `input2.txt`, `input3.txt`, `input4.txt`).
*   Edge cases like no pitcher capacities and target being zero or non-zero.
*   Target being zero with capacities available.

To run the tests, execute:

```bash
python test.py
```