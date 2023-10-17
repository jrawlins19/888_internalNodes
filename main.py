def find_internal_nodes_num(tree):
    # all we're really looking for is how many unique values (excluding -1) there are
    res = set()
    for node in tree:
        # if the value is in the set, then adding it does nothing
        res.add(node)
    # remove -1 as we don't need -1
    return len(res) - 1


# my_tree = [4, 4, 1, 5, -1, 4, 5]
my_tree = [9, 7, 7, 5, 5, 7, 14, -1, 2, 1, 4, 2, 4, 2, 11, 9]
print(find_internal_nodes_num(my_tree))
