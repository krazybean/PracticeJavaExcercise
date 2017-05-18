import os
from os.path import expanduser
import sqlite3

SQLITE_DB = "{0}/.advertiser.db".format(expanduser("~"))


class Advertiser(object):

    def __init__(self):
        self.Name = None
        self.Contact = None
        self.CreditLimit = None

    def _connect(self):
        """ Creates database if it does not exist or connects """
        if not os.path.isfile(SQLITE_DB):
            conn = sqlite3.connect(SQLITE_DB)
            create = ''' CREATE TABLE IF NOT EXISTS `advertise`
                (id INTERGER AUTO INCREMENT PRIMARY KEY,
                 name CHAR(120) NOT NULL,
                 contact TEXT,
                 credit_limit INTERGER,
                 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);
            '''
            conn.execute(create)
            conn.commit()
            conn.close()
        conn = sqlite3.connect(SQLITE_DB)
        return conn

    def _select(self, conn, name):
        """ Queries database for searching advertiser by name

        Args:
            conn (obj): Connection object
            name (str): Advertiser name to be retrieved
        Returns:
            record (str): Full record response
        """
        SELECT = ''' SELECT id, name, contact, credit_limit, timestamp
               FROM advertise WHERE name = ?; '''
        cur = conn.cursor()
        cur.execute(SELECT, [name])
        response = {}
        try:
            for row in cur.fetchall():
                response['id'] = row[0]
                response['name'] = row[1]
                response['contact'] = row[2]
                response['credit_limit'] = row[3]
                response['timestamp'] = row[4]
            return response
        except Exception as e:
            return None

    def _insert(self, conn, name, contact, credit_limit):
        """ Inserts JWT token by key encrypted for storage

        Args:
            conn (obj): Connection object
            name (str): Advertiser Name
            contact (str): Advertiser Contact
            credit_limit (int): Advertiser Credit Limit
        Returns:
            No value returned
        """
        INSERT = ''' INSERT INTO advertise (name, contact, credit_limit)
                VALUES (?, ?, ?);
            '''
        setup = {'name': name,
                 'contact': contact,
                 'credit_limit': credit_limit}
        conn.execute(INSERT, [name, contact, credit_limit])
        conn.commit()

    def _delete(self, conn, name):
        """ Deletes Advertiser based on name for simplicity

        Args:
            conn (obj): Connection object
            name (str): Name of the advertiser to be deleted
        Returns:
            No value returned
        """
        DELETE = ''' DELETE FROM advertise WHERE name = ?; '''
        conn.execute(DELETE, [name])
        conn.commit()

    def add(self, Name, Contact, CreditLimit):
        conn = self._connect()
        self._insert(conn, Name, Contact, CreditLimit)
        return 0

    def get(self, Name):
        conn = self._connect()
        result = self._select(conn, Name)
        return result

    def delete(self, Name):
        conn = self._connect()
        self._delete(conn, Name)
        return 0
