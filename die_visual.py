from die import Die
import pygal

die = Die()

results = []

for x in range(1000):
    result = die.roll()
    results.append(result)

#print(results)

# count frequency of each side
frequencies = []

for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#print(frequencies)

# draw histogram by pygal
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist._x_title = 'Result'
hist.y_title = 'Frequency'

hist.add('D6', frequencies)
hist.render_to_file('D6_1000.svg')