"""This file will define and run our queries then print out the report results
   for our rpg_db assignment."""
import sqlite3


# This will define a function to create a connection to the database
def connect_to_db(db_name="rpg_db.sqlite3"):
    return sqlite3.connect(db_name)


# This will define a function to make a cursor through our 
# connection object, run our queries from the associated file, 
# then return the results of the query
def execute_query(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    results = curs.fetchall()
    curs.close()
    return results


# This will create a function to get the sum of our query
# result lists
def list_sum(list):
    total = []
    for i in range(len(list)):
        total.append(list[i][0])
    return sum(total)


# The following lines will define our queries
total_characters = """
    SELECT character_id
    FROM charactercreator_character;
"""

total_cleric = """
    SELECT character_ptr_id
    FROM charactercreator_cleric;
"""

total_fighter = """
    SELECT character_ptr_id
    FROM charactercreator_fighter;
"""

total_mage = """
    SELECT character_ptr_id
    FROM charactercreator_mage
    WHERE character_ptr_id
    NOT IN (SELECT mage_ptr_id
    FROM charactercreator_necromancer);
"""

total_necromancer = """
    SELECT mage_ptr_id
    FROM charactercreator_necromancer;
"""

total_thief = """
    SELECT character_ptr_id
    FROM charactercreator_thief;
"""

total_items = """
    SELECT item_id
    FROM armory_item;
"""

weapons = """
    SELECT item_ptr_id
    FROM armory_weapon;
"""

non_weapons = """
    SELECT item_id
    FROM armory_item
    WHERE item_id
    NOT IN (SELECT item_ptr_id
    FROM armory_weapon);
"""

# NOTE: For the following 2 functions, a LIMIT 20 would
# normally be desired. However, for a more precise report,
# it has been ommitted not because I misread the instructions,
# but out of a desire to attempt to tie today's lesson to lessons
# taught prior as well.
character_items = """
    SELECT COUNT(item_id) as total_items
    FROM charactercreator_character_inventory
    GROUP BY character_id;
"""

character_weapons = """
    SELECT COUNT(item_id) as total_weapons
    FROM charactercreator_character_inventory
    WHERE item_id
    IN (SELECT item_ptr_id
    FROM armory_weapon)
    GROUP BY character_id;
"""

# This will automatically run the report upon opening the file by
# using our functions to pull our queries and return the results
# in an easy to read format
if __name__ == "__main__":
    conn = connect_to_db()
    # The following lines will focus on the number of characters both in total
    # and in their respective rpg classes
    total_chars = execute_query(conn, total_characters)
    total_clers = execute_query(conn, total_cleric)
    total_fight = execute_query(conn, total_fighter)
    total_mags = execute_query(conn, total_mage)
    total_necs = execute_query(conn, total_necromancer)
    total_thfs = execute_query(conn, total_thief)
    # The following lines will focus on the number of items and weapons
    total_item = execute_query(conn, total_items)
    total_weap = execute_query(conn, weapons)
    # The following lines will focus on items and weapons carried by
    # the characters individually
    char_items = execute_query(conn, character_items)
    char_weaps = execute_query(conn, character_weapons)
    # The following lines will focus on the sums/averages of our
    # character inventory query results
    total_char_items = list_sum(char_items)
    total_char_weaps = list_sum(char_weaps)
    # The following will round the averages to easy to read decimals
    avg_char_items = round((total_char_items/len(char_items)), 2)
    avg_char_weaps = round((total_char_weaps/len(char_weaps)), 2)
    # The following print statements place our above results in
    # a convenient, easy to read print out
    print("There are", len(total_chars), "characters.")
    print(len(total_clers), "are Clerics,")
    print(len(total_fight), "are Fighters,")
    print(len(total_mags), "are Mages,")
    print(len(total_necs), "are Necromancers,")
    print("and", len(total_thfs), "are Thieves.")
    print(" ")
    print("There are", len(total_item), "items in the game,")
    print("of which", len(total_weap), "are weapons.")
    print(" ")
    print("There are", total_char_items, "items being carried by characters,")
    print("of which", total_char_weaps, "are weapons.")
    print(" ")
    print("This works out to an average of", avg_char_items, "items and")
    print(avg_char_weaps, "weapons being carried by each character.")
    