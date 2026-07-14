import psycopg2

from app.config import (
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_DB,
    POSTGRES_USER,
    POSTGRES_PASSWORD
)

class Database:

    def __init__(self):

        self.connection = psycopg2.connect(
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
            dbname=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD
        )
    # Para criar ou atualizar (sincronizar automaticamente) 
    # Patient via PUT a partir do registro do pgsql
    def get_patient(self, patient_id):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT
                patient_id,
                full_name,
                birth_date,
                gender,
                cpf,
                national_health_id
            FROM patients
            WHERE patient_id = %s
            """,
            (patient_id,)
        )

        row = cursor.fetchone()

        if not row:
            return None

        return {
            "patient_id": row[0],
            "full_name": row[1],
            "birth_date": row[2],
            "gender": row[3],
            "cpf": row[4],
            "sus": row[5]
        }