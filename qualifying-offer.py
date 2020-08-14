#!python3
# webscraping code is borrowed from code I wrote while working through
# 'Automate the Boring Stuff' by Al Sweighart.
import bs4, requests
url = 'https://questionnaire-148920.appspot.com/swe/data.html'
res = requests.get(url) 
soup = bs4.BeautifulSoup(res.text, 'html.parser')
salaries = soup.find_all('td', class_='player-salary')
# clean up the salary data by removing $ and ,
salaries = [ salary.get_text().replace('$', '').replace(',', '') for salary in salaries]
salaries = [num for num in salaries if num.isdigit()] # filter out text entries
salaries = list(filter(None, salaries)) # filter out entries with missing salary data
salaries = [int(salary) for salary in salaries] # convert data to int
salaries.sort(reverse=True) # sort descending
topSalaries = salaries[:125] # select the highest 125 salaries
qualifyingOffer = sum(topSalaries) / 125
qualifyingOffer = '${:,.2f}'.format(qualifyingOffer) # taken from https://www.kite.com/python/answers/how-to-format-a-float-as-currency-in-python
print(qualifyingOffer)