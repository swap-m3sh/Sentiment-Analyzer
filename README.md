# Sentiment-Analyzer
Sentiment Analyzer | ACM Month of Code<br>
A chrome extension which filters out negative comments using an ML model.

## Link to the Django Browsable API: [Here](https://sentiment-analyzer-backend.herokuapp.com/)

## Project Motivation
The current times have highlighted the increasing negativity in and around our social media network, especially on Youtube. The negative comments on Youtube have often discouraged good content creators to continue posting awesome new content on their channels. Some of these content creators even consider leaving their careers on Youtube due to this. This prevailing negativity and helplessness motivated us to solve the problem for the greater good - A chrome extension that filters out the negative comments on a Youtube video. To do so, we have used Machine Learning as our primary focus. 

## Tech Stack
NLTK, Tensorflow, Django, Google Youtube API, Javascript, Heroku

## Working of our project
The chrome-extension firstly detach all the comments and sends a POST request of Json having the link to the youtube url to the Django-Backend. There are mainly three scripts: fetching the comments, processing on them using ML model, sending the Json of result. Fetching of youtube comments is acheived using Google Youtube API. The comments are then fed in the model and model return a Json classifying the comments as Positive Comments or Negative comments. Based on the Json, the chrome-extension, prepends only the positive comment. Thus filtering Negative comments.

## Link to the working video: [here](https://youtu.be/3J83gB2I8D4)

## Steps-To-Use
1. Download zip or Clone the Sentiment-Analyzer GIT repository to your desired location.
2. Go-To your Chrome browser.
3. Click on the 'Manage Extensions' icon next to the URL search bar.
4. Enable the 'Developer Mode' on the top right corner.
5. Click on 'Load Unpacked' on the top left corner.
6. On the 'Select the extension directory' window, open the Sentiment-Analyzer repo which you have just downloaded in step 1 and select 'Youtube Comment Filter'.
7. After selecting it, you'll see the Youtube Comment Filter extension box on the screen.
8. Go to Youtube and play any video.
9. Click on the 'Extensions' icon next to the URL search bar.
10. Select the 'Youtube Comment Filter' extension and enable 'Start Filtering Comments'.

## Team Members
- Aatman Pradhan      
- Prashant Dodiya    
- Swapnil Maheshwari   
