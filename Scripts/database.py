import sqlite3


class DataBase:
    def __init__(self, database):
        self.database = database

    def build(self):
        def new_table(request):
            try:
                self.request(request)
            except:
                print(request[:request.find(
                    "(")-1].replace("CREATE TABLE ", ""), " already exist")

        new_table("""
                    CREATE TABLE "Blacklist" (
                    	"ID"	INTEGER NOT NULL UNIQUE,
                    	"Blacklist"	TEXT,
                    	PRIMARY KEY("ID" AUTOINCREMENT)
                    );
                    """)

    def request(self, request, values=[]):
        def db_data_format(cursor, row):
            d = {}
            for idx, col in enumerate(cursor.description):
                d[col[0]] = row[idx]
            return d

        conn = sqlite3.connect(self.database)
        c = conn.cursor()
        c.row_factory = db_data_format

        try:
            c.execute(request, values)
            datos = c.fetchall()
        except:
            datos = ["Error"]

        conn.commit()
        conn.close()
        return datos

    def get_schema(self, table_name, raw=False):
        data = self.request("PRAGMA table_info(%s)" % table_name)
        if raw:
            return data
        return [col['name'] for col in data]

    def get_table(self, table, config=None):

        rows = self.request("SELECT * FROM %s ORDER BY ID" % table)

        columns = list(rows[0].keys()) if rows else self.get_schema(table)
        key_col = [c['name']
                   for c in self.get_schema(table, raw=True) if c['pk']][0]

        autoincrement_table = self.request(
            'SELECT COUNT(*) aut FROM sqlite_sequence WHERE name="%s";' % (table))[0]['aut']
        if autoincrement_table and 'ID' in columns:
            columns.remove('ID')

        table_response = {'header': columns,
                          'rows': rows,
                          'title': table,
                          'key': key_col
                          }
        if config:
            table_response.update({
                'newEntry': {'columns': self.get_schema(table, raw=True),
                             'table': table},
                'delete': True})
            if autoincrement_table:
                table_response['newEntry']['columns'].pop(0)

        return table_response

    def get_tables(self):
        data = self.request(
            """SELECT * FROM sqlite_master WHERE type = 'table'""")
        return data

    def insert(self, data):

        tablename = data['table']

        values = [
            data[col] if col in data else None for col in self.get_schema(tablename)]

        if self.request('SELECT COUNT(*) autoincrm FROM sqlite_sequence WHERE name="%s";' % (tablename))[0]['autoincrm']:
            values[self.get_schema(tablename).index('ID')] = None

        self.request("INSERT INTO %s VALUES (%s)" % (tablename, ", ".join(["?"]*len(values))),
                     (*values,))

    def delete(self, tablename, key):
        key_col = [c['name']
                   for c in self.get_schema(tablename, raw=True) if c['pk']][0]
        self.request("DELETE FROM %s WHERE %s = ?" %
                     (tablename, key_col), (key,))

    def edit(self, tablename, key, data):
        print(tablename, key, data)
        key_q = "%s = %s" % (key, data[key])
        if 'table' in data:
            del data['table']
        data_q = ",".join(["%s='%s'" % (k, v) for k, v in data.items()])

        self.request("""
                    UPDATE %s
                    SET %s
                    WHERE %s;
                      """ % (tablename, data_q, key_q))


if __name__ == "__main__":
    pass
