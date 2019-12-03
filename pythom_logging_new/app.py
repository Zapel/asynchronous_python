from pythom_logging_new import FirstClass, SecondClass

if __name__ == '__main__':

    number = FirstClass()
    number.increment_number()
    number.increment_number()
    print("Текущее значение: %s" % str(number.current_number))
    number.clear_number()
    print("Текущее значение: %s" % str(number.current_number))

    system = SecondClass()
    system.enable_system()
    system.disable_system()
    print("Текущее состояние системы: %s" % str(system.enabled))
