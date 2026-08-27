import oracledb
import os
from dotenv import load_dotenv

load_dotenv()


def conectar():
    dsn = (
        "(description="
        "(address=(protocol=tcps)(port=2484)(host=db.freesql.com))"
        "(connect_data=(service_name=26ai_un3c1)))"
    )

    connection = oracledb.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dsn=dsn
    )

    return connection