import re, logging
import utils.hgvs as hgvs

def load_data (data_file):
         
         d = {}
                   
         with open(data_file, "r+") as f:
             for line in f:
                 try:
                    y = re.split("[\t \n]", line)
                    if y[0] != "Chrom":
                       _id = hgvs.get_hgvs_from_vcf(y[0], y[1],y[2], y[3])
                       d = {"_id":_id, "fire": {}}
                       d["fire"]["chr"] = y[0]
                       d["fire"]["pos"] = y[1]
                       d["fire"]["ref"] = y[2]
                       d["fire"]["alt"] = y[3]
                       d["fire"]["score"] = float(y[4])
                       yield d
                       d = {}
                 except Exception as e:
                     logging.error("Pb with %s: %s" % (line,e))
                     continue
