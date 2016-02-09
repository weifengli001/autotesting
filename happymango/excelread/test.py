from readexcel import read_excel
import fileinput

""" read excel file"""
appid = (int)(read_excel("/Users/weifengli/tmp/test.xlsx", 0, 0, 0))
print int(appid)
path = "//button[@applicationid='" + str(appid) +"']"

print path

""" read file """
with open("/Users/weifengli/tmp/a.txt") as f:
    content = f.readlines()
    print content[0]



