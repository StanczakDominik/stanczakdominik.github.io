<!--
.. title: Short updates: Bayes, Master's, PlasmaPy, Protoss, Julia
.. slug: short-updates-bayes-masters-plasmapy-protoss-julia
.. date: 2020-07-11 20:28:28 UTC+02:00
.. tags: plasmapy, bayes, julia, masters thesis, status
.. category: 
.. link: 
.. description: 
.. type: text
-->

No real new material today, as I'm still in the thick of it. A few updates:

<!-- TEASER_END -->

---

The Bayesian analysis of starcraft data is a bit stuck. I've been trying to
figure out adding time dependence by using gaussian processes. My first real
report note from that is... They're difficult. I mean, they're awesome and
pretty simple conceptually, but picking priors for them is tough, at least for
me and at least for now. I do have some reading to do, there.

There are also a few more projects I want to do in that space. Adding maps to
the split race model is the easiest on that part, but I feel like I don't yet
know enough about model comparison to competently do that. [I'm working on
amending that, though.](https://www.youtube.com/watch?v=bmWMdVQlzIA)

---

My master's thesis is slowly seeing some progress! I've used
[`hypothesis`](https://hypothesis.readthedocs.io/) for testing some of the more
dubious parts of code and it's helped me find a good number of bugs. I might
have more on that to report on in the near future.

---

We're going to be releasing [PlasmaPy](plasmapy.org/) 0.4 soon ish! We're
opting for more time based regular updates rather than based on cool new
features, which are in the works, but not yet for this release. There's been
a bunch of new stuff since January, though!

---

In procrastinatory news, I've been meaning to contribute back to the Starcraft
2 Protoss community a little more, and I figured I'd launch a website to
aggregate current quality educational content in an open and peer reviewed
manner. I'd link it here, but I'm going to be changing its URL and name - I
initially wanted it to be tightly coupled to the [r/AllThingsProtoss
subreddit](https://www.reddit.com/r/allthingsprotoss/) and Discord, but...
let's just say not everyone is as much of a fan of open source culture as I am,
so the website is going to be standalone. I'll still need to work on gathering
reviewers and contributors.

---

Julia the programming language is really, really, really cool. I've been
thinking about it more since (e)attending a seminar by Alan Edelman and, if I
wasn't flooded by projects already, I'd be writing something up for this place
already. For now, three recommendations:

1. This anecdote from the seminar is amazing and really stuck with me:  
<iframe width="560" height="315"
src="https://www.youtube.com/embed/fGgLrzalESY?start=3042" frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen></iframe>

2. This example from a great talk on Julia is pretty darn cool:  
<iframe width="560" height="315"
src="https://www.youtube-nocookie.com/embed/kc9HwsxE1OY?start=227"
frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope;
picture-in-picture" allowfullscreen></iframe>

3. And [this write-up on comparing different ODE solver
   packages](http://www.stochasticlifestyle.com/comparison-differential-equation-solver-suites-matlab-r-julia-python-c-fortran/)
   has made me give up on using Python for that. I've been trying to use
   scipy's odeint to efficiently solve stuff for a while now; but one thing I
   hadn't considered is that defining derivatives through Python functions and
   then having your solver call them the myriad of times required to integrate
   an ODE might... not be the best idea. PV has in fact called it the worst
   case scenario for python, and when you think about it, it makes sense,
   doesn't it?

As a bonus, [`diffeqpy`](https://github.com/SciML/diffeqpy) is a workaround for
that python problem! So I'm not abandoning Python as a high level language, but
the numerics I'll probably do in Julia from now on.

---

And that's all this week; thanks for reading!
