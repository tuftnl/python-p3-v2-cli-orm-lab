#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.make import Make
from models.model import Model
import ipdb

def reset_database():
    Model.drop_table()
    Make.drop_table()
    Make.create_table()
    Model.create_table()

    # Create seed data
    toyota = Make.create("Toyota", "Japan")
    ford = Make.create("Ford", "USA")
    jeep = Make.create("Jeep", "USA")
    nissan = Make.create("Nissan", "Japan")
    
    Model.create("4Runner", "SUV", "Black", toyota.id)
    Model.create("Tacoma", "Truck", "Silver", toyota.id)
    Model.create("Sequoia", "SUV", "White", toyota.id)
    Model.create("F150", "Truck", "Black", ford.id)
    Model.create("Mustang", "Coupe", "Yellow", ford.id)
    Model.create("Bronco", "SUV", "Blue", ford.id)
    Model.create("Wrangler", "SUV", "Green", jeep.id)
    Model.create("Grand Cherokee", "SUV", "White", jeep.id)
    Model.create("Wagoneer", "SUV", "Tan", jeep.id)
    Model.create("Compass", "SUV", "Red", jeep.id)
    Model.create("Pathfinder", "SUV", "Green", nissan.id)
    Model.create("Titan", "Truck", "White", nissan.id)
    Model.create("Xterra", "SUV", "Blue", nissan.id)


reset_database()
ipdb.set_trace()