import os
import psycopg
from psycopg import sql

CSV_FILE = "data.csv"   # already in root folder

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS medicines (
  id SERIAL PRIMARY KEY,

  name VARCHAR(255),
  link VARCHAR(500),
  contains VARCHAR(500),

  introduction TEXT,
  uses TEXT,
  benefits TEXT,
  side_effect TEXT,
  how_works TEXT,
  quick_tips TEXT,

  chemical_class VARCHAR(255),
  habit_forming VARCHAR(50),
  therapeutic_class VARCHAR(255),
  action_class VARCHAR(255),

  safety_advice_to_alcohol TEXT,
  safety_advice_to_pregnancy TEXT,
  safety_advice_to_breast_feeding TEXT,
  safety_advice_to_driving TEXT,
  safety_advice_to_kidney TEXT,
  safety_advice_to_liver TEXT
);
"""

COPY_COLUMNS = (
    "name,link,contains,"
    "introduction,uses,benefits,side_effect,how_works,quick_tips,"
    "chemical_class,habit_forming,therapeutic_class,action_class,"
    "safety_advice_to_alcohol,safety_advice_to_pregnancy,safety_advice_to_breast_feeding,"
    "safety_advice_to_driving,safety_advice_to_kidney,safety_advice_to_liver"
)

def main():
    # Get Neon connection string from env variable
    db_url = os.getenv('postgresql://neondb_owner:npg_HtU7Zgnyh2qz@ep-royal-art-a1xeto09-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require')
    if not db_url:
        print("ERROR: Set DATABASE_URL environment variable for Neon DB.")
        return

    if not os.path.exists(CSV_FILE):
        print(f"ERROR: CSV file '{CSV_FILE}' not found in root directory.")
        return

    print("Connecting to Neon…")

    with psycopg.connect(db_url, autocommit=True) as conn:
        with conn.cursor() as cur:

            # Create table
            cur.execute(CREATE_TABLE_SQL)
            print("Table 'medicines' created or already exists.")

            # Prepare COPY command
            copy_sql = sql.SQL(
                "COPY medicines ({cols}) FROM STDIN WITH (FORMAT csv, HEADER true, DELIMITER ',', QUOTE '\"')"
            ).format(cols=sql.SQL(COPY_COLUMNS))

            # Import CSV
            with open(CSV_FILE, "r", encoding="utf-8") as f:
                cur.copy_expert(copy_sql.as_string(conn), f)

            print("CSV upload completed successfully! 🚀")

if __name__ == "__main__":
    main()
