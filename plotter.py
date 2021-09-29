import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.loadtxt("worker25/timestamps.txt", dtype=np.int32)
print("Start timestamp: ", min(t))
print("End timestamp:   ", max(t))
print("Difference(h):   ", (max(t) - min(t))/3600)
t = t - min(t)
heart_rate = np.loadtxt("worker25/heart.txt", dtype=np.int32)

#Concatenating time and heartrate
merged = np.asarray([t, heart_rate])
merged_sorted = merged.transpose()
merged_sorted = merged_sorted[np.argsort(merged_sorted[:,0])]

s = merged_sorted[:, 1]
t = merged_sorted[:, 0]
dt = [t[i+1] - t[i] for i in range(t.shape[0]-1)]
print("Mean dt: ", np.mean(dt))
print("Standard dev: ", np.std(dt))

#Keep only the first K seconds
K = 500000
index =  np.argmax(t > K)
t = t[:index]
s = s[:index]

stress_classification = [1 if bpm > 90 else 0 for bpm in s]



#Configure plots
fig, ax = plt.subplots()
ax.grid(b=True, which='major', color='#666666', linestyle='-')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

minutes = t/60

ax.plot(minutes, s)
ax.set(xlabel='time (m)', ylabel='Heart rate (bpm)',       title=' ')
#ax.set(xlabel='bin (seconds)', ylabel='Elements in bin', title='delta-time histogram')
#ax.hist(dt, bins=50)


plt.show()
fig.savefig("histogram.png")