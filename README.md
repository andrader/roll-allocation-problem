
# Roll Allocation Problem Solver

This Python code solves the **Roll Allocation Problem**, which involves optimizing the allocation of rolls to fulfill a list of orders. The goal is to find the most efficient way to allocate rolls while minimizing waste or unused roll material.

The code demonstrates how to use recursion to find an optimal allocation of rolls to fulfill orders, taking into account the sizes of the rolls and the requirements of each order.

- [Roll Allocation Problem Solver](#roll-allocation-problem-solver)
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

The code solves the problem of optimizing the allocation of rolls to fulfill a list of orders. It takes a list of `orders` and a list of `rolls` as input. The goal is to find the most efficient way to allocate the rolls to satisfy all the orders.

The `resolver` function is a recursive helper function that attempts to solve the problem. It takes the current list of orders and the remaining rolls as parameters. It iterates through each roll and checks if it can fulfill the first order in the list. If a roll can cover the order, it recursively calls `resolver` with the remaining orders and the updated list of rolls.

The `print_resolver` function provides a user-friendly interface for inputting the orders and rolls and displays the results. It calls the `resolver` function and, if a solution is found, prints the allocation of rolls for each order and the remaining stock of rolls.

The `main` function serves as the entry point of the program. It prompts the user to input the rolls in stock and the orders, and then calls `print_resolver` to solve the problem and display the results.





## Usage

1. Ensure you have Python 3.x installed on your system.
2. Clone the repository or download the code files.
3. Open a terminal or command prompt and navigate to the directory containing the code files.
4. Run the following command to execute the code:

   ```shell
   python main.py
   ```

5. The program will prompt you to enter the rolls in stock and the orders.
6. Provide the rolls and orders as space-separated integers. For example:

   ```shell
   Rolls in stock   >>> 100 150
   Order of rolls   >>> 70 90 70
   ```

7. The program will display the optimal allocation of rolls for each order, as well as the remaining stock of rolls.

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

