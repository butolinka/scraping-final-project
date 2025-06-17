import sqlite3
import sys

DB_NAME = "mlb_almanac.db"

def list_available_years(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    years = [name[0].replace("mlb_almanac_", "") for name in tables if name[0].startswith("mlb_almanac_")]
    return sorted(years)

def query_data(year, player=None, statistic=None, team=None):
    table_name = f"mlb_almanac_{year}"
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        if not cursor.fetchone():
            print(f"❌ No data found for year {year}.")
            return

        query = f'SELECT year, statistic, name, team, value, top_25 FROM "{table_name}" WHERE 1=1'
        params = []

        if player:
            query += " AND name LIKE ?"
            params.append(f"%{player}%")
        if statistic:
            query += " AND statistic LIKE ?"
            params.append(f"%{statistic}%")
        if team:
            query += " AND team LIKE ?"
            params.append(f"%{team}%")

        cursor.execute(query, params)
        results = cursor.fetchall()

        if not results:
            print("ℹ️ No matching records found.")
            return

        print(f"\n📊 Results for year {year}:")
        print("-" * 70)
        for row in results:
            print(f"Year: {row[0]} | Stat: {row[1]} | Player: {row[2]} | Team: {row[3]} | Value: {row[4]} | Top 25: {row[5]}")
        print("-" * 70)

    except Exception as e:
        print(f"⚠️ Error: {e}")
    finally:
        conn.close()

def main():
    print("📁 MLB Almanac Database Query")
    print("-" * 40)

    year = input("Enter year (1876–2025): ").strip()
    if not year.isdigit():
        print("⚠️ Invalid year.")
        return

    player = input("Optional: Enter player name (or leave blank): ").strip()
    statistic = input("Optional: Enter statistic type (or leave blank): ").strip()
    team = input("Optional: Enter team name (or leave blank): ").strip()

    query_data(year, player, statistic, team)

if __name__ == "__main__":
    main()