import psycopg2
from flask import Flask
from flask import jsonify

app = Flask(__name__)

cxn = psycopg2.connect("dbname=ROFL user=postgres password=rofl")
cursor = cxn.cursor()

@app.route('/currentRosters')
def getAllCurrentRosters():
    cursor.execute("""select * from current_rosters""")
    res = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    rostersList = []
    for row in res:
        rostersMap = {}
        for i in range(len(row)):
            rostersMap[column_names[i]] = row[i]
        rostersList.append(rostersMap)
    return jsonify(rostersList)
