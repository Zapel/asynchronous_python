from python_logging.first_class import FirstClass

# if __name__ == '__main__':

number = FirstClass()
number.increment_number()
number.increment_number()
print("Текущее значение: %s" % str(number.current_number))
number.clear_number()
print("Текущее значение: %s" % str(number.current_number))