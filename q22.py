from string import uppercase
from urllib import urlopen


page_text = urlopen('https://projecteuler.net/project/resources/p022_names.txt').read()
page_text_parsed = page_text.replace('"', '')
words = sorted(page_text_parsed.split(','))
print sum(sum(uppercase.index(c) + 1 for c in word) * (i + 1)
          for i, word in enumerate(words))
