
def assert_list():
    list1 = [1, 2, 3]
    list2 = [1, 2, 3, 4, 5]


    assert set(list1).issubset(list2) == True
    # assert set(list2).issubset(list1) == True



if __name__ == '__main__':
    assert_list()
