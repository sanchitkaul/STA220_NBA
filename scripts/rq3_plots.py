import pandas as pd
import matplotlib.pyplot as plt

# Loading merged dataset
df = pd.read_csv("data/nba_clutch_merged.csv") 

top10 = df.sort_values("clutch_win_pct", ascending=False).head(10).copy()
top10 = top10.sort_values("clutch_win_pct", ascending=True)

short_names = {
    "Oklahoma City Thunder": "Thunder",
    "Cleveland Cavaliers": "Cavaliers",
    "Boston Celtics": "Celtics",
    "Los Angeles Lakers": "Lakers",
    "Denver Nuggets": "Nuggets",
    "Milwaukee Bucks": "Bucks",
    "Houston Rockets": "Rockets",
    "Golden State Warriors": "Warriors",
    "New York Knicks": "Knicks",
    "Indiana Pacers": "Pacers"
}

top10["Short_Team"] = top10["Team"].replace(short_names)

def make_clean_slope_chart(data, reg_col, clutch_col, y_label, title, output_file):
    plt.figure(figsize=(10, 9))

    for _, row in data.iterrows():
        plt.plot([0, 1], [row[reg_col], row[clutch_col]], marker="o")
        plt.text(1.03, row[clutch_col], row["Short_Team"], ha="left", va="center", fontsize=8)

    plt.xticks([0, 1], [f"Regular Season {y_label}", f"Clutch {y_label}"])
    plt.ylabel(y_label)
    plt.title(title)
    plt.xlim(-0.1, 1.2)
    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()

# Plot 1: FG%
make_clean_slope_chart(
    top10,
    "reg_fg_pct",
    "clutch_fg_pct",
    "FG%",
    "Top 10 Clutch Teams: Regular-Season vs Clutch FG%",
    "plots/rq3_plot1_fg_pct_slopechart_clean.png"
)

# Plot 2: FT%
make_clean_slope_chart(
    top10,
    "reg_ft_pct",
    "clutch_ft_pct",
    "FT%",
    "Top 10 Clutch Teams: Regular-Season vs Clutch FT%",
    "plots/rq3_plot3_ft_pct_slopechart_clean.png"
)

print("Clean RQ3 slope charts saved successfully.")