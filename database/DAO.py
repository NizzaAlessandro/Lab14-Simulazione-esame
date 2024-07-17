from database.DB_connect import DBConnect
from model.edges import Archi


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getNodes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=False)
        query = """select distinct g.Chromosome
from genes g 
where g.Chromosome > 0 """

        cursor.execute(query, ())

        for row in cursor:
            result.append(row[0])

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getEdges():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ with tab as		(select distinct g1.Chromosome c1,g2.Chromosome c2, i.Expression_Corr val
				from genes g1 , genes g2 , interactions i 
				where (g1.Chromosome!= 0 and g2.Chromosome != 0 ) 
				and (g1.GeneID =i.GeneID1) and (g2.GeneID=i.GeneID2)
				and g1.Chromosome != g2.Chromosome)
select c1, c2, sum(val) as somma
from tab
group by c1, c2
order by somma"""

        cursor.execute(query,())

        for row in cursor:
            result.append(Archi(row["c1"],row["c2"],row["somma"]))

        cursor.close()
        conn.close()
        return result
