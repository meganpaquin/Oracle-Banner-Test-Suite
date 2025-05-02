import oracledb
import settings.constants as constants
import logging

def db_connector(func):
    def with_connection_(*args, **kwargs):
        # Connect to Oracle Client
        oracledb.init_oracle_client(config_dir=constants.config_dir)

        cnn = oracledb.connect(
            user=constants.REGISTRAR_READ_USERNAME,
            password=constants.REGISTRAR_READ_PASSWORD,
            dsn=constants.PNTR_HOST_NAME)

        try:
            rv = func(cnn, *args, **kwargs)
        except Exception:
            cnn.rollback()
            logging.error("Database connection error")
            raise
        finally:
            cnn.close()
        return rv
    return with_connection_
