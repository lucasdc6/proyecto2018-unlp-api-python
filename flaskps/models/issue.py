class Issue(object):

    def __init__(self, db):
        self.db = db

    def all(self):
        sql = 'SELECT * FROM issues'

        return self.db.execute(sql).fetchall()

    def create(self, data):
        sql = """
            INSERT INTO issues (email, description, category_id, status_id)
            VALUES (:email, :description, :category_id, :status_id)
        """

        self.db.execute(sql, data)
        self.db.commit()

        return True
