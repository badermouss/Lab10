from database.DB_connect import DBConnect
from model.contiguity import Contiguity
from model.countries import Country


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getAllCountries():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM country
                 order by StateNme asc"""
        cursor.execute(query)

        for row in cursor:
            result.append(Country(row["StateAbb"],
                                  row["CCode"],
                                  row["StateNme"],
                                  0)
                          )

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(idMap, anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select c.state1no as c1, c.state2no as c2
                    from contiguity c
                    where c.conttype = 1 
                    and c.`year` < %s
                    """
        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(Contiguity(idMap[row["c1"]],
                                     idMap[row["c2"]],
                                     )
                          )
        cursor.close()

        cursor = conn.cursor(dictionary=True)
        query = """select c.state1no as c1, c.state2no as c2
                    from contiguity c
                    where c.`year` < %s
                            """
        cursor.execute(query, (anno,))
        countries = []
        for row in cursor:
            if idMap[row["c1"]] not in result:
                countries.append(idMap[row["c1"]])
            if idMap[row["c2"]] not in result:
                countries.append(idMap[row["c2"]])
        cursor.close()
        conn.close()
        return result, countries
