from typing import Tuple
import numpy as np

class Particle:
    """
    A representation of a point-mass
    has position, velocity, and mass
    """
    def __init__(
            self,
            position: Tuple[float, float, float],   # 3d Vector
            velocity: Tuple[float, float, float],   # 3d Vector
            mass = float 
            ):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.mass = mass

    def kinetic_energy(self) -> float:
        """
        Computes 1/2 mv^2
        """
        # compute speed squared = Vx^2 + Vy^2 + Vz^2
        speed_sq = np.dot(self.velocity,self.velocity)
        return 0.5 * self.mass * speed_sq