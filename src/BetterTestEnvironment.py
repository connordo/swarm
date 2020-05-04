from classes import sClass as s
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
This is a test enviroment for tinkering around with 'floaters', or the small
little nodes that make up our swarm network. Better algorithms and more advanced
Tests ought to be written in other scripts for long-term preservation
"""

swarm_member_count = 50
swarm = s.Swarm(swarm_member_count)
swarm.set_random_destination()

fig = plt.figure()
ax = plt.axes(xlim=(0, s.squarea), ylim=(0, s.squarea))
lineF, = ax.plot([], [], 'bo')
lineC, = ax.plot([], [], 'ro')


def init():
    lineF.set_data([], [])
    lineC.set_data([], [])
    return lineF, lineC


def animate(*args):
    xF = []
    yF = []
    xA = []
    yA = []

    swarm.move_swarm_stochasticly()

    for i in swarm.get_uncollided():
        xF.append(i.position.x)
        yF.append(i.position.y)

    swarm.check_for_detour_needs()
    swarm.check_collisions()

    for i in swarm.get_collided():
        xA.append(i.position.x)
        yA.append(i.position.y)

    lineF.set_data(xF, yF)
    lineC.set_data(xA, yA)

    return lineF, lineC

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True)
plt.show()
