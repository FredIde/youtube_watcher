# Youtube Watcher

A script to list and keep track of youtube user videos.

By default it will only list the ones you haven't seen.


# Installing

## 1 - Make sure you have python3 (python3.4) and pip

`sudo apt-get install python3`
`sudo apt-get install python3-pip`


## 2 - Install with pip

Make sure this is pip3

`pip3 install youtube_watcher`
 

## 3 - Get API key
You will need your own API key for youtube. I will not let you use mine.

Go to https://console.developers.google.com/  sign up and get a youtube v3 key.


# Running
Before you do anything you should get the youtube v3 api key from [step 3](#3-get-api-key)

Use `youtube_watcher key API_KEY` **This is required**

Add a new user with `youtube_watcher add USER NAME`

This can be a direct link to the users page or a playlist ID or just a name and my program will search for it.

**Examples**
```
youtube_watcher add TeamFourStar
youtube_watcher add https://youtube.com/user/TeamFourStar
youtube_watcher add PL6EC7B047181AD013
```

You will then need to update the video list with `youtube_watcher update NAME`

NAME can be left blank to update all of them or can be the name of a user.
You can specify some of the name for this, my program will find the closest match.


After you update you want to list the videos. By default this will only list the vidoes you have not marked as watched.

`youtube_watcher list NAME`

NAME can be left blank again to list all of them or can be any part of the user name.

This will go through each video where you can mark as watched or download. Just follow the on screen instructions.


If you want to remove a user, use `youtube_watcher remove username`


## Params

`youtube_watcher list NAME -s`  -s will show all videos, even the ones you have seen.

`youtube_watcher list NAME -r "REGEX"` -r will only show videos when their title match the regex.


# Screenshots

![1](screenshots/1.png?raw=true)
![2](screenshots/2.png?raw=true)
![3](screenshots/3.png?raw=true)
![4](screenshots/4.png?raw=true)
![5](screenshots/5.png?raw=true)
