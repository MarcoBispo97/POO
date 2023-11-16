class Repositorio:

    def select(self, db_connection: any) -> None:
        concetion = db_connection.conectar()
        print('conectei ao banc {}'.format(concetion))
        print('fazendo um SELECT * FROM ...')
        db_connection.desconectar()

    def insert(self, db_conection: any) -> None:
        concetion = db_conection.conectar()
        print('conectei ao banc {}'.format(concetion))
        print('fazendo um SELECT * FROM ...')
        db_conection.desconectar()
