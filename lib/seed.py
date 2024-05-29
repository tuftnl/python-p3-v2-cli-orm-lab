#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from lib.models.make import Make
from lib.models.model import Model

def seed_database():
    Model.drop_table()
    Make.drop_table()
    Make.create_table()
    Model.create_table()

    # Create seed data
    toyota = Department.create("Toyota", "Japan")
    ford = Department.create("Ford", "USA")
    jeep = Department.create("Jeep", "USA")
    nissan = Department.create("Nissan", "Japan")
    Employee.create("4Runner", "SUV", "Black", toyota.id)
    Employee.create("Tacoma", "Truck", "Silver", toyota.id)
    Employee.create("Sequoia", "SUV", "White", toyota.id)
    Employee.create("F150", "Truck", "Black", ford.id)
    Employee.create("Mustang", "Coupe", "Yellow", ford.id)
    Employee.create("Bronco", "SUV", "Blue", ford.id)
    Employee.create("Wrangler", "SUV", "Green", jeep.id)
    Employee.create("Grand Cherokee", "SUV", "White", jeep.id)
    Employee.create("Wagoneer", "SUV", "Tan", jeep.id)
    Employee.create("Compass", "SUV", "Red", jeep.id)
    Employee.create("Pathfinder", "SUV", "Green", nissan.id)
    Employee.create("Titan", "Truck", "White", nissan.id)
    Employee.create("Xterra", "SUV", "Blue", nissan.id)


seed_database()
print("Seeded database")
