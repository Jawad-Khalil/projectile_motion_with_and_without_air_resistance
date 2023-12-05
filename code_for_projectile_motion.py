import matplotlib.pyplot as plt
import math

"""By Jawad Khalil (https://github.com/Jawad-Khalil)
"""
"""Projectile Motion (with and without resistance:  This is a basic and simple model for Projectile Motion.
One can analyze the difference between the motion of an object with and without resistance in the air.
"""

print()
# 1. Setting some initial values

vel_norm = 50  # velocity norm
print('Initial Velocity= ', vel_norm)

angle_degrees = 35  # angle in degrees
print('Projected Angle= ', angle_degrees)

g = 9.806  # Gravity
time_step = 0.01
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
    Vx_init = vel_norm * math.cos(math.radians(angle_degrees))
    # y component of the initial velocity (formula: Voy =Vo*sin(a))
    Vy_init = vel_norm * math.sin(math.radians(angle_degrees))

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
    plt.scatter([xat_ymax, ], [0, ], 50, color='blue')
    plt.scatter([xat_ymax, ], [y_max, ], 50, color='black')
    plt.scatter([0,],[y_max,], 50, color ='blue')

    # Annotating the notable points
    plt.annotate((round(xat_ymax, 1), round(y_max, 1)),
                 xy=(xat_ymax, y_max), xycoords='data',
                 xytext=(+5, -50), textcoords='offset points', fontsize=9,
                 arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=.2", color='black'))
    plt.annotate(round((xat_ymax), 1),
                 xy=(xat_ymax, 0), xycoords='data',
                 xytext=(-10, -27.5), textcoords='offset points', fontsize=10,
                 arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=.2", color='black'))
    plt.annotate(round((x_max), 1),
                 xy=(x_max, 0), xycoords='data',
                 xytext=(-30, -27.5), textcoords='offset points', fontsize=10,
                 arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=.2", color='black'))
    plt.annotate(round((y_max), 1),
                 xy=(0, y_max), xycoords='data',
                 xytext=(-40, 0), textcoords='offset points', fontsize=10,
                 arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=.2", color='black'))
    plt.legend(loc='upper left', frameon=True)

# 3. Defining another function for the motion with resistance.
def resistance():

    x_init, y_init = 0, 0  # x and y components of the initial point

    # Two lists for plotting the Data
    X_list = [0]
    Y_list = [0]

    next_time_step = 0
    b = 0.0087  # Drag coefficient

    # Initial Velocities
    # x component of the initial velocity (formula: Vox =Vo*cos(a))
    Vx_init = vel_norm * math.cos(math.radians(angle_degrees))
    # y component of the initial velocity (formula: Voy =Vo*sin(a))
    Vy_init = vel_norm * math.sin(math.radians(angle_degrees))

    # Filling X_list and Y_list for plotting
    while y_init >= 0:

        # Horizontal component of the acceleration (formula: ax =-b*Vo*Vx)
        ax = -1 * b * vel_norm * Vx_init

        # Vertical component of the acceleration (formula: ay =-g-b*v*Vy)
        ay = -1 * g - b * vel_norm * Vy_init

        # x component of the velocity (formula: Vx = Vox*sin(a)-gt=)
        Vx_init = Vx_init + (ax * time_step)
        # y component of the velocity (formula: Vy = Voy*sin(a)-gt=)
        Vy_init = Vy_init + (ay * time_step)

        # Getting the next time_step
        x_time_step = x_init + (Vx_init * time_step) + (ax * time_step ** 2) / 2  # formula: x = Vox*t+ax*t**2/2
        y_time_step = y_init + (Vy_init * time_step) + (ay * time_step ** 2) / 2  # formula: y = Voy*t+ay*t**2/2

        # Renewing the time_steps
        x_init = x_time_step
        y_init = y_time_step

        # Appending these to the lists
        X_list.append(x_init)
        Y_list.append(y_init)

        # Next time step
        next_time_step += time_step

    # Taking the values in X_list and Y_list where only Y_list's elements are positive.
    if (Y_list[-1] < 0):
        del X_list[-1]
        del Y_list[-1]

    # Some notable points
    x_max = max(X_list)
    y_max = max(Y_list)
    xat_ymax = X_list[Y_list.index(y_max)]

    print("--------------------------------------------------")
    print(f'With resistance(with Drag coefficient={b}):')
    print("The maximum horizontal distance is", x_max)
    print("The maximum vertical distance is", y_max)

    # Plotting
    plt.plot(X_list, Y_list, label='With Resistance', color='green', linewidth=4)

    # Drawing some lines for the notable points
    plt.plot([xat_ymax, xat_ymax], [y_max, 0], color='magenta', linewidth=1.5, linestyle="--")
    plt.plot([xat_ymax, 0], [y_max, y_max], color='blue', linewidth=1.5, linestyle="--")

    # Showing the notable points on the graph
    plt.scatter([x_max,],[0,], 50, color ='black')
    plt.scatter([xat_ymax,],[0,], 50, color ='blue')
    plt.scatter([xat_ymax,],[y_max,], 50, color ='black')
    plt.scatter([0,],[y_max,], 50, color ='blue')

    # Annotating the notable points
    plt.annotate((round(xat_ymax,1),round(y_max, 1)),
                 xy=(xat_ymax, y_max), xycoords='data',
                 xytext=(+20, +30), textcoords='offset points', fontsize=10,
                 arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=.2", color='black'))
    plt.annotate(round((xat_ymax), 1),
                 xy=(xat_ymax, 0), xycoords='data',
                 xytext=(-50, -27.5), textcoords='offset points', fontsize=10,
                 arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=.2", color='black'))
    plt.annotate(round((x_max), 1),
                 xy=(x_max, 0), xycoords='data',
                 xytext=(-20, -27.5), textcoords='offset points', fontsize=10,
                 arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=.2", color='black'))
    plt.annotate(round((y_max), 1),
                 xy=(0, y_max), xycoords='data',
                 xytext=(-40, 0), textcoords='offset points', fontsize=10,
                 arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=.2", color='black'))
    plt.legend(loc='upper right', fontsize='small', frameon=True)
    print('-----------------------End------------------------')

plt.title("Projectile Motion")
plt.xlabel('Distance')
plt.ylabel('Height')
plt.grid()

# 4. Calling the functions and plot to get insight
without_resistance()
resistance()

plt.show()