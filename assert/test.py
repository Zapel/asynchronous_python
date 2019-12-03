import logging



def assert_list():
    logging.basicConfig(filename="sample.log", level=logging.INFO)
    log = logging.getLogger("ex")

    list1 = [1, 2, 3]
    list2 = [1, 2, 3, 4, 5]

    try:
        assert set(list1).issubset(list2) == False
        assert set(list2).issubset(list1) == True
    except:
        log.exception("Error!")




if __name__ == '__main__':
    assert_list()
