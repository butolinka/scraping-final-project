# scraping-final-project
 MLB Almanac Dashboard
An interactive Streamlit dashboard to explore MLB historical player statistics from 1876 to 2025.
#Features
Three Visualizations:
Bar chart: Top players for a selected statistic
Pie chart: Team distribution among top players
Line chart: Statistical trend over time

Interactive Controls:
Dropdown: Select statistic
Slider: Choose the number of top players
Year range selector: Filter by year span

Data Source:
SQLite database created from 150+ CSV files with cleaned MLB statistics.

How to Run
bash
Copy
Edit

pip install -r requirements.txt

streamlit run dashboard.py

Files
import_to_db.py – Imports and cleans data into a SQLite database.

query_mlb_db.py – Run command-line queries on the database.

dashboard.py – Interactive dashboard (main file).

data/raw/ – Folder for raw CSV files.

mlb_almanac.db – SQLite database (auto-generated).

![image](https://github.com/user-attachments/assets/56fe5d28-6d24-4030-a915-1c4dc19a567c)
