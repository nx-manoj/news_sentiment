import feedparser
import matplotlib.pyplot as plt


def sentiment(string_of_name):
    words = string_of_name.lower().split()
    count_of_positive = 0
    count_of_negative = 0
    neutral = 0
    list_of_positive_word = 'growth win success rise boost peace launch record improve'.lower().split()
    list_of_negative_word = 'crash war death fall crisis attack fail risk disaster'.lower().split()
    for word in words:
        if word in list_of_positive_word:
            count_of_positive += 1
        elif word in list_of_negative_word:
            count_of_negative += 1
        else:
            neutral += 1
    
    if count_of_positive > count_of_negative:
        return "Positive"
    elif count_of_negative > count_of_positive:
        return "Negative"
    else:
        return "Neutral"

    

result = []

rss_feed_url = "http://feeds.bbci.co.uk/news/rss.xml"
print("Fetching news....")
news = feedparser.parse(rss_feed_url)
print("Fetched Successfully")
news.feed.title

news.feed.link
len(news.entries)

for i in range(len(news.entries)):   
    title = news.entries[i].title
    result_of_sentiment = sentiment(title)
    print(title, "-- >", result_of_sentiment)
    result.append(result_of_sentiment)
    

print(result)
count_of_positive = result.count("Positive")
count_of_negative = result.count("Negative")
count_of_neutral = result.count("Neutral")

labels = ["Positive","Negative","Neutral"]
values = [count_of_positive,count_of_negative,count_of_neutral]
plt.title("News demo")
plt.bar(labels,values)
plt.savefig("Chart.png")
plt.show()
print("Chart Saved !!")
