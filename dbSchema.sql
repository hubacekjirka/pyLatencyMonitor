CREATE TABLE latency2 ( 
  loc_id tinyint(4) NOT NULL, 
  ts timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
  packetLoss decimal[3,2] NULL, 
  minLatency smallint(5) unsigned NULL, 
  maxLatency smallint(5) unsigned NULL, 
  avgLatency smallint(5) unsigned NULL, 
  mdevLatency smallint(5) unsigned NULL, 
  PRIMARY KEY (loc_id,ts) 
) ENGINE=InnoDB DEFAULT CHARSET=latin1; 