import re
import hgvs

def load_data (data_file):
         
         d = {}
                   
         with open(data_file, "r+") as f:
             for line in f:
                 y = re.split("[\t \n]", line)
                 if y[0] != "Chrom":
                    x = hgvs.get_hgvs_from_vcf(y[0], y[1],y[2], y[3])
                    d[x] = {}
                    d[x]["chr"] = y[0]
                    d[x]["pos"] = y[1]
                    d[x]["ref"] = y[2]
                    d[x]["alt"] = y[3]
                    d[x]["score"] = float(y[4])
                    print(d)
                    d = {}
