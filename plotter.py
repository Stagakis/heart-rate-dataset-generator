import matplotlib.pyplot as plt
import numpy as np

from io import StringIO   # StringIO behaves like a file object

# Data for plotting
t = np.loadtxt("worker25/timestamps.txt", dtype=np.int32)
print("Start timestamp: ", min(t))
print("End timestamp:   ", max(t))

t = t - min(t)
heart_rate = np.loadtxt("worker25/heart.txt", dtype=np.int32)

#Concatenating time and heartrate
merged = np.asarray([t, heart_rate])
merged_sorted = merged.transpose()
merged_sorted = merged_sorted[np.argsort(merged_sorted[:,0])]

t = merged_sorted[:, 0]
dt = [t[i+1] - t[i] for i in range(t.shape[0]-1)]
print("Mean dt: ", np.mean(dt))
print("Standard dev: ", np.std(dt))
s = merged_sorted[:, 1]

#Keep only the first K seconds
K = 36000
index = np.argmax(t > K)
t = t[:index]
s = s[:index]

fig, ax = plt.subplots()
ax.plot(t, s)
#ax.plot(np.arange(t.shape[0]), t)
ax.set(xlabel='time (s)', ylabel='Heart rate (bpm)',       title=' ')
ax.grid()

#plt.hist(t, bins=500)
plt.show()
fig.savefig("test.png")