#!/usr/bin/python

import sys
import getopt
import datetime
import csv
import MySQLdb as mdb


sqlstr_format = """
SELECT
  cust.iId custid, cust.sEmail email, info.sFname first, info.sLname last,
  app.iId id, app.iAmount amount, app.dtInsert submit_time, app.dtDocusignComplete sign_time, app.iDocusign sign,
  app.sBank bank, app.sStatus status, app.sReview review_status, app.sRecommendation,
  chk.created_at check_time,
  rev.created_at review_time, rev.sOption review_option,
  rec.created_at recommend_time,
  exe.created_at execute_time, exe.sOption execute_status
FROM
  tApplications app
LEFT JOIN
  tCustomers cust ON (cust.iId = app.iUserId)
LEFT JOIN
  tUserInfo info ON (cust.iId = info.iUserId)
LEFT JOIN
  tSpringBankCheck chk ON (app.iId = chk.iApplicationId)
LEFT JOIN
  tReview rev ON (app.iId = rev.iApplicationId)
LEFT JOIN
  tRecommendation rec ON (app.iId = rec.iApplicationId)
LEFT JOIN
  tSpringBankExecute exe ON (app.iId = exe.iApplicationId)
WHERE app.iId IN (%s)
"""

def runQuery(conn, appids):
    #
    # Use a cursor that allows access to the DB result using Python dictionary.
    #
    cur = conn.cursor(mdb.cursors.DictCursor)
    #
    # Retrieve application status for given set of application ids.
    #
    sqlstr = sqlstr_format % ','.join(appids)
    cur.execute(sqlstr)
    rows = cur.fetchall()
    #
    # Iterate through each row which contains application status and other information.
    # Each column value can be retrieved using the key that corresponds to the column name
    # used for the query.
    #
    for row in rows:
        print "cust id = %d, app id = %d, app status = '%s', app review status = '%s', app Recommendation status = '%s'" % (row['custid'], row['id'], row['status'], row['review_status'], row['sRecommendation'])
    cur.close()

def main(argv):
    user = 'weifengli'
    password = 'happymango'
    database = 'happymangotest2'
    port = 3406
    (opts, args) = getopt.getopt(argv, "p:U:P:D:")
    for (o, a) in opts:
        if o == '-U':
            user = a
        elif o == '-P':
            password = a
        elif o == '-D':
            database = a
        elif o == '-p':
            port = int(a)
    if password == '':
        sys.stderr.write("password not given")
        return 1
    if len(args) == 0:
        sys.stderr.write("usage: dbsample.py [-U user] [-P password] [-D database] [-p port] appid ...\n")
        return 1
    conn = mdb.connect('127.0.0.1', user, password, database, port)
    runQuery(conn, args)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
