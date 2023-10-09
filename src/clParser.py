import lxml.html as html
import requests

class Parse:
    def parser_func(self, url):
        req = requests.get(url)
        home = req.content.decode('utf-8')

        parser = html.fromstring(home)
        return parser