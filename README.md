# Sentiment-Analyzer
Sentiment Analyzer | ACM Month of Code<br>
A chrome extension which filters out negative comments using an ML model.

## Link to the Django Browsable API: [Here](https://sentiment-analyzer-backend.herokuapp.com/)

## Project Motivation
The current times have highlighted the increasing negativity in and around our social media network, especially on Youtube. The negative comments on Youtube have often discouraged good content creators to continue posting awesome new content on their channels. Some of these content creators even consider leaving their careers on Youtube due to this. This prevailing negativity and helplessness motivated us to solve the problem for the greater good - A chrome extension that filters out the negative comments on a Youtube video. To do so, we have used Machine Learning as our primary focus. 

## Tech Stack
NLTK, Tensorflow, Django, Google Youtube API, Javascript, Heroku

## Working of our project
The chrome extension firstly detaches all the comments and sends a POST request of Json having the link to the youtube URL to the Django-Backend. There are mainly three scripts: fetching the comments, processing them using the ML model, sending the JSON of the result. Fetching of youtube comments is achieved using Google Youtube API. While processing the model all the pre-processing of data like lemmatizing, stemming etc is done to make the input more accurate and focus only towards the sentiments of users.Then all data is fed to model it returns the final outcome as a Json classifying the comments as Positive Comments or Negative comments. Based on the JSON, the chrome extension prepends only the positive comment. Thus filtering Negative comments.

## Link to the working video: [here](https://youtu.be/3J83gB2I8D4)

## Challenges Faced
- Proper dataset appropriate for our project was not available. So, we combined 3 dataset for the model.
- Using Naive's Bayes Algorithm, we were getting accuracy of 55%. Then we used CNN model and then we got accuracy of 93%.
- We were facing [CORS error](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS/Errors) while integrating extension and backend. It was solved by adding CORS config in the backend.
- We were first using the indexes for the comments to detach and prepend. The problem in that was that the indexes comments fetched by the API and the comments seen on the youtube were mismatching due to dynamic database of the youtube. Instead of matching indexes, we matched the comments while prepending them back to the page.

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
