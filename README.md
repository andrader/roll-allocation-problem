# Roll Allocation Problem Solver

This Python code solves the **Roll Allocation Problem** using recursion to optimize to find an optimal allocation of rolls to fulfill orders, taking into account the sizes of the rolls and the requirements of each order.

## Table of Contents
- [Roll Allocation Problem Solver](#roll-allocation-problem-solver)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
  - [Problem Description](#problem-description)
  - [Solution](#solution)
  - [Performance](#performance)
  - [Contributing](#contributing)
  - [License](#license)

## Usage

Follow these steps to use the code:

1. Ensure you have Python 3.x installed on your system.
2. Clone or download the repository.
3. Open a terminal or command prompt, navigate to the code directory.
4. Execute the code using the following command:
   ```
   python main.py
   ```
5. Enter the rolls in stock and the orders as space-separated integers when prompted:

   ```shell
   Rolls in stock   >>> 100 150
   Order of rolls   >>> 70 90 70
   ```
    The program will display the optimal allocation of rolls for each order, as well as the remaining stock of rolls.

## Problem Description

The Roll Allocation Problem optimizes the allocation of rolls to fulfill a list of orders. It is a variant of the Knapsack Problem where rolls are items with lengths and orders are the associated values or weights. Although this problem is a specific variant of the Knapsack Problem, it doesn't have a widely recognized name within computer science. It can be referred to as a "Roll Allocation Problem" or "Cutting Stock Problem".

The code uses a recursive algorithm to explore all possible combinations of roll allocations, checking if a roll can fulfill an order and recursively calling itself with updated orders and rolls.

## Solution

The algorithm is a recursive approach with the following steps:

1. The `solve_recursively` function takes `orders` and `rolls` as input.
2. If there are no more orders, an empty list is returned.
3. Select the first order and iterate over the rolls.
4. Check if a roll can fulfill the order.
5. If a roll is found, create a copy of the remaining rolls and update it.
6. Recursively call `solve_recursively` with the remaining orders and rolls.
7. If a successful allocation is found, prepend the allocated roll index and return the list.
8. If no roll can fulfill the order, return None.

The `solve_recursively` function is used with other helper functions in the `main` function to prompt the user, solve the allocation problem, and display the results.

## Performance

The recursive algorithm provides a simple solution but has exponential time complexity of O(2^n), where n is the number of orders. This approach is suitable for small problem instances, but larger problems require more efficient methods like dynamic programming or linear programming.

## Contributing

Contributions are welcome! If you have any issues or suggestions, please open an issue or submit a pull request.

## License

This code is released under the [MIT License](LICENSE).