.. title: Export YouTube's Watch Later playlist
.. slug: youtube-watch-later-export.rst
.. date: 2020-02-17 18:00:00 UTC+01:00
.. tags: youtube, tech
.. category: 
.. link: 
.. description: 
.. type: text

YouTube is increasingly becoming a walled garden. One of the dark patterns I see in it is that the Watch Later playlist, which you may have gathered over what feels like a millenia (so many lectures, so little time...), cannot be exported - you can only add one video at a time to another playlist. That obviously doesn't scale. Here's a quick trick to solve that!

.. TEASER_END

Take this URL:

.. code::

    https://www.youtube.com/playlist?list=WL

Append `&disable_polymer=true` to it:

.. code::

    https://www.youtube.com/playlist?list=WL&disable_polymer=true

And this should bring you to an older version of the website, where if you click the 3-dot "More" menu, you'll find an "Add all to..." button. This allows you to export your Watch Later playlist to another playlist, without the annoying limitations. Once you're there, you can use better software (`NewPipe <https://github.com/TeamNewPipe/NewPipe>`_, for example, or `another solution from the many available <https://webapps.stackexchange.com/questions/27589/how-do-i-export-my-youtube-playlists>`_) to store the playlist elsewhere. I did not investigate those, as I simply wanted to mirror my Watch Later playlist in NewPipe.

Sadly, the same method does not work for the Liked Videos page - which is why you should probably not trust YouTube with your data as much as you likely do now.
