from bs4 import BeautifulSoup
with open('./website.html', mode='r', encoding='utf-8') as file:
  html_doc = file.read()



my_soup = BeautifulSoup(html_doc, 'html.parser')
site_title = my_soup.title.string
print(my_soup.prettify())