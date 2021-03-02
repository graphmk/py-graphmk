import sys
from graphgenpy import utils
import os
import jpype
import imp



class GraphMk:
    GML = 'gml'
    GraphSON = 'json'

    def __init__(self, dbname, host='', port='', username='', password=''):
        self.dbname = dbname
        self.port = port
        self.host = host
        self.username = username
        self.password = password

    def displayConfig(self):
        print("DBName: %s, Port: %s, Host: %s, Username: %s, Pass:%s " % self.dbname, self.port, self.host, self.username, self.password)

    def generateGraph(self,extractionQuery, filename, serialization_format='gml'):
        graphmk_version = '1.0.0'
        if jpype.isJVMStarted() != True:
            classpth = os.path.dirname(os.path.abspath(__file__)) + "/lib/graphmk-{0}.jar".format(graphmk_version)
            jpype.startJVM(jpype.getDefaultJVMPath())
            jpype.addClassPath(classpth)    
        
        GraphGenerateClass = jpype.JClass('io.github.graphmk.graphcore.PyGenerateGraph')

        GraphGenerateClass.main([extractionQuery, serialization_format, filename,self.host, self.port, self.dbname, self.username, self.password])

        return filename+"."+serialization_format