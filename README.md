# twitter-summarizer-chsclarke

## Asignment
Let’s build a module with an API that will return to the user of the API in text the twitter feed summary (Twitter Feeds and Text description of the images)
That is, describe the images via text using Google Vision and integrate the output together for the user of the API

## Requirements 
none! the app is containerized so there is no need

## Usage

### Build Docker image locally


Build image from Dockerfile:  
`docker build -t chsclarke11/python-endpoint .`

Expose image to port 80:  
`docker run -p 80:5000 chsclarke11/python-endpoint`

Done!


## If your image breaks
Delete all images and containers in the case of an error:  
`docker rm -vf $(docker ps -a -q);docker rmi -f $(docker images -a -q)`
