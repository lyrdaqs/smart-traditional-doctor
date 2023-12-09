import mysql.connector as mysql


db_config = {
   'user': 'root',
   'password': 'root',
   'host': 'mysql',
   #'host': 'localhost',
   'database': 'doctorai',
}

class MySqlConnection:
    def __init__(self):
        pass
        #self.connection = mysql.connect(**db_config)

    def _connect(self):
        return mysql.connect(**db_config)
    

    def get_illness_by_signs_w2c(self, signs, l):
        conn = self._connect()
        cursor = conn.cursor(dictionary=True)
        query = f"""
            SELECT illness, avg(s) as s FROM
            (
        """
        for index, sign in enumerate(signs):
            query += f"""
                SELECT illness , max(simularity) as s FROM illness_sign
                WHERE (sign = '{sign}')
                GROUP BY illness
            """
            if index == len(signs) - 1:
                query += ") sign_ill"
            else:
                query += "UNION"

        query += f"""
            GROUP BY illness
            ORDER BY s desc
            LIMIT {l};
        """
        cursor.execute(query)   
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result


    def get_signs_by_illness_w2c(self, illness, signs):
        conn = self._connect()
        cursor = conn.cursor(dictionary=True)
        query = f"""
            SELECT sign, count(*) as c FROM
            (
        """
        for index, illnes in enumerate(illness):
            query += f"""
                (SELECT sign , max(simularity) as s FROM illness_sign
                WHERE (illness = '{illnes}')
                GROUP BY sign LIMIT 10)
            """
            if index == len(illness) - 1:
                query += ") sign_ill"
            else:
                query += "UNION"

        query += f"""
            WHERE sign not in {tuple(signs)}
            GROUP BY sign
            ORDER BY c desc;
            LIMIT 5;
        """
        cursor.execute(query)   
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result


    def get_medicine_by_illnes_w2c(self, illness):
        conn = self._connect()
        cursor = conn.cursor(dictionary=True)
        query = f"""
            SELECT medicine , max(simularity) as s FROM medicine_illness
            WHERE (illness = '{illness}')
            GROUP BY medicine
            ORDER BY s desc
            LIMIT 4;
        """
        cursor.execute(query)   
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

        
    def get_medicine_by_sign_sign_w2c(self, s1, s2):
        cursor = self.connection.cursor(dictionary=True)
        query = f"""
            SELECT medicine , sum(simularity) as s FROM medicine_sign
            WHERE sign = '{s1}' OR sign = '{s2}'
            GROUP BY medicine
            ORDER BY s desc
            LIMIT 30;
        """
        cursor.execute(query)   
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def get_sign_by_illness_sign_w2c(self, s1, s2):
        cursor = self.connection.cursor(dictionary=True)
        query = f"""
            SELECT sign , sum(simularity) as s FROM illness_sign
            WHERE illness = '{s1}' OR illness = '{s2}'
            GROUP BY sign
            ORDER BY s desc
            LIMIT 30;
        """
        cursor.execute(query)   
        result = cursor.fetchall()
        cursor.close()
        return result


    def get_medicine_by_sign_illnes_w2c(self, s, i):
        cursor = self.connection.cursor(dictionary=True)
        query = f"""
            SELECT medicine , sum(s1+ s2) as s
            FROM (select sign , medicine , simularity as s1 from doctorai.medicine_sign
            where sign = '{s}') sm
            INNER JOIN (select illness , medicine as medicine2 , (simularity) as s2 from doctorai.medicine_illness
            where illness = '{i}') il
            on sm.medicine = il.medicine2
            GROUP BY medicine 
            ORDER BY s desc
            LIMIT 30;
        """
        cursor.execute(query)   
        result = cursor.fetchall()
        cursor.close()
        return result
        
        
    def get_medicine_by_sign_sign_glove(self, s1, s2):
        cursor = self.connection.cursor(dictionary=True)
        query = f"""
            SELECT medicine, SUM(count) as s FROM graph_signs_medicines
            WHERE sign = '{s1}' OR sign = '{s2}'
            GROUP BY medicine
            ORDER BY s desc
            LIMIT 20;
        """
        cursor.execute(query)   
        result = cursor.fetchall()
        cursor.close()
        return result


    def get_medicine_by_sign_illnes_glove(self, s, i):
        cursor = self.connection.cursor(dictionary=True)
        query = f"""
            SELECT medicine, SUM(c+c2) as s
            FROM (select sign, medicine, count as c from graph_signs_medicines
            WHERE sign = '{s}') sm
            INNER JOIN (select ilness, medicine as medicine2, count as c2 from graph_medicine_ilness
            where ilness = '{i}') mi
            on sm.medicine = mi.medicine2
            GROUP BY medicine
            ORDER BY s desc
            LIMIT 20;
        """
        cursor.execute(query)   
        result = cursor.fetchall()
        cursor.close()
        return result
    
    
    def get_medicine_by_sign_sign_agg(self, s1, s2):
        cursor = self.connection.cursor(dictionary=True)
        query = f"""
            (SELECT medicine, 0.4*SUM(sim) as score FROM (
                select sign, medicine, count/75 as sim from doctorai.graph_signs_medicines
            ) as norm
                WHERE sign = '{s1}' OR sign = '{s2}'
                GROUP BY medicine
                ORDER BY score desc
                LIMIT 20)
            UNION
            (SELECT medicine , 0.6*sum(s) as score FROM (
                SELECT medicine, sign, avg(simularity) as s FROM doctorai.medicine_sign
                WHERE sign = '{s1}' OR sign = '{s2}'
                group by medicine, sign 
            ) as norm
                GROUP BY medicine
                ORDER BY score desc
                LIMIT 20) 
            ORDER BY score desc 
            LIMIT 20
        """
        cursor.execute(query)   
        result = cursor.fetchall()
        cursor.close()
        return result
    
    
    def get_medicine_by_sign_illnes_agg(self, s, i):
        cursor = self.connection.cursor(dictionary=True)
        query = f"""
            (SELECT medicine, 0.4*SUM(c+c2) as score
                FROM (select sign, medicine, count/75 as c from doctorai.graph_signs_medicines
                WHERE sign = '{s}') sm
                INNER JOIN (select ilness, medicine as medicine2, count/52 as c2 from doctorai.graph_medicine_ilness
                where ilness = '{i}') mi
                on sm.medicine = mi.medicine2
                GROUP BY medicine
                ORDER BY score desc
                LIMIT 20)
            UNION
            (SELECT medicine , 0.6*sum(s1+ s2) as score
                FROM (select sign , medicine , avg(simularity) as s1 from doctorai.medicine_sign
                where sign = '{s}' group by sign , medicine) sm
                INNER JOIN (select illness , medicine as medicine2 , avg(simularity) as s2 from doctorai.medicine_illness
                where illness = '{i}' group by illness , medicine) il
                on sm.medicine = il.medicine2
                GROUP BY medicine 
                ORDER BY score desc
                LIMIT 20)
            ORDER BY score desc 
            LIMIT 20
        """
        cursor.execute(query)   
        result = cursor.fetchall()
        cursor.close()
        return result
            