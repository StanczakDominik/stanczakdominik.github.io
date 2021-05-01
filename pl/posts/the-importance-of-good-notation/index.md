<!--
.. title: The importance of good notation
.. slug: the-importance-of-good-notation
.. date: 2021-05-01 14:35:00 UTC+02:00
.. tags: status update, masters thesis, mathjax
.. category: 
.. link: 
.. description: 
.. type: text
-->

I've just spent the last four weeks hunting for [a bug in my thesis code that
I've mentioned last time](/posts/i-atent-dead).  Since then, I've given up on
the paper I'm reimplementing more times than I can count.  Well... Can you
guess how that went?

<!-- TEASER_END -->

It turns out I missed the fact that $S_{pT}^{ai}$ is very much not the same as
$S_{pT\theta}^{ai}$, where the difference is conceptually a rescaling
$S_{pT\theta}^{ai} \sim \mu S_{pT}^{ai}$, $\mu$ being a viscosity-like object.

So, that happened.

---

I suspect I'm sort of writing this as a reminder to future!myself that hey,
small details are crucial and deserve attention, unless you want to waste
your own time.

At the same time, here's my plea to you - when writing, especially when writing
scientific literature (which, like your code, is going to be read many more
times than the one time you're writing it), pay attention to the notation
you're using for your concepts. Think ahead of how it might contribute to the
reader's understanding of what you're trying to communicate, or hinder it.

And maybe, just maybe, make use of the wide arsenal of typography you've
got available and don't reuse symbols for concepts that are different even
just by their dimensionality!

---

At the same time, I'm really happy to be past this. This bug was really
gnawing at me.

Also, I think this is a great testament to the power of physical unit packages
in scientific computing. I wasted 4 weeks on this, sure - but without
[`astropy.units`](https://docs.astropy.org/en/stable/units/) notifying me that
"your units are off, mate" on every test run, I have no idea how many weeks I
would spend on it later on in the development process, with my results in
disagreement with previous results!
