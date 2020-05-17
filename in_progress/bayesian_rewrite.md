* cel: wytłumaczyć bayesa Kabatowi czy Karolinie
* decision making framework
* decisions under uncertainty

---

This is the first post in a series of attempted explanations of Bayesian methods of probability and inference

I'm going to use Protoss vs Protoss, my least favorite matchup in StarCraft II
as my example. It's a game that's recently been rather famous in machine
learning and AI - actual AI, not just fitting a line - circles. Like chess, it
is a strategy game that takes planning, knowing your enemy, etc TODO. Unlike
chess and like a piano recital, it takes real time dexterity and agility to
carry out all of your strategies. 

I'll try to explain any relevant game concepts as I go and mark **important
concepts in bold**. I'm already late on explaining: the **Protoss** (space
aliens #1) are one of the three playable races in the game. Each of them
handles differently and if you wish to master, say, Protoss, you have to learn
how to beat other Protoss players (these are called "mirror" matchups) as well
as players who choose one of the other two races: Terran (scrappy humans) or
Zerg (space aliens #2).

Another difference between StarCraft and chess - and the one that made me
select this particular example - is that players **act on imperfect
information** all the time. Much like in (pre-satellite) warfare, you do not
know your enemy's actions unless you actually have someone nearby to report
them to you. In StarCraft, this keeping tabs on your opponent is called
**scouting**.

Let's dive into PvP (although my 40% PvP win percentage says, let's not!).

## Basics of PvP

At the risk of oversimplifying a little, there are two main ways a PvP can go nowadays.

The first is "standard" play - where players build their economy up a little,
research some tech upgrades, maybe take an expansion and the game takes 5 to 20
minutes, usually. Like I said, I'm oversimplifying, but PvP has plentiful ways
of becoming what is professionally known as a *clown fiesta* in that period.
The important thing for us here is going to be that players start their game
with two **Gateways**, basic troop producing structures, forming a defensive
wall at the starting base's entrance.

TODO gateway wall pic

The latter is the **cannon rush** - where players refuse to let the game evolve
into a clown fiesta and aim to kill their opponent before the 5 minute mark,
taking their destiny into their hands. This is done by constructing **photon
cannons** - defensive (nominally) turrets - near the enemy's base, shooting
down their workers and eventually the base, at which point the defending player
is eliminated unless they manage to hold the attack off. Cannons require a
building called a **Forge** to exist anywhere to be constructed, and need a
**pylon** - a power source you must construct additional instances of during
the game - nearby to function.

TODO forge + cannons pic

This means that, if you're not trying to cannon rush, the most important part
of early PvP is to identify, *is this opposing Protoss bastard trying to cannon
rush me?* Once that's known, you can either relax a little, breathe out and transition
into whatever flavor of insane clown fiesta you like best... or start looking
around for cannons.

# Bayes rules



# Discrete case

* see gateways at wall = no cannon rush
* see forge at wall = cannon rush
* see nothing = ? well, not actually
* see 1 gate = ?

Thus, taking the bayesian approach... what's my belief that I'm getting cannon rushed?

For example, we may be in a cannon-rush-heavy time, or we may be playing a
known fan of cannons, or we've met someone who tried to play standard last game
and lost! All of these possibilities influence our estimate of the **prior
probability** of cannon rushing.


just apply - simply

player a doesn't cannon rush

player b has made a pledge to avoid the clock striking 7 minutes

# Continuous case

However, things are rarely that simple.
For instance, there's the walking distance. StarCraft games take place on
different maps, often created by enthusiastic players; and as a trend, walking
distance from your base to your opponent's has historically increased.  By the
time you reach their base, a pylon may already be going up, and cannons may be
soon to follow.

timing of worker going towards your base

meet early - high chance of cannon rush
meet mid - lower chance
meet late - very low chance
meet not at all - ?

alternate explanations

apply bayes to function
