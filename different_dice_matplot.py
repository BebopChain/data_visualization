from die import Die
import matplotlib.pyplot as plt

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

# count frequency of each side
frequencies = []
max_value = 0
for one_die in die_list:
    max_value += one_die.num_sides
min_value = len(die_list)

for value in range(min_value, max_value+1):
    frequency = results.count(value)
    frequencies.append(frequency)

title_str = 'D' + str(die_list[0].num_sides)
for one_die in die_list[1:]:
    tmp = ' and ' + 'D' + str(one_die.num_sides)
    title_str += tmp
num_str = str(roll_num)
full_title = 'Results of rolling ' + title_str + ' ' + num_str + ' times'

#start plot
plt.plot(range(min_value, max_value+1), frequencies, linewidth=4)
plt.title(full_title, fontsize=24)
plt.xlabel('Result', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()