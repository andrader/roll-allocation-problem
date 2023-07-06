# Author: Rubens Andrade Filho
# Date: 2023-07-05


def resolver(orders: list[int], rolls: list[int]):
    """
    Recursively solves the order allocation problem by finding the optimal way
    to fulfill the given orders using the available rolls.

    Args:
        orders (list[int]): A list of order lengths.
        rolls (list[int]): A list of available roll lengths.

    Returns:
        tuple: The indices of rolls allocated for each order if a solution is found,
               otherwise False.
    """
    if not orders:
        return []

    order = orders[0]
    for i, roll_lenght in enumerate(rolls):
        if roll_lenght >= order:
            remaining_rolls = rolls[:]
            remaining_rolls[i] = roll_lenght - order
            res = resolver(orders[1:], remaining_rolls)
            if isinstance(res, list):
                return [i] + res
    return None


def calculate_leftovers(allocated_rolls, orders, rolls):
    """
    Calculates the leftover roll lengths after order allocation.

    Args:
        allocated_rolls (list[int]): A list of indices of rolls allocated for each order.
        orders (list[int]): A list of order lengths.
        rolls (list[int]): A list of available roll lengths.

    Returns:
        list[int]: The lengths of leftover rolls after allocation.
    """
    if not allocated_rolls:
        return rolls
    leftover_rolls = rolls[:]
    for roll_index, order_length in zip(allocated_rolls, orders):
        leftover_rolls[roll_index] -= order_length
    return leftover_rolls


def format_output(
    orders: list[int],
    rolls: list[int],
    allocated_rolls: list[int],
    leftovers: list[int],
):
    """
    Prints the allocation solution for the given orders and rolls.

    Args:
        orders (list[int]): A list of order lengths.
        rolls (list[int]): A list of available roll lengths.
        allocated_rolls (list[int]): A list of allocated rolls for each order.
        leftovers (list[int]): A list of leftovers roll lengths.

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


def main(orders=None, rolls=None):
    """
    Entry point of the program. Prompts the user for rolls in stock and order of rolls,
    and calls the print_resolver function with the provided inputs.

    Example usage
    print("#" * 80)
    main([50, 15, 30], [100])
    print("#" * 80)
    main([70, 90, 70], [100, 150])
    print("#" * 80)
    """
    if not rolls:
        rolls = input("Rolls in stock\t>>> ").split()
    rolls = [int(r) for r in rolls]

    if not orders:
        orders = input("Order of rolls\t>>> ").split()
    orders = [int(o) for o in orders]

    allocated_rolls = resolver(orders, rolls)
    leftovers = calculate_leftovers(allocated_rolls, orders, rolls)

    print(orders, rolls, allocated_rolls, leftovers)

    format_output(orders, rolls, allocated_rolls, leftovers)


if __name__ == "__main__":
    main()
