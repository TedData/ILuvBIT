

'''
        /*
         * Please implement the Task 1 code here, including both two sub-tasks
         */
'''

import src.oracle.DBconnect as db
from src.data.restaurant import restaurant as res

try:
    con = db.create_connection()
    cur = db.create_cursor(con)
    string_query1 = "SELECT COUNT(CITY) FROM RESTAURANT WHERE CITY like 'new york_'"
    string_query2 = "SELECT COUNT(CITY) FROM RESTAURANT WHERE CITY like 'new york city_'"
    string_query3 = "SELECT COUNT(distinct(CITY)) FROM RESTAURANT"
    restaurants = []
    cur.execute(string_query1)
    for city in cur:
        restaurant = res()
        restaurant.set_city(city)
        Number1 = str(restaurant.get_city())
        print('new york,', Number1[1:4])
    cur.execute(string_query2)
    for city in cur:
        restaurant = res()
        restaurant.set_city(city)
        Number2 = str(restaurant.get_city())
        print('new york city,',Number2[1:3])
    cur.execute(string_query3)
    for city in cur:
        restaurant = res()
        restaurant.set_city(city)
        Number3 = str(restaurant.get_city())
        print('Number of distinct value in city:',Number3[1:3])
    cur.close()
    con.close()
except:
    print("Error occurred. Statement execution failed.")
