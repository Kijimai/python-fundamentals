from prettytable import *

field_names = ["City name", "Area", "Population", "Annual Rainfall"]
my_data = [["Adelaide", 1295, 1158259, None],
           ["Brisbane", 5905, 1857594, 1146.4],
           ["Darwin", 112, 120900, 1714.7],
           ["Hobart", 1357, 205556, 619.5],
           ["Sydney", 2058, 4336374, 1214.8],
           ["Melbourne", 1566, 3806092, 646.9],
           ["Perth", 5386, 1554769, 869.4]]

my_table = PrettyTable()
for data in my_data:
    my_table.add_row(data)
my_table.field_names = field_names
my_table.align = 'l'  #left-aligned table
print(my_table)
