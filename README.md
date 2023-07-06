
# Roll Allocation Problem Solver

This Python code solves the **Roll Allocation Problem**, which involves optimizing the allocation of rolls to fulfill a list of orders. The goal is to find the most efficient way to allocate rolls while minimizing waste or unused roll material.

The code demonstrates how to use recursion to find an optimal allocation of rolls to fulfill orders, taking into account the sizes of the rolls and the requirements of each order.

## Table of Contents
- [Roll Allocation Problem Solver](#roll-allocation-problem-solver)
  - [Table of Contents](#table-of-contents)
  - [Problem Description](#problem-description)
  - [Solution](#solution)
  - [Usage](#usage)
  - [Example](#example)
  - [Contributing](#contributing)
  - [License](#license)


## Problem Description

The Roll Allocation Problem is a variant of the Knapsack Problem. Given a list of orders, each with a specific length, and a list of available rolls, the code determines the optimal allocation of rolls to fulfill all the orders.

The program uses a recursive algorithm to explore all possible combinations of roll allocations. It checks each roll to see if it can fulfill the current order, and if so, recursively calls itself with the remaining orders and updated roll list.

In the classical Knapsack Problem, you are given a set of items, each with a weight and a value, and a knapsack with a maximum weight capacity. The goal is to determine the most valuable combination of items to include in the knapsack without exceeding its weight capacity.

In the variant addressed by the code, the rolls can be seen as the items, where each roll has a length or size. The orders can be seen as the value or weight associated with each item. The objective is to find the optimal allocation of rolls (items) to fulfill the orders (value/weight) while minimizing waste or unused roll material.

Although this problem is a specific variant of the Knapsack Problem, it doesn't have a widely recognized name within computer science. It can be referred to as a "Roll Allocation Problem" or "Cutting Stock Problem," which are specific instances of the Knapsack Problem adapted to cutting rolls of material to fulfill orders.

## Solution

The algorithm used to solve the order allocation problem in the code is a recursive approach. Here's a description of the algorithm:

1. The main function, `solve_recursively`, takes two lists as input: `orders`, which represents the lengths of the orders to be fulfilled, and `rolls`, which represents the available roll lengths.

2. The function starts by checking if there are no more orders to fulfill (`if not orders`). If that's the case, it means all orders have been allocated and the function returns an empty list, indicating a successful allocation.

3. If there are orders remaining, the function selects the first order from the `orders` list and iterates over the available rolls.

4. For each roll, it checks if the length of the roll is greater than or equal to the length of the current order. If it is, the roll can fulfill the order.

5. If a roll is found that can fulfill the order, the function creates a copy of the remaining rolls and subtracts the length of the order from the selected roll. This represents allocating the roll for the order.

6. The function then recursively calls itself (`solve_recursively`) with the remaining orders (excluding the first order) and the updated list of rolls.

7. If the recursive call returns a list, it means a successful allocation has been found. In this case, the function prepends the index of the allocated roll to the list and returns it.

8. If no roll can fulfill the current order, the function returns None, indicating that a solution could not be found for the given set of orders and rolls.

The `solve_recursively` function is used in conjunction with other helper functions (`calculate_leftovers` and `format_output`) in the `main` function to prompt the user for orders and rolls, solve the allocation problem, and display the results.

Overall, the algorithm explores all possible combinations of roll allocations through recursion, checking each roll's length against the order length to find an optimal allocation solution.

The recursive algorithm used in the code provides a straightforward and intuitive approach to solving the order allocation problem. However, it may not be the most efficient solution in terms of runtime complexity.

Compared to other solutions, such as dynamic programming or linear programming approaches, the recursive algorithm has some limitations. Here's a brief comparison:

1. **Dynamic Programming**: Dynamic programming can be used to solve the order allocation problem by breaking it down into smaller subproblems and storing the solutions in a table. This allows for efficient re-use of computed results and avoids redundant computations. Dynamic programming can offer significant performance improvements over the recursive approach, especially for larger problem instances.

2. **Linear Programming**: Linear programming techniques, such as the simplex algorithm or integer programming, can also be applied to solve the order allocation problem. These methods formulate the problem as a mathematical optimization model and use efficient algorithms to find the optimal solution. Linear programming approaches can handle more complex constraints and provide provably optimal solutions, but they may require additional libraries or tools to implement.

3. **Heuristic and Approximation Algorithms**: In some cases, it may be sufficient to find good approximate solutions instead of an optimal solution. Heuristic algorithms, such as greedy algorithms or local search algorithms, can provide fast and practical solutions that are close to optimal. These algorithms make trade-offs between solution quality and computational efficiency, which can be advantageous in time-constrained scenarios.

In summary, while the recursive algorithm used in the code provides a simple and understandable solution to the order allocation problem, other techniques like dynamic programming, linear programming, or heuristic algorithms may offer better performance or more accurate solutions, depending on the specific requirements and constraints of the problem.


## Usage

1. Ensure you have Python 3.x installed on your system.
2. Clone the repository or download the code files.
3. Open a terminal or command prompt and navigate to the directory containing the code files.
4. Run the following command to execute the code:

   ```shell
   python main.py
   ```

5. The program will prompt you to enter the rolls in stock and the orders. Provide the rolls and orders as space-separated integers. For example:

   ```shell
   Rolls in stock   >>> 100 150
   Order of rolls   >>> 70 90 70
   ```

    The program will display the optimal allocation of rolls for each order, as well as the remaining stock of rolls.

## Example

Here's an example usage of the code:

```shell
################################################################################
There are 3 orders to be fulfilled:
    Order 0: 50
    Order 1: 15
    Order 2: 30
Optimal allocation to fulfill 3 orders:
    Order 0: cut 50 m from roll 0
    Order 1: cut 15 m from roll 0
    Order 2: cut 30 m from roll 1
Leftover rolls in stock:
    Roll 0: 5 m
    Roll 1: 120 m
################################################################################

```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This code is released under the [MIT License](LICENSE).

