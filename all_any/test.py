data = [
            {
                'title': "Super page",
                'description': "Super puper page",
                'id': 'page_super',
                'data': {}
            },
            {
                'title': "Super super page",
                'description': "Super puper page2",
                'id': 'page_super_super',
                'data1': {}
            },
        ]

keys = ['title', 'description', 'id', 'data',]

# for d in data:
#     for key in keys:
#         if key not in d.keys():
#               raise ValueError("Not valid data")


for d in data:
    if not all( [key in d.keys() for key in keys ] ):

        # raise ValueError("Not valid data")
        raise ValueError(print(d.keys()))



# if not all( [key in d.keys() for key in keys for d in data] ):
#     raise ValueError("Not valid data")

# numbers = [1,10,100,1000,10000]
# if [number for number in numbers if number < 10]:
#     print('At least one element is over 10')
#
#
# if any(number < 10 for number in numbers):
#     print('Success')



