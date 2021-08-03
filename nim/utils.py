
def nim_sum(num_list):
    """ Calculates the nim sum of the elements in num_list

    Args:
        num_list ([integer]): List of numbers. 
    """
    total_sum = 0
    for num in num_list:
        total_sum ^= num
    return total_sum
