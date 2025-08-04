import pandas as pd
import numpy as np
import math

def calculate_trajectory(initial_velocity, angle):
    angle_radians  = math.radians(angle)
    sin_2a = math.sin(2 * angle_radians)
    Range_fly = round((initial_velocity**2 * sin_2a) / 9.81, 2)
    
    sin_squared = math.sin(angle_radians) ** 2
    max_height = round((initial_velocity**2 * sin_squared) / (2 * 9.81), 2)
    return Range_fly, max_height

print(calculate_trajectory(20 ,45 ))