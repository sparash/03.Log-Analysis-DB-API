#!/usr/bin/env python3
import psycopg2
DBNAME = "news"

query1 = """
        SELECT title, views
        FROM articles,
        (SELECT path, count(path) AS views
        FROM log
        GROUP BY log.path
        )  AS log
        WHERE log.path='/article/'||articles.slug
        ORDER BY views DESC
        LIMIT 3;
      """


query2 = """
        SELECT authors.name, count(*) as auth_views
        FROM articles, authors, log
        WHERE articles.author=authors.id AND
        log.path='/article/'||articles.slug
        GROUP BY authors.name
        ORDER BY auth_views DESC;
     """


query3 = """
        SELECT final.day,
        ROUND(((errors.err_req*1.0) / final.requests), 2) AS percent
        FROM (
          SELECT time::date AS day, count(*) AS err_req
          FROM log
          WHERE status LIKE '404%'
          GROUP BY day
        ) AS errors
        JOIN (
          SELECT time::date AS day, count(*) AS requests
          FROM log
          GROUP BY day
          ) AS final
        ON final.day = errors.day
        WHERE (ROUND(((errors.err_req*1.0) / final.requests), 2) > 0.01)
        ORDER BY percent DESC;
    """


def operations(statement):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(statement)
    var = c.fetchall()
    db.close()
    return var


print("Query Results:"+"\n")

print("What are the most popular three articles of all time?")
print("\n")
result1 = operations(query1)
count = 0
for i in result1:
    count += 1
    title = i[0]
    views = '" -- ' + str(i[1]) + " views"
    print(str(count) + '. ' + '"' + title + views)
print("\n")


print("Who are the most popular article authors of all time?")
print("\n")
result2 = operations(query2)
count = 0
for i in result2:
    count += 1
    author = i[0]
    views = '" -- ' + str(i[1]) + " views"
    print(str(count) + ". " + '"' + author + views)
print("\n")


print("On which days did more than 1% of requests lead to errors?")
print("\n")
result3 = operations(query3)
for i in result3:
    date = i[0].strftime('%B %d, %Y')
    err = str(round(i[1], 2))
    print(date + ' -- ' + err + "%" + " errors")
