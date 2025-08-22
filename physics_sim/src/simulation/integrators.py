
def euler_step(system, dt):
    """
    Uses Euler's method to advance the system
    in increments of dt
    """
    forces = system.compute_forces()
    for i, p in enumerate(system.particles):
        acceleration = forces[i] / p.mass
        p.velocity += acceleration * dt
        p.position += p.velocity * dt