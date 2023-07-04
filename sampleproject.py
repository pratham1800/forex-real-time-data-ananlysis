from kafka import KafkaConsumer
import matplotlib.pyplot as plt
import json
import threading
import csv
import numpy as np
from matplotlib.ticker import FormatStrFormatter
from datetime import datetime
plt.ion()
fig,dataPlotter = plt.subplots()
x=['']
y=[0]
plt.xlim(0.678,0.679)
plt.ylim(0,10)
fig.set_figwidth(20)
dataPlotter.xaxis.set_major_formatter(FormatStrFormatter('%.6f'))
graph=dataPlotter.scatter(y,x)
consumer = KafkaConsumer ('askPriceOutput',bootstrap_servers = ['localhost:9092'],
value_deserializer=lambda m: json.loads(m.decode('utf-8')))
plt.draw()
for message in consumer:
 
    x.append(message[6]['quoteTimestamp'])
    y.append(message[6]['askPrice'])
    npX = np.array(x,dtype='O')
    npY = np.array(y)
    scatterArray = np.concatenate([npY,npX])
    print(scatterArray)
    graph.set_offsets(np.c_[npY,npX])
    fig.canvas.draw_idle()
  
    plt.pause(0.1)
plt.waitforbuttonpress()
