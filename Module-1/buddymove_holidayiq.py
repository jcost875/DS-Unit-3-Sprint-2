"""This file will build an empty DB, populate it with a table,
   define and run queries, then report the results"""
import sqlite3
import pandas as pd


# The following will save our csv url to a variable
url = "https://raw.githubusercontent.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv"
buddy_df = pd.read_csv(url)
buddy_df = buddy_df.rename(columns={'User Id': "User_Id"})

# The following will build a connection using our function
conn = sqlite3.connect("buddymove_holidayiq.sqlite3")


# The following will populate a table within the database with our dataframe
buddy_df.to_sql('review', con=conn, if_exists='replace')


# The following will define a function to run a query and return the results
def execute_query(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    results = curs.fetchall()
    curs.close()
    return results


# The following will define our queries
total_rows = """
    SELECT COUNT(*)
    FROM review;
"""


nature_shopping = """
    SELECT COUNT(*)
    FROM review
    WHERE Nature >= 100
    AND Shopping >= 100;
"""


sports_avg = """
    SELECT avg(Sports)
    FROM review;
"""


religious_avg = """
    SELECT avg(Religious)
    FROM review;
"""


nature_avg = """
    SELECT avg(Nature)
    FROM review;
"""


theatre_avg = """
    SELECT avg(Theatre)
    FROM review;
"""


shopping_avg = """
    SELECT avg(Shopping)
    FROM review;
"""


picnic_avg = """
    SELECT avg(Picnic)
    FROM review;
"""


# The following will automatically run the report upon opening the file and populate
# our report using our previously defined function and queries to create an easy to
# read output
if __name__ == "__main__":
    # The following will run our queries
    num_rows = execute_query(conn, total_rows)
    nat_shop = execute_query(conn, nature_shopping)
    sport_av = execute_query(conn, sports_avg)
    relig_av = execute_query(conn, religious_avg)
    natr_av = execute_query(conn, nature_avg)
    thet_av = execute_query(conn, theatre_avg)
    shop_av = execute_query(conn, shopping_avg)
    pic_av = execute_query(conn, picnic_avg)
    # The following will format our results for our report
    num_rows_output = num_rows[0][0]
    nat_shop_output = nat_shop[0][0]
    sport_av_output = round((sport_av[0][0]), 2)
    relig_av_output = round((relig_av[0][0]), 2)
    natr_av_output = round((natr_av[0][0]), 2)
    thet_av_output = round((thet_av[0][0]), 2)
    shop_av_output = round((shop_av[0][0]), 2)
    pic_av_output = round((pic_av[0][0]), 2)
    # The following print statements will place our results in an easy
    # to read, convenient way to read
    print(" ")
    print("There are", num_rows_output, "rows in our review table.")
    print(" ")
    print("There are", nat_shop_output, "users that reviewed over 100")
    print("in both the Nature and Shopping categories.")
    print(" ")
    print("The average review for the individual categories are:")
    print("Sports:", sport_av_output)
    print("Religious:", relig_av_output)
    print("Nature:", natr_av_output)
    print("Theater:", thet_av_output)
    print("Shopping:", shop_av_output)
    print("Picnic:", pic_av_output)
    print(" ")
    print("Thank you for reading!")
