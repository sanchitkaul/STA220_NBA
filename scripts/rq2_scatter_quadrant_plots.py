import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/nba_clutch_merged.csv")

# making team names shorter
short_names = {
    "Atlanta Hawks": "Hawks",
    "Boston Celtics": "Celtics",
    "Brooklyn Nets": "Nets",
    "Charlotte Hornets": "Hornets",
    "Chicago Bulls": "Bulls",
    "Cleveland Cavaliers": "Cavs",
    "Dallas Mavericks": "Mavs",
    "Denver Nuggets": "Nuggets",
    "Detroit Pistons": "Pistons",
    "Golden State Warriors": "Warriors",
    "Houston Rockets": "Rockets",
    "Indiana Pacers": "Pacers",
    "LA Clippers": "Clippers",
    "Los Angeles Lakers": "Lakers",
    "Memphis Grizzlies": "Grizzlies",
    "Miami Heat": "Heat",
    "Milwaukee Bucks": "Bucks",
    "Minnesota Timberwolves": "Wolves",
    "New Orleans Pelicans": "Pelicans",
    "New York Knicks": "Knicks",
    "Oklahoma City Thunder": "Thunder",
    "Orlando Magic": "Magic",
    "Philadelphia 76ers": "76ers",
    "Phoenix Suns": "Suns",
    "Portland Trail Blazers": "Blazers",
    "Sacramento Kings": "Kings",
    "San Antonio Spurs": "Spurs",
    "Toronto Raptors": "Raptors",
    "Utah Jazz": "Jazz",
    "Washington Wizards": "Wizards"
}

df["Short_Team"] = df["Team"].replace(short_names)

# Plot 1: Scatter Plot : clutch eFG% vs clutch win%
plt.figure(figsize=(9, 6))
plt.scatter(df["clutch_efg_pct"], df["clutch_win_pct"], s=60)

for _, row in df.iterrows():
    plt.text(
        row["clutch_efg_pct"] + 0.002,
        row["clutch_win_pct"] + 0.004,
        row["Short_Team"],
        fontsize=7
    )

plt.title("Clutch eFG% vs Clutch Win%")
plt.xlabel("Clutch eFG%")
plt.ylabel("Clutch Win Percentage")
plt.tight_layout()
plt.savefig("plots/rq2_scatter_efg_vs_win.png")
plt.show()

# Plot 2: Quadrant plot : clutch eFG% vs clutch TOV%
x_mean = df["clutch_efg_pct"].mean()
y_mean = df["clutch_tov_pct"].mean()

plt.figure(figsize=(9, 6))
plt.scatter(df["clutch_efg_pct"], df["clutch_tov_pct"], s=60)

for _, row in df.iterrows():
    plt.text(
        row["clutch_efg_pct"] + 0.002,
        row["clutch_tov_pct"] + 0.002,
        row["Short_Team"],
        fontsize=7
    )

# Mean reference lines
plt.axvline(x_mean, linestyle="--")
plt.axhline(y_mean, linestyle="--")

plt.title("Quadrant Plot of Clutch eFG% and Clutch TOV%")
plt.xlabel("Clutch eFG%")
plt.ylabel("Clutch Turnover Percentage")
plt.tight_layout()
plt.savefig("plots/rq2_quadrant_efg_vs_tov.png")
plt.show()

print("RQ2 scatter and quadrant plots saved successfully.")