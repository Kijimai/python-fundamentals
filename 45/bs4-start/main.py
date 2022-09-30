from bs4 import BeautifulSoup

with open('./website.html', mode='r', encoding='utf-8') as file:
    html_doc = file.read()


my_soup = BeautifulSoup(html_doc, 'html.parser')
site_title = my_soup.title.string

all_lists = my_soup.find_all(name='li')
all_anchors = my_soup.find_all(name="a")

# for list in all_lists:
#     print(list.getText())

for anchor in all_anchors:
    # print(anchor.getText()) # Get the text content of an anchor tag
    print(anchor.get('href'))  # Get the contents of an href

section_heading = my_soup.find(name="h3", class_="heading")
print(section_heading)

# selected via unga bunga
# first_anchor = my_soup.find(name="p").find(name="em").find(name="strong").find(name="a")
# print(first_anchor)

# selected via css selectors
first_anchor = my_soup.find(class_="site-link")
print(first_anchor)

# select the first matching item, think queryselectors
# a tag nested within a p tag
company_url = my_soup.select_one(selector="p a")
print(company_url)

# quicker way of doing the same thing
section_heading_select= my_soup.select(".heading")
print(section_heading_select)
