from die import Die
import pygal

die_list = []
die1 = Die()
die2 = Die(10)
die3 = Die(8)
die_list.append(die1)
die_list.append(die2)
die_list.append(die3)

results = []
roll_num = 70000

for x in range(roll_num):
    result = 1
    for one_die in die_list:
        result += one_die.roll()
    results.append(result)

#print(results)

# count frequency of each side
frequencies = []
max_value = 0
for one_die in die_list:
    max_value += one_die.num_sides
min_value = len(die_list)

for value in range(min_value, max_value+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#print(frequencies)

# draw histogram by pygal
hist = pygal.Bar()

title_str = 'D' + str(die_list[0].num_sides)
for one_die in die_list[1:]:
    tmp = ' and ' + 'D' + str(one_die.num_sides)
    title_str += tmp
num_str = str(roll_num)

hist.title = 'Results of rolling ' + title_str + ' ' + num_str + ' times'

x_label_list = []
for x in range(min_value, max_value+1):
    x_label_list.append(str(x))
hist.x_labels = x_label_list
print(x_label_list)

hist._x_title = 'Result'
hist.y_title = 'Frequency'


hist.add(title_str, frequencies)


hist.render_to_file(title_str + '_' + num_str + '.svg')