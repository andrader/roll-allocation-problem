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

    Credit:
        The initial implementation of this function was authored by Rubens Andrade Filho.
    """
    if len(orders) == 0:
        return []

    order = orders[0]
    for i, roll in enumerate(rolls):
        if roll - order >= 0:
            remaining_rolls = rolls[:]
            remaining_rolls[i] = roll - order
            res = resolver(orders[1:], remaining_rolls)
            if res is not False:
                return i, *res

    else:
        return False


def print_resolver(orders: list[int], rolls: list[int]):
    """
    Prints the allocation solution for the given orders and rolls.

    Args:
        orders (list[int]): A list of order lengths.
        rolls (list[int]): A list of available roll lengths.

    Credit:
        The initial implementation of this function was authored by Rubens Andrade Filho.
    """
    print(f"There are {len(orders)} orders to be fulfilled:\n\t"
          + "\n\t".join([f"Order {i}: {o}" for i, o in enumerate(orders)]))

    res = resolver(orders, rolls)

    if res is not False:
        print(f"Optimal allocation to fulfill {len(orders)} orders:\n\t"
              + "\n\t".join([f"Order {i}: cut {o} m from roll {r}" for i, (o, r) in enumerate(zip(orders, res))]))

        leftovers = rolls[:]
        for o, r in enumerate(res):
            leftovers[r] -= orders[o]
        print(f"Leftover rolls in stock:\n\t"
              + "\n\t".join([f"Roll {i}: {leftover} m" for i, leftover in enumerate(leftovers)]))
    else:
        print("Unable to fulfill the order")


def main():
    """
    Entry point of the program. Prompts the user for rolls in stock and order of rolls,
    and calls the print_resolver function with the provided inputs.
    """
    rolls = input("Rolls in stock\t>>> ")
    rolls = [int(r) for r in rolls.split()]

    orders = input("Order of rolls\t>>> ")
    orders = [int(r) for r in orders.split()]

    print_resolver(orders, rolls)

# Example usage
# print("#" * 80)
# print_resolver([50, 15, 30], [100])
# print("#" * 80)
# print_resolver([70, 90, 70], [100, 150])
# print("#" * 80)

# Call the main function
if __name__=="__main__":
    main()
