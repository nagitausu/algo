# coding: utf-8
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


dt = 1e-2
epoch = 10**4
p = 10; r = 28; b = 8.0 / 3.0
nodes = 5

def calc_trajectory(x, y, z):
    data = []
    for i in range(epoch):
        dx = -p * x + p * y
        dy = -x * z + r * x - y
        dz = x * y - b * z
        x += dt * dx; y += dt * dy; z += dt * dz
        data.append((x, y, z))
    return data

trajs = []
for _ in range(nodes):
    xyz = [random.random() * 30.0 for _ in range(3)]
    trajs.append(calc_trajectory(*xyz))

def set_aspect_equal_3d(ax, data):
    """Fix equal aspect bug for 3D plots."""
    xmean = (max(data[0]) + min(data[0])) * 0.5
    ymean = (max(data[1]) + min(data[1])) * 0.5
    zmean = (max(data[2]) + min(data[2])) * 0.5

    plot_radius = max(data[0])
    ax.set_xlim3d([xmean - plot_radius, xmean + plot_radius])
    ax.set_ylim3d([ymean - plot_radius, ymean + plot_radius])
    ax.set_zlim3d([zmean - plot_radius, zmean + plot_radius])

fig = plt.figure(figsize=(10, 10))
plt.tight_layout()
ax = fig.add_subplot("111", projection='3d')
set_aspect_equal_3d(ax, trajs[0])

for lines in zip(*trajs):
    for line in lines:
        scat = ax.scatter(*line)
        plt.pause(0.001)
