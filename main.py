# Author: Rubens Andrade Filho
# Date: 2023-07-05

from typing import List, Tuple, Union


def solve_recursively(orders: List[int], rolls: List[int]) -> Union[Tuple[int], bool]:
    """
    Recursively solves the order allocation problem by finding the optimal way
    to fulfill the given orders using the available rolls.

    Args:
        orders (List[int]): A list of order lengths.
        rolls (List[int]): A list of available roll lengths.

    Returns:
        Union[Tuple[int], bool]: The indices of rolls allocated for each order if a solution is found,
            otherwise False.
    """
    if not orders:
        return []

    order = orders[0]
    for i, roll_length in enumerate(rolls):
        if roll_length >= order:
            remaining_rolls = rolls[:]
            remaining_rolls[i] = roll_length - order
            solve_remaining_orders = solve_recursively(orders[1:], remaining_rolls)
            if isinstance(solve_remaining_orders, list):
                return [i] + solve_remaining_orders
    return None


def calculate_leftovers(
    allocated_rolls: List[int], orders: List[int], rolls: List[int]
) -> List[int]:
    """
    Calculates the leftover roll lengths after order allocation.

    Args:
        allocated_rolls (List[int]): A list of indices of rolls allocated for each order.
        orders (List[int]): A list of order lengths.
        rolls (List[int]): A list of available roll lengths.

    Returns:
        List[int]: The lengths of leftover rolls after allocation.
    """
    if not allocated_rolls:
        return rolls
    leftover_rolls = rolls[:]
    for roll_index, order_length in zip(allocated_rolls, orders):
        leftover_rolls[roll_index] -= order_length
    return leftover_rolls


def format_output(
    orders: List[int],
    rolls: List[int],
    allocated_rolls: List[int],
    leftovers: List[int],
) -> None:
    """
    Prints the allocation solution for the given orders and rolls.

    Args:
        orders (List[int]): A list of order lengths.
        rolls (List[int]): A list of available roll lengths.
        allocated_rolls (List[int]): A list of allocated rolls for each order.
        leftovers (List[int]): A list of leftovers roll lengths.
    """
    print(f"There are {len(orders)} orders to be fulfilled:")
    for i, o in enumerate(orders):
        print(f"\tOrder {i}: {o}")

    if not allocated_rolls:
        print("Unable to fulfill the order")
        return

    print(f"Optimal allocation to fulfill {len(orders)} orders:")
    for i, (o, r) in enumerate(zip(orders, allocated_rolls)):
        print(f"\tOrder {i}: cut {o} m from roll {r}")

    print(f"Leftover rolls in stock:")
    for i, leftover in enumerate(leftovers):
        print(f"Roll {i}: {leftover} m")


def main(orders: List[int] = None, rolls: List[int] = None) -> None:
    """
    Entry point of the program. Prompts the user for rolls in stock and order of rolls,
    and calls the solve_recursively function with the provided inputs.

    Args:
        orders (List[int], optional): A list of order lengths. Defaults to None.
        rolls (List[int], optional): A list of available roll lengths. Defaults to None.

    Example usage:

    >>> main([50, 15, 30], [100])

    >>> main([70, 90, 70], [100, 150])
    """
    if not orders:
        orders = input("Order of rolls\t>>> ").split()
    orders = [int(o) for o in orders]

    if not rolls:
        rolls = input("Rolls in stock\t>>> ").split()
    rolls = [int(r) for r in rolls]

    allocated_rolls = solve_recursively(orders, rolls)
    leftovers = calculate_leftovers(allocated_rolls, orders, rolls)

    format_output(orders, rolls, allocated_rolls, leftovers)


if __name__ == "__main__":
    main()
