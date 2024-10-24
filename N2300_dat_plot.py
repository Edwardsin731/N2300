import numpy as np
import matplotlib.pyplot as plt

def plot_csv_data_with_numpy(file_path):
  data = np.genfromtxt(file_path, delimiter=',', skip_header=1)
  time = data[:, 0 ]
  voltage = data[:, 1]
  plt.figure(figsize=(10,6))
  plt.plot(time, voltage, label= 'Chemical signal', color ='b')
  plt.xlabel('Time (s)')
  plt.ylabel('Transfer )
  plt.title('Voltage over time')
  plt.legend()
  plt.grid()
  plt.show()
csv_file_path = '/content/coc_1_output.csv'
plot_csv_data_with_numpy(csv_file_path)