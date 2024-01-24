import matplotlib.pyplot as plt
import math
import scipy.integrate as sci
import numpy as np

"""Projectile Motion (with and without resistance:  This is a basic and simple model 
for Projectile Motion. One can analyze the difference between the motion of an object
with and without resistance in the air.
"""

print()
# 1. Setting some initial values

vel_norm = 4  # velocity norm
print('Initial Velocity= ', vel_norm)

angle = 45*np.pi/180  # angle in radians
print('Projected Angle= ', angle)

g = 9.806  # Gravity
time_step = 0.001
b = 1  # Drag coefficient

print("--------------------------------------------------")

# 2. Defining a function for motion without resistance
def without_resistance():
    # Initial Point
    x_init, y_init = 0, 0  # x and y components of the initial point

    # Two lists for plotting
    X_list = [0]
    Y_list = [0]

    next_time_step = 0

    # Initial Velocities
    # x component of the initial velocity (formula: Vox =Vo*cos(a))
    Vx_init = vel_norm * math.cos(angle)
    # y component of the initial velocity (formula: Voy =Vo*sin(a))
    Vy_init = vel_norm * math.sin(angle)

    # Filling X_list and Y_list for plotting
    while y_init >= 0:
        # ax is zero: no change in x component of the velocity
        # Vertical component of acceleration is negative of the Gravity
        ay = -g

        # y component of the velocity (formula: Vy = Voy*sin(a)-gt=)
        Vy_init = Vy_init + (ay * time_step)

        # Getting the next time_step
        x_time_step = x_init + (Vx_init * time_step)  # formula: x = Vo*cos(a)*t)
        y_time_step = y_init + Vy_init * time_step + (ay * time_step ** 2) / 2  # formula: y = Vo*sin(a)*t-g*t**2/2

        # Renewing time_steps
        x_init = x_time_step
        y_init = y_time_step

        # Appending these to the lists
        X_list.append(x_init)
        Y_list.append(y_init)

        # Next time step
        next_time_step += time_step

        """ We may get the negative value in Y_list even while y_init >= 0 due to -g.
        So, take the values in X_list and Y_list where only Y_list's elements are positive.
        """
        if (Y_list[-1] < 0):
            del X_list[-1]
            del Y_list[-1]

    # Some notable points
    x_max = max(X_list)  # Maximum horizontal distance
    y_max = max(Y_list)  # Maximum height reached
    xat_ymax = X_list[Y_list.index(y_max)]  # Value of x when y is maximum.

    print("without resistance:")
    print("The maximum horizontal distance is", x_max)
    print("The maximum vertical distance is", y_max)

    # Plotting
    plt.plot(X_list, Y_list, label='Without Resistance', color='red', linewidth=3, linestyle='-')

    # Drawing some lines for the notable points
    plt.plot([xat_ymax,xat_ymax],[0,y_max], color ='magenta', linewidth=1.5, linestyle="--")
    plt.plot([xat_ymax,0],[y_max,y_max], color ='blue', linewidth=1.5, linestyle="--")

    # Showing the notable points on the graph
    plt.scatter([x_max, ], [0, ], 50, color='black')
    plt.scatter([xat_ymax, ], [y_max, ], 50, color='black')

"""Let X = x, Vx , y Vy. To solve our ODE with sci.solve_ivp, we will need a function
that takes X, time, and friction and returns dX/dt.
"""
# 4 Defining the dX/dt function
def dXdt(t,X,b):
    x, Vx, y, Vy, = X
    return [Vx,
            -b*np.sqrt(Vx**2+Vy**2)*Vx,
            Vy,
            -g-b*np.sqrt(Vx**2+Vy**2)*Vy]

# Using scipy to solve the above differential equations
solved = sci.solve_ivp(dXdt, [0, 575], y0=[0,vel_norm*np.cos(angle),0,vel_norm*np.sin(angle)], t_eval=np.linspace(0,2,1000), args=(b,))

# 2 list for plotting
list1 = []
list2 = []
for i in solved.y[2]:
    list2.append(i)
while list2[-1] < 0:
    del list2[-1]
for i in solved.y[0]:
    list1.append(i)
list3 = list1[:len(list2)]

# Some notable points
x_max = max(list3)
y_max = max(list2)
xat_ymax = list3[list2.index(y_max)]

# Plotting
plt.plot(list3, list2, label='With resistance', color='black', linewidth=2)
plt.scatter([x_max,],[0,], 50, color ='black')
plt.scatter([xat_ymax,],[y_max,], 50, color ='black')
plt.plot([xat_ymax, xat_ymax], [y_max, 0], color='magenta', linewidth=1.5, linestyle="--")
plt.plot([xat_ymax, 0], [y_max, y_max], color='blue', linewidth=1.5, linestyle="--")

plt.annotate('With Resistance \n(solved with \nscipy.solve_ivp)',
                 xy=(0.54, 0.24), xycoords='data',
                 xytext=(65, 0), textcoords='offset points', fontsize=9,
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 horizontalalignment='left',
                 verticalalignment='center',
                 clip_on=True)
# Spines

ax = plt.gca()
ax.spines['right'].set_color('yellow')
ax.spines['top'].set_color('cyan')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
without_resistance()

plt.title("Projectile Motion")
plt.xlabel('Distance')
plt.ylabel('Height')
plt.grid()
plt.legend(loc=1)
plt.show()

print('----------------------------------------------')
print(f'With resistance(solved with sci.solve_ivp with Drag coefficient={b}):')
print("The maximum horizontal distance is", x_max)
print("The maximum vertical distance is", y_max)
print('ended')
