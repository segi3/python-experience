from bs4 import BeautifulSoup
import requests
import csv

url = "https://pokemondb.net/pokedex/all"

html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "lxml")

# * print html markdown
# print(soup.prettify())

# * print title
# print(soup.title.text)

# * print all links and its meta
# for link in soup.find_all("a"):
#     print("Inner Text: {}".format(link.text))
#     print("Title: {}".format(link.get("title")))
#     print("href : {}".format(link.get("href")))
#     print("\n")

# * search for table
target_table = soup.find("table", attrs={"id": "pokedex"})
target_table_data = target_table.find_all("tr")

# with open("pokedex_data.txt", "w", encoding="utf-8") as text_file:
#     print(f"{target_table_data[0]}", file=text_file)

# * append table head
headings = []
for th in target_table_data[0].find_all("th"):
    # print(th.text)
    headings.append(th.text.replace('\n', '').strip())

# * make 2d list
rows, cols = (1000, 10)
data = [[0 for i in range(cols)] for j in range(rows)]

# * append table body
for x in range(1, 1000):
    # print(f"\nx: {x}")
    for td, j in zip(target_table_data[x].find_all("td"), range(0, 10)):
        # print(td.text)
        data[x][j] = td.text.replace('\n', '').strip()

data[0] = headings # append head to data
# print(data)

# * write to csv
with open('poke_csv.csv', 'w+', newline='', encoding="utf-8") as csv_file:
    csvWriter = csv.writer(csv_file, delimiter=',')
    csvWriter.writerows(data)

# * write to txt file
f = open("Output.txt", "w+", encoding="utf-8")
for td in data:
    for entry in td:
        f.write(f"{entry} ")
    f.write("\n")
f.close()


