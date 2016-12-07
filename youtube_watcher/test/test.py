#!/usr/bin/env python3


import youtube_watcher


with open('youtube_watcher/test/api_key', 'r') as f:
    API_KEY = f.read()

class Dummy:
    verbose = 10

youtube_watcher.args = Dummy

videos = []
new_videos = []


def test_get_videos():
    global videos
    global new_videos
    user = {'username': 'TeamFourStar'}
    videos = youtube_watcher.get_videos(user, API_KEY)
    new_videos = list(videos)
    assert len(videos) != 0
    return None


def test_get_updated_count():
    global videos
    videos = videos[:-10]
    assert youtube_watcher.get_updated_count(new_videos, videos)[0] == 10
    return None


def test_video_in():
    video = videos[0]
    assert youtube_watcher.video_in(video, videos)
    return None


def test_video_index():
    video = videos[0]
    vid_id = video['id']
    assert youtube_watcher.get_video_index(vid_id, videos) == 0
    return None
