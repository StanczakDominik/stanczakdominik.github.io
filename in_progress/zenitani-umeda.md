Further work on this one seems to have revealed numerical instabilities...

I encountered this error while working on improving the particle tracker for PlasmaPy. I implemented a few integrators to choose from, including the zenitani/Umeda one.

Unfortunately, it seems like the integrator works only in dimensionless variables, or my implementation is incorrect. I'm not sure how, though. I should really compare my implementations between the old numpy and new numba.
