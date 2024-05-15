from random import randrange

def create_id_list():
    """
    Creates list of integers int32 for testing
    :return: id_list
    """
    value_id_negative = []
    value_id_positive = []
    for _ in range(0, 10):
        min_value = 10**_
        max_value = 10**(_+1)
        if max_value > 2147483647:
            max_value = int(2147483647 - max_value * 0.1)
        value_id_positive.append(randrange(min_value, max_value))
        value_id_negative.append((randrange(-max_value+1, -min_value)))
    id_list = [-2147483648]
    id_list.extend(sorted(value_id_negative))
    id_list.append(0)
    id_list.extend(value_id_positive)
    id_list.append(2147483647)
    # print(id_list)
    return id_list

if __name__ == "__main__":
    create_id_list()