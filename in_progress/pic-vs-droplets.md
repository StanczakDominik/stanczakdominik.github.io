<!--
.. title: Comparison of Particle-in-cell plasma simulation and the super-droplet method in hydrodynamics
.. slug: pic-vs-droplets
.. date: 2019-04-16 18:00:00 UTC+02:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

I've been diverging with my research interest a little bit recently - reading
a few papers on the [Shima **super-droplet model** in
hydrodynamics](https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.441),
namely turbulence simulation.

And since that sounded interesting, I went ahead and dug into that.

It turns out that the comparison is apt to a degree - super-droplets and
super-particles have that in common that they both **represent vast numbers**
of real particles, fluid droplets and electrons/ions respectively. They are
also both used to translate lagrangian position data into a continuous density
in Eulerian space, on a grid.

There are a bunch of subtle differences, though. Firstly, this is the PIC cycle
that [I've mentioned before](particle-in-cell-methods.md):

![Particle-in-cell cycle (TODO)](PIC-cycle.svg) 

Note that there are two basic actors: particles (which also stand for the
charge and current in the simulation box) and the electric and magnetic fields
on the discrete grid.

For a super-droplet simulation, you would have the velocity and density field,
the particles, but also the temperature, potential temperature,
pollution/aerosol concentration... There's a bunch of entities, thus suggesting
that clouds are more complex environments (even though their interactions may
not be as complex as plasmas are).

The funny thing is, as I've had it explained, the super-droplets do not provide
their density to the velocity field Navier-Stokes solver. Instead, they sort of
live in their own world, coalescing, changing their radii in response to
turbulence and thus evolving their own distribution function - but while a PIC
cycle is interested in the result of *continuously cranking the wheel of the
self-consistent field/plasma evolution*, super-droplet ones are closer to
*"evolve the velocity field self consistently, and on top of that look into how
these <span title="Cheers, luv'!">tracer-like particles</span> evolve over time
especially with respect to turbulence response"*.

Thus, their computational cycle would look more like this:

![Super-droplet cycle (TODO)](Droplet-cycle.svg)

Secondly, super-droplets have vastly more mutual interactions than
super-particles do (at least the classic ones that I know of). In PIC
simulations, you can put two super-particles on top of each other and they're
basically going to represent a larger density at that point in space - two
clusters of real particles superposed on top of each other.

Super-droplets, on the other hand, have a bunch of interactions - the whole
idea is researching coalescence, so when super-droplets meet they
(stochastically, as I'm gonna be investigating soon!) exchange droplets, change
their radii, aerosol content,

Thirdly, there's a difference in that PIC super-particles live in $2 * D$
position-velocity phase space. You could apply a multiplicity to each of them and
while that could be another degree of freedom, as far as I know, it tends not to be -
it's simply preset and constant for all particles in the simulation.

Shima super-droplets, on the other hand, are assumed to reach their free-fall
terminal velocity instantly (thus moving under the paradigm) of Stokesian dynamics.
They have a bunch of other attributes, though - the radius, multiplicity,
aerosol content - and thus they would have $D + 3$ degrees of freedom, moving in $D + 3$
parameter space. Funnily enough, it's the same in 3D.
