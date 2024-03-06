#!/usr/bin/env python3


import math

"""
The following is meant to assist with computing common equations in a college lvl intro to physics course
"""

# constants
GRAVITY = 9.8



# Trigonometry

def split_vector(vector, angle):
    """
    Splits a vector into its x and y components
    @param vector: the vector 
    @param angle: the angle
    """
    x = vector * math.cos(math.radians(angle)) 
    y = vector * math.sin(math.radians(angle))
    
    # print what was solved
    print("Given:\n\tVector: {} at {} degrees".format(vector, angle))
    print("""
             /|              
            / |
           /  |
          /   |     
         /    |
        /_____|
cos = adj/hyp => dir[x]/vector => x = vector * cos(angle)
sin = opp/hyp => dir[y]/vector => y = vector * sin(angle)
Therefore, x = {} and y = {}""".format(x, y))




# Pulley Program
def pulley_system(m1, m2, mu_k):
    """
    Solves for the acceleration of a pulley system
    """
    g = 9.8

    print("""
Diagram of the pulley system:           Broken up into:

                                         N          T
                                         |          |
        +--+                            +--+      +--+
        |1 |------0             F[mu_k]-|1 |-T    |2 |
    ----+--+---+  |                     +--+      +--+
    |          |  |                      |          |
    |          | +--+                   M1*g        M2*g
    |          | |2 |
    |          | +--+
    +----------+

sum(F[x]) = M1*a
    -F[mu_k] + T = M1*a
    -(mu_k) * N + T = M1*a
    => T = M1*a + (mu_k) * N
sum(F[y]) = -M2*a
    T - M2*g = -M2*a
    => T = M2*g - M2*a      
Substitute T:
    M1*a + (mu_k) * N = M2*g - M2*a
Solve for a:
    a = [g*M2 - (mu_k) * N]/(M1 + M2)
""")
    a = (g*m2 - mu_k*g*m1)/(m1 + m2)
    print("Acceleration: {} m/s^2".format(a))



def tension_rope_system(m, length, max_tension):
    """
    Solves for the tension in a rope system
    @param m: mass 
    @param length: length of the rope
    @param max_tension: max tension
    """
    GRAVITY = 9.8
    print("""
Diagram:
        
       ---
        |
        | <- length
        |
        |               So tension goes Up, and mass and gravity go down
       +-+
       | | <- mass      We use the equation Sum(F) = m*v^2/r
       +-+
Steps:
    Sum(F) = m*v^2/r
    T - m*g = m*v^2/r
    v = sqrt[(r(T - m*g))/m] 
""")
    v = math.sqrt((length * (max_tension - m*GRAVITY))/m)
    print("Velocity: {} m/s".format(v))


def work_displacement(F_i, F_j, D_i, D_j):
    """
    Solves for the work done by a force
    @param F_i: force in the x direction 
    @param F_j: force in the y direction
    @param D_i: displacement in the x direction
    @param D_j: displacement in the y direction
    """
    print("""
Formulas:
    Work = Force * Displacement
    Work = F_i * D_i + F_j * D_j
    ------------------------------
    Work = vector(F) * vector(D) * cos(theta)
    Work = sqrt(F_i^2 + F_j^2) * sqrt(D_i^2 + D_j^2) * cos(theta)
    Solve for theta.
""")
    work = F_i * D_i + F_j * D_j
    vector_F = math.sqrt(F_i**2 + F_j**2)
    vector_D = math.sqrt(D_i**2 + D_j**2)
    temp = work / (vector_F * vector_D)
    angle = math.acos(temp)
    print("Work: {} J".format(work))
    print("Angle: {} degrees".format(math.degrees(angle)))


def spring_loaded_system(k, m, x, h):
    """
    Solves for the force of a spring loaded system
    @param k: spring constant 
    @param m: mass
    @param x: displacement
    @param h: height
    """
    print("""

How to Solve:
    - The spring has three positions 1.) equilibrium, 2.) compressed, and 3.) stretched
    - Energy[compressed] = (1/2)kx^2
    - Energy[stretched] = (1/2)mv^2 + mgh
    - Energy[compressed] = Energy[stretched]
""")
    Energy = (1/2)*k*x**2
    v = math.sqrt((Energy - (m * GRAVITY * h))*(2/m))
    print("Velocity: {} m/s".format(v))






