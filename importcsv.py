import csv
import matplotlib.pyplot as plt 

with open('c:/Users/elzha/OneDrive/Bureau/BACKTESTING/btcusdtpricechange/sorted_bitcoin_data.csv', 'r') as file:
    content = csv.reader(file)

    date = []
    open = []
    high = []
    low = []
    close = []
    volume = []
    next(content)

    for row in content:
        date.append(row[0])
        open.append(float(row[1]))
        high.append(float(row[2]))
        low.append(float(row[3]))
        close.append(float(row[4]))
        volume.append(float(row[5]))

plt.plot(date, high)
plt.show()