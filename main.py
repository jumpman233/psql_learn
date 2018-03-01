#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import datetime


def q1():
    db = psycopg2.connect("dbname=news")

    c = db.cursor()

    print "1. What are the most popular three articles of all time?"

    print ""

    c.execute('''
        SELECT title, count(*) as count
        FROM log, articles
        WHERE substr(log.path, 10) = articles.slug
        GROUP BY articles.title
        ORDER BY count DESC
        LIMIT 3;
        ''')

    data = c.fetchall()

    for i in data:
        print "● %(name)s - %(num)d" % {'name': i[0], 'num': i[1]}

    print ""

    db.close()


def q2():
    db = psycopg2.connect("dbname=news")

    print "2. Who are the most popular article authors of all time?"

    print ""

    c = db.cursor()

    c.execute('''
        SELECT name, count
        FROM (SELECT articles.author, count(*) AS count
            FROM log, articles
            WHERE substr(log.path, 10) = articles.slug
            GROUP BY articles.author
            ORDER BY count DESC
            LIMIT 4) AS t
        LEFT JOIN authors ON t.author = authors.id;
        ''')

    data = c.fetchall()

    for i in data:
        print "● %(name)s - %(num)d" % {'name': i[0], 'num': i[1]}

    print ""

    db.close()


def q3():
    db = psycopg2.connect("dbname=news")

    print "3. On which days did more than 1% of requests lead to errors?"

    print ""

    c = db.cursor()

    c.execute('''
        SELECT to_char(t.time, 'FMMonth DD, YYYY'), t.ratio
        FROM (
           SELECT CAST(c_4 AS float)/(c_4+c_2) AS ratio, time1 AS time
            FROM (SELECT count(*) AS c_2, time::date AS time1
                FROM log
                WHERE status
                LIKE '200%'
                GROUP BY time1
                ) AS t1
            LEFT JOIN (SELECT count(*) AS c_4,
                       time::date AS time2
                FROM log
                WHERE status
                LIKE '404%'
                GROUP BY time2
                ) AS t2
            ON t1.time1 = t2.time2
            ORDER BY ratio DESC
            ) AS t
        WHERE t.ratio >= 0.01;
        ''')

    data = c.fetchall()

    for i in data:
         print('{0} - {1:.2%} errors'.format(i[0], i[1]))

    print ""

    db.close()

if __name__ == '__main__':
    q1()
    q2()
    q3()
