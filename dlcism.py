#!/usr/bin/env python
import feedparser
import datetime
import urllib
import sys
import os


def _format_filename(date):
    return date.strftime('%Y-%m-%d.mp3')


def _get_feed_infos(id):
    d = _parse_feed(id)
    infos = {
        'title': d.feed.title.replace('CISM 89.3 : ', ''),
        'shows': []
    }
    for entry in d.entries:
        show = {}
        parts = entry.title.split(' ')
        date = parts[-2]
        show['date'] = datetime.datetime.strptime(date, '%m/%d/%Y')
        show['link'] = entry.link
        infos['shows'].append(show)

    return infos


def _parse_feed(id):
    url = 'http://podcast.cism893.ca/radioshow/feed_itunes/{}.xml'.format(id)
    d = feedparser.parse(url)
    if d.status == 404:
        sys.stderr.write("Error: feed {} doesn't exist\n".format(id))
        sys.exit(1)
    return d


def download_shows(base_dir, id):
    infos = _get_feed_infos(id)
    show_path = os.path.join(base_dir, infos['title'])
    if not os.path.exists(show_path):
        os.makedirs(show_path)
    for show in infos['shows']:
        filename = _format_filename(show['date'])
        path = os.path.join(show_path, filename)
        if not os.path.isfile(path):
            print('Downloading {} ({})...'.format(filename, infos['title']))
            urllib.request.urlretrieve(show['link'], path)
        else:
            print('Skipping {} ({})...'.format(filename, infos['title']))


if __name__ == '__main__':
    show_id = sys.argv[1]
    base_dir = os.getcwd()
    if len(sys.argv) >= 3:
        base_dir = sys.argv[2]
    download_shows(base_dir, show_id)
