from flask import Flask, jsonify
from config import config
from flask_mysqldb import MySQL
from flask_cors import CORS

app=Flask(__name__)
cors=CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
conexion=MySQL(app)

@app.route('/datos', methods=['GET'])
def listar_datos():
    try:
        cursor=conexion.connection.cursor()
        sql='SELECT dato1, dato2, dato3 FROM api_flask.datos;'
        cursor.execute(sql)
        datos=cursor.fetchall()
        datosJSON=[]
        for fila in datos:
            datosJS={'dato1':fila[0],'dato2':fila[1],'dato3':fila[2]}
            datosJSON.append(datosJS)
        response=jsonify({'datos':datosJSON,"mensaje":"Los cursos han sido listados"})
        response.headers.add("Access-Control-Allow-Origin","*")
        return response
    except Exception as ex:
        print(ex)
        return jsonify({"mensaje":"Error"})

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()