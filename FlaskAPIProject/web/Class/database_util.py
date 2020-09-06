import pyodbc


class database:
    def __init__(self, server_name, database_name):
        self.server_name = server_name
        self.database_name = database_name

    def open_con(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server={' + self.server_name + '};'
                                                              'Database={' + self.database_name + '};'
                                                                                                  'Trusted_Connection=yes;')
        cursor = conn.cursor()
        return cursor

    def jsonify(self, cursor):
        json_data = []
        row_headers = [x[0] for x in cursor.description]  # headers
        rv = cursor.fetchall()
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        return json_data
