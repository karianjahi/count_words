from count_words import CountWords
import pytest
class TestCountWords:

    def test_empty(self):
        assert CountWords("").count_words() == 0
    
    def test_one(self):
        assert CountWords("diana").count_words() == 1
    
    @staticmethod
    def test_multiple():
        words = "This bootcamp is extremely important for aspiring data scientists"
        assert CountWords(words).count_words() == 9
    
    def test_line_breaks(self):
        words = "This\nbootcamp\nis\nextremely\nimportant\nfor\naspiring\ndata\nscientists"
        assert CountWords(words).count_words() == 9
    
    def test_accents(self):
        words = "Cortège\nNaïve\nJalapeño"
        assert CountWords(words).count_words() == 3

    def test_html(self):
        words = "<h1> This is a heading </h1>"
        assert CountWords(words).count_words() == 4
    
    def test_html_with_attributes(self):
        words = '<h1 class="bootcamp"> This is some bootcamp code </h1>'
        assert CountWords(words).count_words() == 5
    
    def test_html_with_more_attributes(self):
        words = '<h2 id="924" class="bootcamp">Try me</h2>'
        assert CountWords(words).count_words() == 2
    
    def test_dashes(self):
        words = "John-Peter-Simons"
        assert CountWords(words).count_words() == 3
    
    def test_non_string_type(self):
        words = ["I have a story about my life at university"]
        with pytest.raises(Exception) as error:
            CountWords(words).count_words(words)
        assert "input should be string" in str(error.value)
            
# Test parameterizations - many tests in one
my_tests = [( "<h1> This is a heading </h1>", 4), 
('<h1 class="bootcamp"> This is some bootcamp code </h1>', 5), 
( "John-Peter-Simons", 3), ("This\nbootcamp\nis\nextremely\nimportant\nfor\naspiring\ndata\nscientists", 9)]
@pytest.mark.parametrize('input, output', my_tests)
def test_all_tests(input, output):
    assert CountWords(input).count_words() == output