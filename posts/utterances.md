<!--
.. title: Now with comments through utteranc.es!
.. slug: utterances
.. date: 2021-02-08 19:47:16 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

As promised, I've switched the site's comment system from Disqus to
[utteranc.es](https://utteranc.es/). It ended up being [pretty simple to
do in Nikola](https://github.com/StanczakDominik/stanczakdominik.github.io/commit/858c7530d6bd83f1a193ef9225bee5776f2c591c). If I'm correct about how this is supposed to work, comments on the site will now appear as [issues on the site's repo](https://github.com/StanczakDominik/stanczakdominik.github.io/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc). Of course, I would love to test out how this works :)

<!-- TEASER_END -->

The reason I switched away from Disqus was their pretty horrid privacy record, for which a quick websearch will provide ample sources. Utterances is cleverly built around GitHub issues, and while it does require a GitHub account, I think it really is the lesser evil in this case.

Admittedly, I do still feel a little queasy about this. While GitHub does provide repositories for various, [definitely](https://github.com/amerlo94/awesome-plasma-physics-courses) [programming](https://github.com/dask/community) [lite](https://github.com/PlasmaPy/plasmapy-project) repositories, I can't help but think that this takes advantage of a resource given freely in ways that are not entirely as-intended-by-providers.

Take Travis CI, for example. It was a great service, the first project I'm aware of that worked with a "completely free online testing, for every commit, for every open source project out there" model. And, well, they got bought out a few years ago; last year was the year when the new owners (as I suspect) tried to plug the money sink and introduce crippling limits, and a lot of open source projects had to migrate away. I don't know of a single one that still uses Travis, and I fully expect the paid version to go out of business soon.

[Tragedy of the commons, a little?](https://en.wikipedia.org/wiki/Tragedy_of_the_commons)

But you can't solve all problems everywhere at the same time, or at least I haven't yet found a way to. So, for now, utteranc.es it is!


