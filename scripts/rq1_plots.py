import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/nba_clutch_merged.csv")

# Create difference column
df["clutch_minus_reg_win_pct"] = df["clutch_win_pct"] - df["reg_win_pct"]

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

# Plot 1: Regular-season win% vs clutch win%
plt.figure(figsize=(9, 6))
plt.scatter(df["reg_win_pct"], df["clutch_win_pct"], s=60)

for _, row in df.iterrows():
    plt.text(
        row["reg_win_pct"] + 0.004,
        row["clutch_win_pct"] + 0.004,
        row["Short_Team"],
        fontsize=7
    )

plt.title("Regular-Season Win% vs Clutch Win%")
plt.xlabel("Regular-Season Win Percentage")
plt.ylabel("Clutch Win Percentage")
plt.tight_layout()
plt.savefig("plots/rq1_plot1_reg_vs_clutch_win_shortnames.png")
plt.show()

# Plot 2: Difference between clutch and regular-season win%
diff_df = df.sort_values("clutch_minus_reg_win_pct", ascending=False)

plt.figure(figsize=(11, 6))
plt.bar(diff_df["Short_Team"], diff_df["clutch_minus_reg_win_pct"])
plt.axhline(0)
plt.title("Difference Between Clutch Win% and Regular-Season Win%")
plt.xlabel("Team")
plt.ylabel("Clutch Win% - Regular-Season Win%")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("plots/rq1_plot2_clutch_minus_reg_win_shortnames.png")
plt.show()

print("Both plots saved successfully.")