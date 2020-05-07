<!--
.. title: Bayesian Inference part 1: What I Talk About When I Talk About Bayes
.. slug: bayesian1
.. date: 2020-02-25 18:00:00 UTC+01:00
.. tags: Bayes
.. type: text
-->

This is the first in a series of a few (number to be determined) blog posts that try to explain Bayesian inference, the subject of my master's thesis. This is basically a spoken language warm-up for my master's thesis. There has already been a great many blog posts written about this topic TODO, but I felt like I could try adding a little of my understanding to the pool of internet knowledge already out there.

In this post, I'll talk about what the Bayesian approach to probability is, TODO. There may be StarCraft examples.

# Frequentism

The classical approach to probability is called the "frequentist" one. When you ask a frequentist, what is the probability that, given some state of the world, event A happens

For our example, let's take StarCraft. You could ask a frequentist: *what's the probability that, when I queue up on the StarCraft ladder as a Protoss, the Terran I meet is going to **proxy rax** me (put his marine-producing barracks structure close to my base and start rushing infantry towards my face)?*

And a Frequentist would probably answer, *"let's ask the wonderful people at `sc2replaystats.com` TODO if they know the numbers on the **proportion** of games where Terrans proxy rax versus Protoss as compared to games where they don't do so*. And then they'd hope the sample size was good enough to have that **frequency** approach the actual **probability**.

TODO this argument feels flimsy and I don't think I should diss frequentists that much

# Bayesianism

Where frequentists think in terms of frequencies in the infinite limit, Bayesians think of beliefs. Off the top of my head, I would say Terrans proxy rax me in about 10% games, so I'd estimate a probability of 0.1 for it. Is that a good estimate? No idea. But it's a start - it's my initial belief, also known as a prior.

I can then use the power of the Bayes Theorem. Behold!

$$TODO BAYES THEOREM$$

Probability of proxy raxing given evidence = probability of evidence given proxy rax * probability of proxy raxing / probability of evidence

## Bayesianism in the field

In fact, this can happen live, when you think about it: let's say I'm scouting the Terran base, here we go. The hero of this story is this very probe: TODO

I see this: TODO

And I know that this is likely


## other

Przykład diagnostyki

Diagnostyka jako graf

Explain explain explain

Examples of different priors affecting output

It is pretty enlightening to see how different choices for this prior change the output:

Discrete input for proxy problem!
