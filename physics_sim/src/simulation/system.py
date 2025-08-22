from typing import List
import numpy as np
from .particles import Particle
from .forces import Force

class System:
    """
    hold the particles and force laws 
    computes total force
    """
    def __init__(self):
        self.particles: List[Particle] = []
        self.forces: List[Force] = []

    def add_particle(self, p: Particle):
        self.particles.append(p)

    def add_force(self, f: Force):
        self.forces.append(f)

    def compute_forces(self) -> List[np.ndarray]:
        """
        returns a list of net force vectors
        one for each particle
        """
        net_forces = []
        for p in self.particles:
            total = np.zeroes(3)
            for f in self.forces:
                total += f.compute(p)
            net_forces.append(total)
        return net_forces