from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
print(bs.find('img',
              {'src': '../img/gifts/img1.jpg'})
      .parent.previous_sibling.get_text())


# RegEx
##### aa*bbbbb(cc)*(d|e) #####
# aa* -> at least 1 a
# bbbbb -> 5 b
# (cc)* -> even number (pairs) of c ( 0 or more pairs )
# (d|e) -> one d or one e

# REGEX SYMBOLS TABLE
# * _ matches the preceding character, subexpression or bracketed character, 0 or more times
# + _ matches the preceding character, subexpression or bracketed character, 1 or more times
# [] _ matches any character within the brackets [A-Z]*
# () _ a grouped subexpression
# x{m,n} _ matches the preceding character, subexpression or bracketed character between m and n times
# [^] _ matches any single character that is not in the brackets
# | _ matches any character, string of characters or subexpression separated by the |
# . _ matches any single character (including symbols, nums, space etc) x.y
# ^ _ indicates that a character or subexpression occurs at the beginning of a string
# \ _ an escape character allows you to use special chars as their literal meanings
# $ _ often used at the end of a regular expression
# ?! _ dos not contain. This symbols indicates that that character should not be found in that specific place

# IDENTIFYING EMAIL ADRESSES
# [A-Za-z0-9._+]+@[A-Za-z]+.(com|org|edu|net)
