<!--
.. title: I aten't dead
.. slug: i-atent-dead
.. date: 2021-04-18 19:25:41 UTC+02:00
.. tags: status update
.. category: 
.. link: 
.. description: 
.. type: text
-->

Here's a quick status update; I have been meaning to post these more often.

<!-- TEASER_END -->

# Thesis

I'm tinkering away and playing bug whack-a-mole with
[PlasmaPy #1059](https://github.com/PlasmaPy/PlasmaPy/pull/1059), the pull
request that's going to become my masters thesis. Basically, it implements
neoclassical transport calculations - solves for particle and heat flows -
in axisymmetric plasma configurations. It's rather basic, but it's a start.

![Example flux surface](/images/fluxsurface.png)

Here's a sample flux surface - I will soon-ish write a note that explains this concept.
In a nutshell, though - I'm splitting the domain (a 2D slice through a tokamak)
into these circular flux surfaces, a radial grid:

![Example flux surface grid](/images/fluxsurfacegrid.png)

And then I calculate how much flow there is between them.  I still have a good
bunch of problems with it:

* I'm using `astropy.units`, from which I infer that my formulae have issues, as
    each flux comes out with a different physical unit attached. And I'm still
    not quite sure why.
* I still have to figure out a decently nice way to input the quantities
    (density and temperature) that, together with the magnetic field, determine
    this transport.
* I don't understand differential geometry yet, and it really would have been
    useful here. But I'm picking it up, slowly.

# The rest

Whoops, I'm writing this on a timer as an exercise and that one's rapidly
running away. Okay, here goes.

* Part 2 of the [series on fusion](/posts/fusion1) is coming soon; I'm using
    it as a way to cobble together a first draft of my actual thesis introduction.
* PlasmaPy's coming along nicely, though I'm mostly knee deep in the neoclassics
    PR. There have been some cool new developments with documentation and
    speeding up our formulary functions. We're also trying to figure out how
    to host essentially a hackathon. Tips appreciated!
* I've been getting back into reading books, recently, and really enjoying it.
    I'll do a write up of my current system (because *of course* I have a
    system, for it, what did you expect?) in a few weeks.
* Speaking of systems, we recently sat down together with Paulina, realized our
    way of consistently keeping the flat clean... wasn't at all consistent, and
    figured out a system based on a python script and a shared yaml file with
    dates of when we last did X thing (say, vacuuming) vs how often do we
    want to do that particular X. The ratio of time since last occurrence to
    expected period is then a metric than we can actually try to keep down. As
    you have probably guessed by now - write up coming up! But probably not
    soon.

All right, that's in for this week! I will try to be back here next week with
another status update, if I don't actually manage to get fusion2 out. Time will
tell! In the meantime, stay safe!
