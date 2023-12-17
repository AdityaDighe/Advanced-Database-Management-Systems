import xml.etree.ElementTree as ET

tree=ET.parse('books.xml')
root = tree.getroot()

def runqueries():

    for book in root.findall('book'):
        title=book.find('title').text
        author=book.find('author').text
        print(f"Title: {title}, Author: {author}")

    for book in root.findall('book'):
        year = book.find('year').text
        if year.startswith('2005'):
            title = book.find('title').text
            author = book.find('author').text
            print(f"Title: {title}, Author: {author}, Year: {year}")

runqueries()
