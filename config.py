from MeguBot.sample_config import Config

class Development(Config):
    OWNER_ID = 1258640682
    OWNER_USERNAME = "Fastmore Crak"
    API_KEY = "1934799326:AAEV-WHPDqBoJbnGlgI6AdV1d3aO8b-rGQY"
    SQLALCHEMY_DATABASE_URI = 'postgresql://nombredeusuario:contraseña@localhost:5432/database' # Credenciales de base de datos de muestra.
    MESSAGE_DUMP = '1001165336536'
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [1258640682]
    LOAD = []
    NO_LOAD = ['translation']