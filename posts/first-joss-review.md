---
title: First JOSS review!
slug: first-joss-review
date: 2020-05-02 19:55:00 UTC+02:00
categories: 
- science
- open-science
- status
---

Several months ago, I stumbled upon [the journal they call
Joss](https://www.youtube.com/watch?v=Y4eKWN_eAxM). Well, actually, [JOSS - the
Journal of Open Source Software, "a developer friendly, open access journal for
research software packages"](https://joss.theoj.org/). It's a completely free,
open-source and open-access alternative to established,
[for-(often-a-lot-of)-profit](https://www.theguardian.com/science/2017/jun/27/profitable-business-scientific-publishing-bad-for-science)
journals such as those by Reed-Elsevier or Springer.

And a few days ago, [I've been called into
service](https://github.com/openjournals/joss-reviews/issues/2133#issuecomment-618617823)
to review [VlaPy, "1D-1V Vlasov-Poisson(-Fokker-Planck) Plasma Physics
Simulation Tool"](https://github.com/joglekara/VlaPy). While I'm digging into that code, I thought I'd write something up about JOSS in general!

<!-- TEASER_END -->

JOSS, as a software-centric journal, is mostly managed via GitHub. Reviewers
sign up [here](https://joss.theoj.org/reviewer-signup.html) (which is a link
I'd like to recommend that you follow!). It's mostly meant to solve one issue:

## Research software attribution

Acknowledgement and funding for developing and maintaining research software
tends to be sparse. Remember the black hole image from last year? To quote
[Andreas Mueller on
Twitter](https://twitter.com/amuellerml/status/1117455802598662144):

<center><blockquote class="twitter-tweet"><p lang="en" dir="ltr">Slightly
ironic that in the same week <a
href="https://twitter.com/NSF?ref_src=twsrc%5Etfw">@NSF</a> rejects a grant to
fund the scipy ecosystem saying that working on it is not impactful enough and
hiring developers to work on it is too expensive. Cc <a
href="https://twitter.com/thisgreyspirit?ref_src=twsrc%5Etfw">@thisgreyspirit</a>
(Katie doesn&#39;t seem to be on Twitter?)</p>&mdash; Andreas Mueller
(@amuellerml) <a
href="https://twitter.com/amuellerml/status/1117455802598662144?ref_src=twsrc%5Etfw">April
14, 2019</a></blockquote> <script async
src="https://platform.twitter.com/widgets.js"
charset="utf-8"></script></center>

To counteract that, scientific developers tend to chase exciting new results
that accompany new releases of their software. However, that often leads to
"more software" instead of "better and more stable software".

As for attribution, citations are everything in the current (rather flawed, in
my opinion - I'm not ready with a pull request just yet, though) system of
evaluation of scientific work. Package authors tend to try to write books about
their works that are then cited. This seems to have improved in the recent years,
but I distinctly remember that most `__citation__` atributes for packages in the
Pythonosphere were books a while ago. Getting software that "just works" and 
simplifies your life published, from what I've heard, can be difficult if not
accompanied by a "novel" result.

JOSS is sort of [a hack on this
system](https://www.arfon.org/announcing-the-journal-of-open-source-software) -
it allows for software to be thoroughly reviewed and appreciated for its own merits.
Of course, it's not a permanent solution; but I'm going to leave deliberating on another one
for another time :)
