#!/usr/bin/env python2.7

import psycopg2

from prettytable import from_db_cursor

DBNAME = 'news'


def get_popular_articles():

    """Return most popular articles."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query_popular_articles = """
    SELECT art.title, COUNT(lg.id) as views
    FROM articles as art
    JOIN log as lg
    ON art.slug = substring(lg.path,10)
    AND lg.status = '200 OK'
    GROUP BY art.title
    ORDER BY views desc
    LIMIT 3; """
    c.execute(query_popular_articles)
    articles = from_db_cursor(c)
    db.close()
    return articles


def get_popular_authors():

    """Return most popular authors."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query_popular_authors = """
    SELECT aut.name, COUNT(lg.id) AS views
    FROM articles AS art
    JOIN log AS lg ON art.slug = SUBSTRING(lg.path,10)
    AND lg.status = '200 OK'
    JOIN authors AS aut ON aut.id = art.author
    GROUP BY aut.name
    ORDER BY views desc; """
    c.execute(query_popular_authors)
    authors = from_db_cursor(c)
    db.close()
    return authors


def get_days_rate():

    """Return days with errors more than 1%."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query_days_rate = """
    SELECT * FROM (SELECT TO_CHAR(time::date,'Mon DD, YYYY') AS date,
    ROUND((COUNT(status) FILTER (
    WHERE status='404 NOT FOUND'))*100/COUNT(status)::decimal, 2)::text
    ||'% errors' AS rate
    FROM log
    GROUP BY time::date) AS error_rate
    WHERE rate::text > 1::text;"""
    c.execute(query_days_rate)
    rates = from_db_cursor(c)
    db.close()
    return rates


def app():

    """Method to execute all methods"""
    articles_list = get_popular_articles()
    authors_list = get_popular_authors()
    rates_list = get_days_rate()
    file = open('results.txt', 'w+')
    file.write('Most Popular Articles\n')
    file.write('%s\n' % articles_list)
    file.write('\n')
    file.write('Most Popular Authors\n')
    file.write('%s\n' % authors_list)
    file.write('\n')
    file.write('Days with error rate > 1%\n')
    file.write('%s\n' % rates_list)


if __name__ == '__main__':
    app()
