import requests


class News_App:
    API_KEY = "9d4ecb64e5bd4a64bbbfd2a820a5dec0"
    BASE_URL = "https://newsapi.org/v2/everything?"
    LIMIT = 10

    def get_news_by_topic(self, topic):
        url = self.BASE_URL + f"q={topic}&apiKey={self.API_KEY}"

        req = requests.get(url)
        res = req.json()

        # print(res)

        if (res["status"] != "ok"):
            print("Something went wrong! Please try again.")

        total_results = res["totalResults"]
        print(f"{total_results} total results.")
        print(f"Showing top {self.LIMIT} results")

        articles = res["articles"]

        title = []
        publish_time = []
        source = []
        urls = []

        for article in articles:
            title.append(article["title"])
            urls.append(article["url"])
            source.append(article["source"]["name"])
            publish_time.append(article["publishedAt"].split("T")[0])

        for i in range(self.LIMIT):
            print("-" * 60)
            print(
                f"{i+1}. {title[i]} \nposted by {source[i]} on {publish_time[i]}\nurl:- {urls[i]}.")
            print("-" * 60)

    def get_breaking_news(self):
        print("-" * 60)
        print(f"Breaking News")
        print("-" * 60)

        self.get_news_by_topic("breaking")


while True:
    user_input = input(
        "what news you want to read? enter a topic or phrase like 'Breaking' \nexit to quit: ").lower()
    if (user_input in ['exit', 'Exit', 'EXIT', 0, 'quit', '0', '']):
        print('quiting')
        break

    print(f"\nShowing news related to query {user_input}.")
    newsApp = News_App()
    newsApp.get_news_by_topic(user_input)

    # newsApp.get_breaking_news()
    # newsApp.get_news_by_topic("space")
