import random

import MySQLdb

##from passover import *

#Make sure to insert MySQL Workbench password



#User Information
class Forgett_User:
    def __init__(self, FirstName, LastName, Email, UserName, UserPassword, UserID=None):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.UserName = UserName
        self.UserPassword = UserPassword
        self.UserID= UserID

    # def __str__(self):
    #     return f"{self.UserID}, {self.FirstName}, {self.LastName}"










class LostObject:
    def __init__(self, ItemName, UserID):
        self.UserID = UserID
        self.ItemName = ItemName
        self.locations = {}


    def add_location(self, location):
        if location in self.locations:
            self.locations[location] += 1
        else:
            self.locations[location] = 1


    def most_likely_location(self):
        if not self.locations:
            return None
        # Find the location with the maximum count
        return max(self.locations, key=self.locations.get)



user1 = Forgett_User(
    UserID="1",
    FirstName="John",
    LastName="Doe",
    Email="John@Doe.co.il",
    UserName="JohnDoe",
    UserPassword="12345678",

)


item1 = LostObject(
    ItemName="keys",
    UserID=user1.UserID
)

# Adding locations
item1.add_location("table")
item1.add_location("table")
item1.add_location("kitchen counter")



db_connection = MySQLdb.connect(
    host="localhost",
    user="root",
    password="INSERTHEREPASSWORD",
    database="passover",
    port=3306

)

# def add_user_to_db(user: Forgett_User, connection):
#     db_cursor = db_connection.cursor()
#     db_cursor.execute(f"""
#     INSERT INTO Users VALUES({user1})
#     """)
#     db_connection.commit()
#
def add_user_to_db(user: Forgett_User, connection):
    try:
        db_cursor = connection.cursor()
        insert_query = """
        INSERT INTO Users (UserID, FirstName, LastName, Email, UserName, UserPassword)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        user_data = (user.UserID, user.FirstName, user.LastName, user.Email, user.UserName, user.UserPassword)
        db_cursor.execute(insert_query, user_data)
        connection.commit()
    except MySQLdb.Error as e:
        print(f"Error: {e}")

print("The most likely location for the item is:", item1.most_likely_location())
add_user_to_db(user1, db_connection)
print(user1)


def check_username_availability():
    pass


def check_email_availability():
    pass


def update_user_data():
    pass


def create_a_new_user(connection):
    new_user = Forgett_User(
        UserID=int(input("Enter your new user ID: ")),
        FirstName=int(input("Enter your first name: ")),
        LastName=int(input("Enter your last name: ")),
        Email=int(input("Enter your email address: ")),
        UserName=int(input("Enter your username: ")),
        UserPassword=int(input("Enter your password: ")),

    )
    add_user_to_db(new_user, connection)