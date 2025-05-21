import feedparser
from datetime import datetime
from django.shortcuts import render

def index(request):
    feed_url = 'https://mashable.com/feed'
    feed = feedparser.parse(feed_url)

    articles = []
    for entry in feed.entries:
       
        published = datetime(*entry.published_parsed[:6])
        if published >= datetime(2015, 1, 1):
            articles.append({
                'title': entry.title,
                'link': entry.link,
                'date': published,
            })

   
    articles.sort(key=lambda x: x['date'], reverse=True)

    return render(request, 'aggregator/index.html', {'articles': articles})
