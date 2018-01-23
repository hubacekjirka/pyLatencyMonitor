#!#/usr/bin/python3
import subprocess,MySQLdb
import config as cfg
from collections import namedtuple
from datetime import datetime
 
def ping(host):
    #subprocess.Popen()
    p1 = subprocess.Popen(['ping', "-c "+ str(cfg.icmpCount), host], stdout=subprocess.PIPE)
    output = p1.communicate()[0]
    
    decoded=output.decode("utf-8").splitlines()

    #print(decoded[len(decoded)-2])
    #print(decoded[len(decoded)-1])

    statsTemp=decoded[len(decoded)-2].split(", ")
    packetLoss=int(statsTemp[2].split("%")[0])/100.0
    #print(packetLoss)

    statsTemp=decoded[len(decoded)-1].split(" = ")[1].split(" ")[0].split("/")
    minLatency=statsTemp[0]
    maxLatency=statsTemp[2]
    avgLatency=statsTemp[1]
    mdevLatency=statsTemp[3]

    #return tuple
    latencyRecord=namedtuple('LatencyRecord','ts,packetLoss,min,max,avg,mdev')
    latencyRecord.ts=str(datetime.now())
    latencyRecord.packetLoss=packetLoss
    latencyRecord.min=minLatency
    latencyRecord.max=maxLatency
    latencyRecord.avg=avgLatency
    latencyRecord.mdev=mdevLatency
    
    return latencyRecord

def writeToDb(latencyRecord):
    #python 3.6 syntax, not present in Raspbian's packages yet
    #sqlStr=f"""INSERT INTO latency2
    #            (loc_id, ts, minLatency,maxLatency,avgLatency,mdevLatency) 
    #            VALUES (1,'{latencyRecord.ts}',{latencyRecord.min},{latencyRecord.max},{latencyRecord.avg},{latencyRecord.mdev});"""
    
    #python 3.4 syntax
    sqlStr="""INSERT INTO latency2
                (loc_id, ts, packetLoss, minLatency,maxLatency,avgLatency,mdevLatency) 
                VALUES (1,""" + "'" + latencyRecord.ts + "'," + str(latencyRecord.packetLoss) + "," + latencyRecord.min + "," + latencyRecord.max + "," + latencyRecord.avg + "," + latencyRecord.mdev + ");"

    print(sqlStr)

    conn = MySQLdb.connect(host= cfg.mysql['host'],
                  user=cfg.mysql['user'],
                  passwd=cfg.mysql['passwd'],
                  db=cfg.mysql['db'])
    x = conn.cursor()

    try:
        x.execute(sqlStr)
        conn.commit()
        print("Db commit successfull")
    except:
        conn.rollback()
        print("Db commit failed")

    conn.close()

print(str(datetime.now()) + " - utility start")
writeToDb(ping(cfg.host))
print(str(datetime.now()) + " - utility end")