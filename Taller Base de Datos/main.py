import mysql.connector
from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)

conexion = mysql.connector.connect(
    user='root',
    password='admin',
    host='127.0.0.1',
    port='3306',
    auth_plugin='mysql_native_password',
    database='negocio') 
cursor = conexion.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS cliente(
    cuil VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(50),
    edad INT,
    puntos INT
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ordenes(
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE,
    empleado VARCHAR(50) REFERENCES empleados(cuil),
    cliente VARCHAR(50) REFERENCES cliente(cuil)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS items_orden(
    id_orden INT REFERENCES ordenes(id),
    id_producto INT REFERENCES productos(id),
    PRIMARY KEY (id_orden, id_producto)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS empleados(
    cuil VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    edad INT
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS productos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    marca VARCHAR(50),
    cantidad INT,
    precio INT
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS enteRegulador(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    recaudado INT,
    gastos INT,
    abona INT,
    fecha DATE
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS proveedores(
    cuil VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    empresa VARCHAR(50),
    provee VARCHAR(50)
)''')


@app.route("/consultaCliente",methods=["POST","GET"])
def inicio():
    
    sql = "INSERT INTO cliente(nombre, edad, cuil,puntos) VALUES(%s, %s, %s, %s)"
    val = ("Juan", 21, '23221391',0)

    sql1 = "INSERT INTO cliente(nombre, edad, cuil,puntos) VALUES(%s, %s, %s,%s)"
    val1 = ("Pepe", 40, '22109138',0)
    return render_template("consultaCliente.html")


@app.route("/crear_cuenta",methods=["POST","GET"])
def crearCliente():
    if request.method == 'POST':
        if not request.form["correo"] or not request.form["clave"] or not request.form["nombre"]:
            return render_template ("registro.html")
        elif Usuario.query.filter_by(correo=request.form["correo"]).first():
            return render_template ("registro.html")
        elif Usuario.query.filter_by(correo=request.form["nombre"]).first():
            return render_template ("registro.html")
        else:
            user = Usuario(
			nombre=request.form['nombre'],
			correo=request.form['correo'],
			clave=hashlib.md5(bytes(request.form['clave'], encoding='utf-8')).hexdigest()
            )
            db.session.add(user)
            db.session.commit()
            return render_template ("inicio.html")
    
    else:
        return render_template ("error.html")

cursor.execute(sql, val)
cursor.execute(sql1, val1)
conexion.commit()

cursor.close()
conexion.close()

#ncorrect table definition; there can be only one auto column and it must be defined as a key

"""try:
    with conexion: #se ejecuta el bloque de codigo y al finalizar se ejecute el metodo close, la documentacion de postgres recomienda usar with ya que no cerra la conexion
        with conexion.cursor() as cursor:
            sentencia = 'SELECT *FROM persona'
            cursor.execute(sentencia) #ejecuta la sentencia
            registros = cursor.fetchall() #recupera todos los registros de la consulta
            print(registros)

            sentencia1 = 'SELECT *FROM persona WHERE id_persona= %s' # %s es un parametro posicional 
            id_persona = input('Proporciona la valor a buscar: ')
            cursor.execute(sentencia1,(id_persona,))
            registro = cursor.fetchone() #para recuperar un solo registro
            print(registro)

            sentencia2 = 'SELECT *FROM persona WHERE id_persona IN (1,2)'
            cursor.execute(sentencia2)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
            sentencia3 = 'SELECT *FROM persona WHERE id_persona IN %s'
            entrada = input('Proporciona la valor a buscar (separad por comas): ')
            llaves_primarias = (tuple(entrada.split(',')),)
            cursor.execute(sentencia3,llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()"""

if __name__== "__main__":
    app.run(debug = True)