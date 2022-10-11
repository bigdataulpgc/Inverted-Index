# Inverted-index

This project is an implementation of an inverted index.

An inverted index is a way of structuring the information to be retrieved by a search engine. Thus, the goal is to create the data structure to perform a full-text search.

The implementation creates the indexes from a list with the path of a series of books, so that it indicates for each word in which books it appears and in which lines of each book.

You can learn about the project in depth at [LINK TO PAPER](https://github.com/Alvaroooooooo/Inverted-index/blob/main/Paper.pdf).

## DEVELOPERS:

- Álvaro Juan Travieso García
- Alba Martín Lorenzo
- Victoria Torres Rodríguez
- Joel Del Rosario Pérez
- Jorge Langlenton Ferreiro

## INSTRUCTIONS FOR USE:

The program requires three directories: 
- The first one with files whose extension has to be xml, each one refers to the metadata of a book.
- The second one with files whose extension has to be txt, and each one contains the content of a book.
- The third will be for storing the index, which will be a file with extension json.

* NOTE: For each document in xml there must be a txt, both with the same name, which will be the identifier of each book (for example book1.xml and book1.txt).

## PROJECT STATUS:
As documented in the attached paper, this project is NOT finished, as a series of future optimizations and performance improvements have been proposed. In summary, these are concentrated in two objects of study:
- The creation of a persister: Keeping the searches under the same directory with a high number of words in the inverted index does not allow us to exploit the minimum amount of time that would be used in future searches. For this reason, the future creation of a perisstor is proposed, which will allow us to divide the set of inverted indexes alphabetically, creating directories with the following structure: {aa, ab, ac...}
- Change the serialization format: It is true that one of the most direct conversion formats is JSON, since we use nested dictionaries as the main object in the inverted index. Despite this, there are other formats such as CSV and its variants that would allow us to exploit this data collected in studies oriented to BIG DATA.

## GETTING STARTED:
The minimum requirements for the execution of this project are:
- Latest version of Python 3.10 (if applicable), in order to avoid execution conflicts.
- Installation of libraries: stop-words and xmltodict
```
pip install stop-words
```
```
pip install xmltodict
```

## TECHNOLOGY USED:
The main technologies used have been the IDE PyCharm from JetBrains, where the development of this project has been supported.

