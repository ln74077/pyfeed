'''
Created on 01-Apr-2018

@author: lakshminarayana
'''
import feedparser
import pickle
import requests as req
import mysql.connector

cnx = mysql.connector.connect(user='root', database='THEHINDU',password='admin',host='127.0.0.1',port='3306',autocommit=True)
cursor = cnx.cursor()

add_row = ("INSERT INTO links "
               "(loc, title,content) "
               "VALUES (%s, %s, %s)")


if __name__ == '__main__':
    readDictFile = open("rssDict.data","rb")
    rssDict = pickle.load(readDictFile)
    readDictFile.close()
    #inDataFile = open("parsed.data","a")
    
    for key in range(1,len(rssDict.keys())+1):
        URL,rssPage,status,etag,modified = rssDict[key].split("$$")
        xmlData=feedparser.parse(URL,etag=etag,modified=modified)
        
        for i in range(0,len(xmlData.entries)):
            
            responseData = req.request("GET","http://jws-app-nbojanapuae.1d35.starter-us-east-1.openshiftapps.com/api/v1/content?url="+xmlData.entries[i].link).text
            #inDataFile.write(xmlData.entries[i].title+"$$"+xmlData.entries[i].published+"$$"+responseData)
            data_row = (xmlData.entries[i].link, xmlData.entries[i].title, responseData)
            cursor.execute(add_row, data_row)
            
        etag=xmlData.etag if xmlData.has_key("etag") else etag
        modified = xmlData.modified if xmlData.has_key("modified") else modified
        rssDict[key]=URL+"$$"+rssPage+"$$"+status+"$$"+etag+"$$"+modified
    
    cnx.commit()
    cursor.close()
    cnx.close()
            
    writeDictFile = open("rssDict.data","wb")
    pickle.dump(rssDict,writeDictFile)
    #inDataFile.close()
    writeDictFile.close()


    
    
    
        
    
    
    