__author__ = 'ankit'

import sqlparse

class SQLParser:

    def __init__(self, query):
        self.query = query.replace("'","")
        self.stmt = None


    #Add more error handling
    def parse(self):
        res = sqlparse.parse(self.query)
        if res: stmt = res[0]

        if stmt is not None and stmt.get_type() == "SELECT":
            self.stmt = stmt
            return stmt

    def understand(self):

        table = ""

        for token in self.stmt.tokens:
            if token.is_keyword and token.value.lower() == "from":
                table = self.stmt.token_next(self.stmt.token_index(token), skip_ws=True)
                break

        return table
