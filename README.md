# twitter-summarizer-chsclarke

## Asignment
Let’s build a module with an API that will return to the user of the API in text the twitter feed summary (Twitter Feeds and Text description of the images)
That is, describe the images via text using Google Vision and integrate the output together for the user of the API

## Requirements 
none! the app is containerized so there is no need

## Installation

### Enable [google](https://cloud.google.com/vision/docs/before-you-begin) and [twitter](https://developer.twitter.com/en/docs/basics/getting-started) API's

Once you have your API keys, add them to the [auth](https://github.com/BUEC500C1/twitter-summarizer-chsclarke/tree/master/auth) folder. Be sure to remove `[template]` from the file names.

### Build Docker image locally

Build image from Dockerfile:  
`docker build -t chsclarke11/python-endpoint .`

Expose image to port 80:  
`docker run -p 80:5000 chsclarke11/python-endpoint`

Done!


### If your image breaks
Delete all images and containers in the case of an error:  
`docker rm -vf $(docker ps -a -q);docker rmi -f $(docker images -a -q)`

## Usage

There are two active enpoints on the REST service `/get_profile`, and `/get_tweet`.

`/get_profile` takes username as an input and returns a a JSON object describing the given users profile as well as a text description for their profile image.

example: http://localhost/get_profile?username=realdonaldtrump

I passed the handle (not case sensitive) for donal trump to get a description of his profile.

Response:
```
{
  "created_at": "Wed Mar 18 13:46:38 +0000 2009", 
  "description": "45th President of the United States of America\ud83c\uddfa\ud83c\uddf8", 
  "followers_count": 72051906, 
  "id": 25073877, 
  "img": [
    [
      "Face", 
      99.36352968215942
    ], 
    [
      "Forehead", 
      98.30324053764343
    ], 
    [
      "Hair", 
      97.86621332168579
    ]
  ], 
  "location": "Washington, DC", 
  "name": "Donald J. Trump", 
  "screen_name": "realDonaldTrump", 
  "urls": [
    {
      "display_url": "Instagram.com/realDonaldTrump", 
      "expanded_url": "http://www.Instagram.com/realDonaldTrump", 
      "indices": [
        0, 
        23
      ], 
      "url": "https://t.co/OMxB0x7xC5"
    }
  ]
}
```


`/get_tweet` endpoint has the same functionality, but it returns the latest tweet of a given handle. Photos within the tweet are described under "img"

example: http://localhost/get_tweet?username=realdonaldtrump

Response:
```
{
  "img": [
    [
      "News", 
      87.33186721801758
    ], 
    [
      "Photo caption", 
      84.17827486991882
    ], 
    [
      "Font", 
      74.9562680721283
    ]
  ], 
  "tweet": "https://t.co/KSVkKL76NM"
}
```
