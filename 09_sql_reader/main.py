import pandas as pd
from sqlalchemy import create_engine, text
from openai import OpenAI
from decouple import config
import re

client = OpenAI(api_key=config("OPEN_API_KEY"))

# Configure DB connection - example PostgreSQL
DB_URI = "postgresql+psycopg2://postgres:password@localhost:5432/eduboard"
engine = create_engine(DB_URI, echo=False)

def get_db_schema():
    query = """
    SELECT table_name, column_name
    FROM information_schema.columns
    WHERE table_schema = 'public'
    ORDER BY table_name, ordinal_position
    """
    return pd.read_sql(query, engine)


def generate_sql(user_question, schema):
    schema_str = schema.to_string(index=False)

    prompt = f"""
        You are an expert SQL assistant.
        Return ONLY a valid PostgreSQL SELECT query.
        Rules:
        - NO explanations
        - NO backticks
        - NO markdown
        - NO comments
        - MUST end with a semicolon

        Schema:
        {schema_str}

        Question: "{user_question}"

        Respond with a single SQL query only.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    sql = response.choices[0].message.content.strip()

    # Remove backticks or code fences
    sql = re.sub(r"(```sql|```|`)", "", sql, flags=re.IGNORECASE).strip()

    # Extract first SELECT ... ; statement
    match = re.search(r"(select[\\s\\S]+?;)", sql, re.IGNORECASE)
    if match:
        sql = match.group(1).strip()

    # Validate
    if not sql.lower().startswith("select"):
        raise ValueError(f"⚠️ Invalid SQL generated:\n{sql}")

    # Add LIMIT safeguard if missing
    if "limit" not in sql.lower():
        sql = sql.rstrip(";") + " LIMIT 100;"

    return sql


def execute_sql(sql):
    try:
        df = pd.read_sql(text(sql), engine)
        return df
    except Exception as e:
        return f"SQL Error: {e}"


if __name__ == "__main__":
    schema = get_db_schema()
    print("Schema loaded!")

    while True:
        user_q = input("\nAsk something (or type 'exit'): ")
        if user_q.lower() == "exit":
            break

        sql = generate_sql(user_q, schema)
        print("\nGenerated SQL:")
        print(sql)

        result = execute_sql(sql)
        print("\nResult:")
        print(result)
