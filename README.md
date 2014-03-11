dlcism
======

Download your favorite [CISM](http://cism893.ca/) podcasts.


deps
----

  * Python 3
    * feedparser


usage
-----

    $ dlcism.py <show ID> [<output dir>]

with:

  * `<show ID>`: show ID (XML filename, without extension, of the feed, e.g.
    714 in `http://podcast.cism893.ca/radioshow/feed_itunes/714.xml`)
  * `<output dir>` (optional): output directory for shows subdirectories
    (defaults to current working directory)

Files will be saved in `<output dir>/<show title>/<Y>-<m>-<d>.mp3`, where
`<show title>` is the show title and `Y`, `m` and `d` the year, month and day when
the show aired.

Existing files are skipped.
