import sqlite3
from sqlite3 import Error

class QueriesSQLite:
	def create_connection(path):
		connection = None
		try:
			connection = sqlite3.connect(path)
			print("Conexión a BD_SQLite establecida")
		except Error as e:
			print(f"The error '{e}' ocurred")

		return connection

	def execute_query(connection, query, data_tuple):
		cursor = connection.cursor()
		try:
			cursor.execute(query, data_tuple)
			connection.commit()
			print("Query ejecutado de forma correcta")
			return cursor.lastrowid
		except Error as e:
			print(f"The error '{e}' ocurred")

	def execute_read_query(connection, query, data_tuple = ()):
		cursor = connection.cursor()
		result = None
		try:
			cursor.execute(query, data_tuple)
			result = cursor.fetchall()
			return result
		except Error as e:
			print(f"The error '{e}' ocurred")

	def create_tables():
		connection = QueriesSQLite.create_connection("BD_pdv.sqlite")

		tabla_productos = """
		CREATE TABLE IF NOT EXISTS productos(
			codigo TEXT PRIMARY KEY,
			nombre TEXT NOT NULL,
			precio REAL NOT NULL,
			cantidad INTEGER NOT NULL
			);
		"""

		tabla_usuarios = """
		CREATE TABLE IF NOT EXISTS usuarios(
			username TEXT PRIMARY KEY,
			nombre TEXT NOT NULL,
			password TEXT NOT NULL,
			tipo TEXT NOT NULL
			);
		"""

		tabla_ventas = """
		CREATE TABLE IF NOT EXISTS ventas(
			id INTEGER PRIMARY KEY,
			total REAL NOT NULL,
			fecha TIMESTAMP,
			username TEXT NOT NULL,
			FOREIGN KEY(username) REFERENCES usuarios(username)
			);
		"""

		tabla_ventas_detalle = """
		CREATE TABLE IF NOT EXISTS ventas_detalle(
			id INTEGER PRIMARY KEY,
			id_venta TEXT NOT NULL,
			precio REAL NOT NULL,
			producto TEXT NOT NULL,
			cantidad INTEGER NOT NULL,
			FOREIGN KEY(id_venta) REFERENCES ventas(id),
			FOREIGN KEY(producto) REFERENCES productos(codigo)
			);
		"""

		QueriesSQLite.execute_query(connection, tabla_productos, tuple()) 
		QueriesSQLite.execute_query(connection, tabla_usuarios, tuple()) 
		QueriesSQLite.execute_query(connection, tabla_ventas, tuple()) 
		QueriesSQLite.execute_query(connection, tabla_ventas_detalle, tuple()) 

if __name__ == "__main__":
	connection = QueriesSQLite.create_connection("BD_pdv.sqlite")


	# create_product_table = """
	# CREATE TABLE IF NOT EXISTS productos(
	# 	codigo TEXT PRIMARY KEY,
	# 	nombre TEXT NOT NULL,
	# 	precio REAL NOT NULL,
	# 	cantidad INTENGER NOT NULL
	# 	);
	# """
	# QueriesSQLite.execute_query(connection, create_product_table, tuple())

	# create_user_table = """
	# CREATE TABLE IF NOT EXISTS usuarios(
	# 	username TEXT PRIMARY KEY,
	# 	nombre TEXT NOT NULL,
	# 	password TEXT NOT NULL,
	# 	tipo TEXT NOT NULL
	# 	);
	# """
	# QueriesSQLite.execute_query(connection, create_user_table, tuple())

	# crear_producto = """
	# INSERT INTO
	# 	productos(codigo, nombre, precio, cantidad)
	# VALUES
	# 	('010', 'guantes box 10oz', 530.00, 20),
	# 	('012', 'guantes box 12oz', 550.00, 50),
	# 	('014', 'guantes box 14oz', 570.00, 30),
	# 	('016', 'guantes box 16oz', 590.00, 70),
	# 	('018', 'guantes box 18oz', 610.00, 25),
	# 	('020', 'espinilleras chicas', 350, 30),
	# 	('022', 'espinilleras medianas', 400, 60),
	# 	('024', 'espinilleras grandes', 450, 30),
	# 	('030', 'vendas de box 5m', 100, 200),
	# 	('040', 'short chico', 250, 50),
	# 	('042', 'short mediano', 270, 50),
	# 	('044', 'short chico', 290, 50),
	# 	('050', 'domi', 560, 100),
	# 	('060', 'paos (par)', 500, 80),
	# 	('070', 'manoplas (par)', 250, 85)
	# """
	# QueriesSQLite.execute_query(connection, crear_producto, tuple())

	select_products = "SELECT * from ventas"
	productos = QueriesSQLite.execute_read_query(connection, select_products)
	for producto in productos:
		print(producto)

	# usuario_tuple = ('peleador2', 'Luis', 'pelea2', 'trabajador')
	# crear_usuario = """
	# INSERT INTO
	# 	usuarios (username, nombre, password, tipo)
	# VALUES
	# 	(?, ?, ?, ?);
	# """
	# QueriesSQLite.execute_query(connection, crear_usuario, usuario_tuple)

	nueva_data = ('Luis Fernando', 'pelea1', 'admin', 'peleador1')
	actualizar = """
	UPDATE
		usuarios
	SET
		nombre = ?, password = ?, tipo = ?
	WHERE
		username = ?
	"""
	QueriesSQLite.execute_query(connection, actualizar, nueva_data)

	select_users = "SELECT * from usuarios"
	usuarios = QueriesSQLite.execute_read_query(connection, select_users)
	for usuario in usuarios:
		print("type: ", type(usuario), "usuario: ", usuario)

	# select_products = "SELECT * from productos"
	# productos = QueriesSQLite.execute_read_query(connection, select_products)
	# for producto in productos:
	# 	print(producto)

	# producto_a_borrar = ('070',)
	# borrar = """DELETE from productos where codigo = ?"""
	# QueriesSQLite.execute_query(connection, borrar, producto_a_borrar)

	# select_products = "SELECT * from productos"
	# productos = QueriesSQLite.execute_read_query(connection, select_products)
	# for producto in productos:
	# 	print(producto)
	# 	