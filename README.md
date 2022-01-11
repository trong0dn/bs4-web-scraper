# bs4-web-scraper
A simple web scraper using Python3 with BeautifulSoup4 library to extract the latest feed of products from the Newegg website.  The resulting output was then written to a csv file. Long story made short, recently built a PC and looking for GPUs on the market. Thought it would be fun to web scrape some potential websites for comparing overall cost of the product.

## Dependencies
[BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) - Python library for pulling data out of HTML and XML files

## Installation

To get started, we need to download Python package manager.

```
// Windows Environment
> python -m pip install --upgrade pip
```

```
// Ubuntu-Linux Environment
$ sudo apt-get install python-pip
```

### Installing BeautifulSoup

As BeautifulSoup is not a standard library, we need to install it. We are going to use the BeautifulSoup 4 package (known as bs4).

```
// Window Environment
> pip install beautifulsoup4
```

```
// Ubuntu-Linux Environment
$ sudo apt-get install python3-bs4
```

## Deployment

```
# Clone
$ https://github.com/trong0dn/bs4-web-scraper.git

# Run script
$ python scraper.py
```

## Data Object Model

Parsing the HTML page is a commonly done using the Data Object Model (DOM) which is the data representation of the objects that comprise the structure and content of a document on the web. More traditionally, it is the programming interface for web documents where the page structure, style, and content is translated from script code.

## Acknowledgement

Thanks to my gaming friends for giving me the "push" to look for GPUs.

## Disclaimer

Copyright disclaimer under section 107 of the Copyright Act 1976, 
allowance is made for “fair use” for purposes such as criticism, 
comment, news reporting, teaching, scholarship, education and research.

Fair use is a use permitted by copyright statute that might otherwise 
be infringing.
