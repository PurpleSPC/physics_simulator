from abc import ABC, abstractmethod
import numpy as np
from .particles import Particle

class Force(ABC):
    """
    abstract base class for force laws
    """
    @abstractmethod
    def compute(self, p: Particle) -> np.ndarray:
        """returns a force vector on a particle"""
        pass

class Gravity(Force):
    """
    force of gravity on earth
    in the -z direction
    """
    def __init__(self, g: float = 9.81):
        self.g = g

    def compute(self, p: Particle):
        return np.array([0, 0, -p.mass * self.g])