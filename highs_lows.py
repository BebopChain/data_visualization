import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[2])
        except ValueError:
            print(current_date, 'misssing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    #print(highs)
 
fig = plt.figure(dpi=128, figsize=(10,6))
plt.ylim((-20, 120))
plt.plot(dates, highs, c='red',alpha=0.5, linewidth=1)
plt.plot(dates, lows, c='blue', alpha=0.5, linewidth=1)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title('Daily high and low tempratures - 2014\nDeath Valley', fontsize=24)
plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temprature (F)', fontsize=16)
plt.tick_params(axis='both', labelsize=16)
plt.show()
# for index, column_header in enumerate(header_row):
#    print(index, column_header)