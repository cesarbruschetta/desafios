"""  """
import requests
from requests.compat import urljoin, quote_plus
import bs4


class RedditThreads:

    base_url = "https://old.reddit.com"
    end_pont = "/r/{0}/top"
    raite_limit = 5000
    count_limit = 10
    threads = []

    def __init__(self, threads):
        self.threads = threads

    def get_score(self, item_bs):
        obj = item_bs.find(class_="score unvoted")
        if obj:
            try:
                return int(obj.get("title", "0"))
            except ValueError:
                return 0
        else:
            return 0

    def get_title(self, item_bs):
        return item_bs.find("a", class_="title may-blank").text or ""

    def get_link_title(self, item_bs):
        obj = item_bs.find("a", class_="title may-blank")
        if obj:
            return obj.get("href", "")
        else:
            return ""

    @property
    def results(self):
        result = {}
        for thread in self.threads:
            result[thread] = self.process_thread(thread)
        return result

    def process_thread(self, thread):

        result = []
        
        link_thread = urljoin(self.base_url, self.end_pont.format(thread))
        data = requests.get(link_thread, headers={"User-agent": "reddit_bot"})
        data.raise_for_status()

        full_html = bs4.BeautifulSoup(data.text, "html.parser")
        for item in full_html.find(class_="linklisting"):

            score = self.get_score(item)
            if score >= self.raite_limit:
                result.append(
                    {
                        "score": score,
                        "subreddit": self.end_pont.format(thread),
                        "title": self.get_title(item),
                        "link_comment": urljoin(self.base_url, self.get_link_title(item)),
                        "link_thread": link_thread,
                    }
                )
        return result
