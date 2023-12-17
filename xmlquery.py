import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('books.xml')
root = tree.getroot()

# Define a function to run queries on the XML data
def run_queries():
    # Query 1: Retrieve all book titles and authors
    for book in root.findall('book'):
        title = book.find('title').text
        author = book.find('author').text
        print(f"Title: {title}, Author: {author}")

    # Query 2: Retrieve books published in the year 2005
    for book in root.findall('book'):
        year = book.find('year').text
        if year.startswith('2005'):
            title = book.find('title').text
            author = book.find('author').text
            print(f"Title: {title}, Author: {author}, Year: {year}")

# Run the queries
run_queries()

