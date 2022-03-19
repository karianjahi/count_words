from pyexpat import features
from bs4 import BeautifulSoup
import re
class CountWords:
    def __init__(self, words):
        assert isinstance(words, str), "input should be string"
        self.words = words
    
    def count_words(self):
        # Find out if the document is a html object
        self.run_words_through_html
        self.replace_dashes
        splits = self.words.split()
        return len(splits)
    
    @property
    def run_words_through_html(self):
        """
        Find out if a set of words are entrapped in html
        @property converts the method into an attribute
        """
        bs4_object = BeautifulSoup(self.words, features="html.parser")
        list_elements = bs4_object.find_all()
        if len(list_elements) > 0:
            self.words = bs4_object.get_text()
    
    @property
    def replace_dashes(self):
        """
        In case words are separated by dashes!
        """
        self.words = re.sub("-", " ", self.words)



if __name__ == "__main__":
    # print(CountWords("Jeshi la wazee").count_words())
    # print(CountWords("Jeshi").count_words())
    # print(CountWords("").count_words())
    # print(CountWords("<h1> This is a heading </h1>").count_words())
    html = "<h1> This is a heading </h1>"
    #html = "924r"
    bs = BeautifulSoup(html, features="html.parser")
    print(bs.find_all())
    print(bs.get_text())