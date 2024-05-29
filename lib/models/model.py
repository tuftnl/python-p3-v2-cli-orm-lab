# lib/models/model.py
from models.__init__ import CURSOR, CONN
from models.make import Make


class Model:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, form_style, color, make_id, id=None):
        self.id = id
        self.name = name
        self.form_style = form_style
        self.color = color
        self.make_id = make_id

    def __repr__(self):
        return (
            f"<model {self.id}: {self.name}, {self.form_style}, {self.color} " +
            f"Make ID: {self.make_id}>"
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if isinstance(color, str) and len(color):
            self._color = color
        else:
            raise ValueError(
                "color must be a non-empty string"
            )



    @property
    def make_id(self):
        return self._make_id

    @make_id.setter
    def make_id(self, make_id):
        if type(make_id) is int and Make.find_by_id(make_id):
            self._make_id = make_id
        else:
            raise ValueError(
                "make_id must reference a make in the database")

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Employee instances """
        sql = """
            CREATE TABLE IF NOT EXISTS models (
            id INTEGER PRIMARY KEY,
            name TEXT,
            form_style TEXT,
            color TEXT,
            make_id INTEGER,
            FOREIGN KEY (make_id) REFERENCES makes(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Employee instances """
        sql = """
            DROP TABLE IF EXISTS models;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, job title, and department id values of the current Employee object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO models (name, form_style, color, make_id)
                VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.form_style, self.color, self.make_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Employee instance."""
        sql = """
            UPDATE models
            SET name = ?, form_style = ?, make_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.form_style,
                             self.make_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Employee instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM models
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, name, form_style, color, make_id):
        """ Initialize a new Employee instance and save the object to the database """
        model = cls(name, form_style, color, make_id)
        model.save()
        return model

    @classmethod
    def instance_from_db(cls, row):
        """Return an Employee object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        model = cls.all.get(row[0])
        if model:
            # ensure attributes match row values in case local instance was modified
            model.name = row[1]
            model.form_style = row[2]
            model.color = row[3]
            model.make_id = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            model = cls(row[1], row[2], row[3], row[4])
            model.id = row[0]
            cls.all[model.id] = model
        return model

    @classmethod
    def get_all(cls):
        """Return a list containing one Employee object per table row"""
        sql = """
            SELECT *
            FROM models
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Employee object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM models
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return Employee object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM models
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None