from die import Die
import pygal

die1 = Die()
die2 = Die()

results = []

for x in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

#print(results)

# count frequency of each side
frequencies = []

for value in range(2, die1.num_sides+die2.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#print(frequencies)

# draw histogram by pygal
hist = pygal.Bar()

hist.title = "Results of rolling 2 D6 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist._x_title = 'Result'
hist.y_title = 'Frequency'

hist.add('D6 + D6', frequencies)
hist.render_to_file('D6+D6_1000.svg')