<!--
.. title: Dealing with backlogs
.. slug: backlogs
.. date: 2020-05-17 13:25:00 UTC+02:00
.. tags: python,scripting
.. category: Personal productivity scripting
.. link: 
.. description: 
.. type: text
.. has_math: true
-->


I have a backlog problem.

Like probably many of you in 2020, I suffer from having too much interesting
content to read, watch, listen to or play through. I've been thinking about
ways to tackle my gathering points, and I think I finally have something I'm
willing to share that could be useful for you as well.

<!-- TEASER_END -->

The journey for me started with Pocket, which is basically a centralized link
gathering service for articles you'd like to read.  I use it to dump
interesting links from RSS and from all over the web that I don't have a
particular need to read right where and when I find them. This, of course,
vastly exceeds the number of articles I actually read. And that's fine; you
have to say no to a lot of content nowadays, becuse a vast amount of news
content (I'm looking at you, politics!) becomes out of date pretty much
instantly. If you let them stew for a week or two, it often turns out you
didn't need to read them in the first place anyway.

Still, my backlog has become a hoard of way too many articles to get through in
my lifteime. I could just set a goal of "read 5 articles a day", but that can
be easily gamed - just go through all the trash politics news you don't
actually care about, bingo, go do something else while your backlog gently
expands.

While reading up on Beeminder (on which you can expect another post soon-ish!),
I found this interesting method for dealing with this issue on
[beemind.me](https://beemind.me/goals/pocket/article_days_linear) by [Gal
Tsubery](https://github.com/tsubery). To your backlog, you assign a numerical
value calculated as

$$ F = \sum_{articles} \text{Days since article was added} $$

And then you try to minimize that. You can easily plug this into Beeminder to
get easy tracking of progress on decreasing your backlog, and a deadline if you slack
off on getting through it:

<center><iframe src="https://www.beeminder.com/widget?slug=pocket-backlog&username=stanczakdominik" height="185px" width="230px" frameborder="0px" ></iframe></center>

This idea is particularly neat for a few reasons:

1. to grab these juicy drops in F, you can always remove articles you know you're not going to get to;
2. reading old articles becomes the default action, and the tail end of your backlog gets filtered by the previous point to become stuff you actually care about;
3. reading important new articles becomes preventive action; you stop them from growing into these huge threats;
4. deleting unimportant new articles becomes more of a habit due to 2;
5. with your experience from 4, you start paying more attention to your information diet, skipping articles that catch your attention via clickbaity articles but are going to stop being important in a fortnight's time.

I liked it, so I tinkered a bit with Python, Systemd (though a cron job to run the script periodically would do) and the Beeminder web API and some neat libraries to apply the same concept to:

## Todoist

This tracks my old tasks (all the Julia tutorials I'm never going to get to,
stuff I've quietly given up on over the years, etc etc):

<center><iframe src="https://www.beeminder.com/widget?slug=todoist-backlog&username=stanczakdominik" height="185px" width="230px" frameborder="0px" ></iframe></center>

A little helper function to do the Beeminder API call is nice to have:

```python
import requests
import os
beeminder_auth_token = os.environ['BEEMINDER_TOKEN']
beeminder_username = os.environ['BEEMINDER_USERNAME']

def increment_beeminder(desc, beeminder_goal, value=1):
    data = {
        "value": value,
        "auth_token": beeminder_auth_token,
        "comment": desc,
    }

    response = requests.post(
        f"https://www.beeminder.com/api/v1/users/{beeminder_username}/goals/{beeminder_goal}/datapoints.json",
        data=data,
    )
    return response
```

And now we use the [Todoist API](https://pypi.org/project/todoist-python/) to get at out tasks:
```python
#!/usr/bin/python
import datetime
import numpy as np
import dateutil
import dateutil.parser
import todoist
import os
now = datetime.datetime.now(datetime.timezone.utc)
key = os.environ['TODOIST_KEY']
api = todoist.TodoistAPI(key)
api.sync()

undone_tasks = api.items.all(lambda x: not x['checked'])
dates = [dateutil.parser.parse(task['date_added']) for task in undone_tasks]
deltas = [date - now for date in dates]
total = -np.sum(deltas)
total_days = total.days + total.seconds / 3600 / 24

message = f"Incremented automatically from {len(undone_tasks)} tasks at {now}"
increment_beeminder(message, "todoist-backlog", total_days)

```
## Youtube videos

<center><iframe src="https://www.beeminder.com/widget?slug=youtube-backlog-upgrade&username=stanczakdominik" height="185px" width="230px" frameborder="0px" ></iframe></center>

This took a bit of legwork because [YouTube's Watch Later playlist is not
accessible from remote API's, as I've written about
before](/posts/youtube-watch-later-export.rst); but once you get accustomed to
using another playlist for you ~~kitten vids~~ SciPy tutorials, it's as simple
as the following:

```python
#!/usr/bin/python
import pafy
import dateutil.parser
from datetime import datetime, timedelta
from sc2replib import increment_beeminder
url = "https://www.youtube.com/playlist?list=PL8B03F998924DA45B"  # example playlist ID
playlist = pafy.get_playlist(url)

now = datetime.now()
total = timedelta(seconds=0)
for item in playlist['items']:
    added_date = dateutil.parser.parse(item['playlist_meta']['added'])
    total += now - added_date


total_days = total.days + total.seconds / 3600 / 24

message = f"Incremented automatically from {len(playlist['items'])} movies at {now}"
increment_beeminder(message, "youtube-backlog-upgrade", total_days)
```

## Future work?

I'm probably going to simplify these scripts using my [Beeminder-CLI](https://github.com/StanczakDominik/beeminder-cli/)
library I've been writing recently.

I'm also wondering about other applications of this idea:

* My [pubs](https://github.com/pubs/pubs/) (another piece of really cool software!) articles-to-read list is definitely the next move. They store article add dates in `.yaml` files, so it's going to be simple to loop over all those, filter out only the ones marked as actually to be read, then sum them up.
* I use [Antennapod](https://antennapod.org/) for podcasts, but that's Android-only and I haven't yet found a simple way to run Python scripts on mobile; even then, I have no clue how to extract podcast queue-addition dates from it.
* Steam games would be another neat idea, but I don't know if they have a library API I could read. I also don't know of any way to neatly remove a game from the immediate library. Tags could work, I guess, if they have them.
