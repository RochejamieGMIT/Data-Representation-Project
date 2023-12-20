import mysql.connector
import dbconfig as cfg
class CountryDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
         
    def create(self, values):
        cursor = self.getcursor()
        sql="insert into country (country,Land_area, capital,co2,C_Code,Life_ex,Min_Wage,Off_language,Population,Lat,lon) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

    def getAll(self):
        cursor = self.getcursor()
        sql="select * from country"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from country where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue
    
    def findByCountry(self, country):
        cursor = self.getcursor()
        sql="select * from country where country = %s"
        values = (country,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def findByRegion(self):
        
        #sql="select c.country,c.capital,r.region,r.literacy,r.phone from country c inner join regionInfo r on c.country = r.country where r.region = 'WESTERN EUROPE' limit 5"
        #values = (region,limit,)
        cursor = self.getcursor()
        sql="select c.country,c.capital,r.region,r.literacy,r.phone from country c inner join regionInfo r on c.country = r.country limit 5"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray



    def update(self, values):
        cursor = self.getcursor()
        sql="update country set country= %s,Land_area= %s, capital= %s,co2= %s,C_Code= %s,Life_ex= %s,Min_Wage=%s,Off_language=%s,Population=%s,Lat=%s,lon=%s  where id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from country where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        print("delete done")

    def convertToDictionary(self, result):
        colnames=["id","country","Land_area", "capital","co2","C_Code","Life_ex","Min_Wage","Off_language","Population","Lat","lon"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
countryDAO = CountryDAO()