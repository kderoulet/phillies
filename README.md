# Phillies Baseball R&D Questionnaire
## Part 1: Improved Palindrome

#### palindrome.py (given)
```py
def is_palindrone(s):
    r=""
    for c in s:
        r = c +r
    for x in range(0, len(s)):
        if s[x] == r[x]:
            x = True
        else:
            return False
    return x
```

I would propose that we make the following improvements to the palindrome algorithm:

1) We can reduce memory storage and improve run-time by choosing not to store a backward version (```r``` in the given algorithm) of the given string (```s```). Instead of comparing the original string with a revered version of itself, we can simply compare the first element of the string with last element, the second with the second-to-last, and so on. Thus we can eliminate lines 2-4.

2) We can accurately determine whether or not a string is a palindrome with ```n // 2``` comparisons, where n is equal to the length of the string. Because each comparison is between 2 elements of the string, we can set our loop (line 5) to iterate through the range ```(0, len(s) // 2)``` instead of through the full length of the string.

3) Instead of comparing ```s[x]``` with ```r[x]```, we can compare ```s[x]``` with ```s[-1-x]```, which will give us the correctly corresponding character in the string (see point 1).

4) The original algorithm errors when given an empty string input because we are returning ```x``` instead of ```True```. We can simplify a bit by returning ```False``` when ```s[x]``` is not equal to ```s[-1-x]```, and returning ```True``` only when we have iterated through the string without any unequal values.

5) Fix our spelling!

#### improved_palindrome.py
```py
def is_palindrome(s):
    for x in range(0, len(s) // 2):
        if s[x] != s[-1 - x]:
            return False
    return True
```

## Part 2: Determining a Qualifying Offer

### Solution

My solution for this problem is fairly simple:

1) Use the requests module and the bs4 (BeautifulSoup) module to scrape data from the webpage.
2) Clean up the data--remove unnecessary characters, remove empty entries, and convert the numbers stored in strings to integers. (More could be done here if we were worried about further corruption in our data source, but the below code will work fine for the given data source.).
3) Average the top 125 salaries, and print the average in a US dollar-cent format.

Below is my solution; commented code can be found in the qualifying-offer.py file.
#### qualifying-offer.py
```py
import bs4, requests
url = 'https://questionnaire-148920.appspot.com/swe/data.html'
res = requests.get(url) 
soup = bs4.BeautifulSoup(res.text, 'html.parser')
salaries = soup.find_all('td', class_='player-salary')
salaries = [ salary.get_text().replace('$', '').replace(',', '') for salary in salaries]
salaries = [num for num in salaries if num.isdigit()]
salaries = list(filter(None, salaries))
salaries = [int(salary) for salary in salaries] 
salaries.sort(reverse=True)
topSalaries = salaries[:125]
qualifyingOffer = sum(topSalaries) / 125
qualifyingOffer = '${:,.2f}'.format(qualifyingOffer)
print(qualifyingOffer)
```

### To Run
To run this solution:
1) Download this repository
2) Make sure that a version of python3 is installed on your machine (depending on configurations, this can be done on the command line with ```python --version``` or ```python3 --version```). If python3 is not installed, installation instructions specific to your machine can be found at https://docs.python-guide.org/starting/installation/.
3) Make sure that pip is installed on your machine with the command ```pip --version```. If pip is not installed, instructions can be found here: https://bootstrap.pypa.io/get-pip.py. 
4) After navigating to your local copy of the repository via command line, install the dependencies with the commands ```pip install requests``` and ```pip install beautifulsoup4```. The program can then be run with the command ```python3 qualifying-offer.py```.
5) The result will print in your command line; here are some examples of results I've gotten when running this solution:
![](result.png?raw=true)

Thank you for reading!