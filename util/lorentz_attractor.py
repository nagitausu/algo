# coding: utf-8
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib.animation import FuncAnimation


dt = 1e-3
epoch = 13 * 10**3
skip = 4 * 10**1
p = 10; r = 28; b = 8.0 / 3.0
nodes = 300

def calc_trajectory(x, y, z):
    data = []
    for i in range(epoch):
        dx = -p * x + p * y
        dy = -x * z + r * x - y
        dz = x * y - b * z
        x += dt * dx; y += dt * dy; z += dt * dz
        if i % skip == 0:
            data.append((x, y, z))
    return data

trajs = []
for _ in range(nodes):
    xyz = [random.random() * 2.0 + 3.0 for _ in range(3)]
    trajs.append(calc_trajectory(*xyz))

def set_aspect_equal_3d(ax, data):
    """Fix equal aspect bug for 3D plots."""
    # xmean = (max(data[0]) + min(data[0])) * 0.5
    # ymean = (max(data[1]) + min(data[1])) * 0.5
    # zmean = (max(data[2]) + min(data[2])) * 0.5
    # plot_radius = max(data[0])
    xmean = 0.0
    ymean = 0.0
    zmean = 20.0
    plot_radius = 20.0
    ax.set_xlim3d([xmean - plot_radius, xmean + plot_radius])
    ax.set_ylim3d([ymean - plot_radius, ymean + plot_radius])
    ax.set_zlim3d([zmean - plot_radius, zmean + plot_radius])

fig = plt.figure(figsize=(10, 10))
fig.tight_layout()
ax = fig.add_subplot("111", projection='3d')
set_aspect_equal_3d(ax, trajs[0])

# Plot animation
# for i, lines in enumerate(zip(*trajs)):
#     scats = []
#     for line in lines:
#         scats.append(ax.scatter(*line))
#     plt.pause(0.001)
#     for scat in scats:
#         scat.remove()

# Save animation
ims = []
for _ in range(nodes):
    im, = ax.plot([], [], [], "o")
    ims.append(im)

def update_anim(frame):
    for i in range(nodes):
        xyz = trajs[i][frame]
        ims[i].set_data(*xyz[:2])
        ims[i].set_3d_properties(xyz[2])
    return ims
anim = FuncAnimation(fig, update_anim, epoch//skip, blit=True)
anim.save("anim.mp4", writer="ffmpeg", fps=10)
