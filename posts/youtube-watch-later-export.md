---
title: Export YouTube's Watch Later playlist
date: 2020-02-17 18:00:00 UTC+01:00
date_modified: 2024-10-21
categories: [youtube, tech]
---

::: {.callout-important}
## Outdated by 2021-10-03

As pointed out in the comments by LiadNeumann, YouTube no longer takes the [`&disable_polymer=true`](https://www.youtube.com/playlist?list=WL&disable_polymer=true) parameter for the URL, so this method no longer works. I'm leaving it up for posterity's sake. If anyone has better ideas how to solve this, I'd be much obliged for a comment. 😉
:::

YouTube is increasingly becoming a walled garden. One of the dark
patterns I see in it is that the Watch Later playlist, which you may
have gathered over what feels like a millenia (so many lectures, so
little time\...), cannot be exported - you can only add one video at a
time to another playlist. That obviously doesn\'t scale. Here\'s a quick
trick to solve that!

Take this URL:

``` 
https://www.youtube.com/playlist?list=WL
```

Append [&disable_polymer=true]{.title-ref} to it:

``` 
https://www.youtube.com/playlist?list=WL&disable_polymer=true
```

And this should bring you to an older version of the website, where if
you click the 3-dot \"More\" menu, you\'ll find an \"Add all to\...\"
button. This allows you to export your Watch Later playlist to another
playlist, without the annoying limitations. Once you\'re there, you can
use better software ([NewPipe](https://github.com/TeamNewPipe/NewPipe),
for example, or [another solution from the many
available](https://webapps.stackexchange.com/questions/27589/how-do-i-export-my-youtube-playlists))
to store the playlist elsewhere. I did not investigate those, as I
simply wanted to mirror my Watch Later playlist in NewPipe.

Sadly, the same method does not work for the Liked Videos page - which
is why you should probably not trust YouTube with your data as much as
you likely do now.
