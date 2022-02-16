<h1 align=center>
Workshop-Scraping
</h1>

# Summary
- [Discovery](#discovery)
- [Install](#install)
- [Discovery](#discovery)
- [Install](#install)
- [First Part : Python Basis](#first-part--python-basis)
- [Second Part : Scraping Basis](#second-part--scraping-basis)
- [Third Part : Advanced Scraping](#third-part--advanced-scraping)

# Discovery

In this workshop you will learn how to use Scrapy framework with python.

## What is scraping?

Scraping generally defines a technique for extracting content (informations) from one or more websites in a completely automatic way. These are scripts, computer programs, which are responsible for extracting this information.

## Why use scraping ?

Scraping, web scraping or harvesting, has several uses. First, it allows to reuse content present on a website to display it on another website, and thus multiply without effort the number of pages with the same content. This technique, assimilated to the plundering or pumping of content, participates in a better referencing of a website, except when it is detected by the algorithms of the search engines (which sanction it severely). 

Scraping can also be used as a competitor monitoring tool (we automatically retrieve the prices charged by a competitor's e-commerce site and we detect their variations) or as a competitive intelligence tool.

A spider is a bot who get informations wanted. In this workshop you will learn how to create your spiders.

# Install

1- Install python

https://docs.python-guide.org/starting/install3/linux/

2- Install Scrapy

```shell
pip install Scrapy
```

### Setup

Fork this repository, and push code throughout the activity


# First Part : Python Basis

## Exercise 1

Print every number between 1 and 100 as follows:

- For every multiple of 3 print "Three".
- For every multiple of 5 print "Five".
- And for every multiple of both 3 and 5 print "ThreeFive"

The output should be as follows:
 
```shell
1
2
Three
4
Five
Three
7
8
Three
Five
11
Three
13
14
ThreeFive
16
```

## Exercise 2

Determine whether a positive integer number is colorful or not.

263 is a colorful number because [2, 6, 3, 2x6, 6x3, 2x6x3] are all different; whereas 236 is not colorful, because [2, 3, 6, 2x3, 3x6, 2x3x6] have 6 twice.

So take all consecutive subsets of digits, take their product and ensure all the products are different.

Examples:

```shell
263  -->  true
236  -->  false
2532 -->  false
```
## Exercise 3

Write a function calculate that takes a list of strings a returns the sum of the list items that represents an integer (skipping the other items).

Examples :

```shell
calculate(['4', '3', '-2']) ➞ 5
calculate(453) ➞ False
calculate(['nothing', 3, '8', 2, '1']) ➞ 9
calculate('54') ➞ False
```

## Exercise 4

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none.

Examples:

```shell
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
```

# Second Part : Scraping Basis

Create your scrapy projet :

```shell
scrapy startproject worshop-scraping
```

## Setup your spider

First we need to create our scrapy folder :

```shell
scrapy startproject folder_name
```

After, we have to generate the first spider:

```shell
scrapy genspider spider_name
```

To launch your spider :

```shell
scrapy crawl spider_name
```
## Exercise 1

To begin, we have to implement the items.py file with the following fields :  name, description, id, current_url, image, detail_link, price, old_price, availability, flag

https://docs.scrapy.org/en/latest/topics/items.html#declaring-item-subclasses


## Exercise 2

Then get the title product of each items in this page :

https://webscraper.io/test-sites/e-commerce/static

You need to work on your spider, that is to say in the file generate in previous steps.

The keyword "yield" can maybe help you.

Don't forget : You spider is a bot, you have to automise the recuperation of the data with selectors.

https://docs.scrapy.org/en/latest/topics/selectors.html

## Exercise 3

In the same way, you have to get the following informations about all the products present on the website :

- detail_link
- description
- price
- image(s)
- rating (number of stars)
- review count

## Exercise 4

Here we have scraped all the informations of all products present in the page. But we have only scrap the first page of the list, now it's time to do all the pages.

https://webscraper.io/test-sites/e-commerce/static/computers/laptops

Go on this website and scrap, on the same way, all products to all pages.

## Exercise 5

Now we that we have scrap all the products of all the page, we will scrap all the last categories.

On the same way scrap on https://webscraper.io/test-sites/e-commerce/static, all the products of each page on each category.


# Third Part : Advanced scraping

Does the same as the second part with this link
https://www.materiel.net/ordinateur-de-bureau/c401/

You have to recreate a python file in the same place of your previous spider.

You need to complete all fields present in items class.
