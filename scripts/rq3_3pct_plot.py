import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Loading the merged dataset
df = pd.read_csv("data/nba_clutch_merged.csv")  

# Top 10 clutch teams
top10 = df.sort_values("clutch_win_pct", ascending=False).head(10).copy()
top10 = top10.sort_values("clutch_win_pct", ascending=True)

# making shorter names
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

y = np.arange(len(top10))

plt.figure(figsize=(10, 7))

# connecting lines
for i in range(len(top10)):
    plt.plot(
        [top10["reg_3p_pct"].iloc[i], top10["clutch_3p_pct"].iloc[i]],
        [y[i], y[i]],
        linewidth=2
    )

plt.scatter(top10["reg_3p_pct"], y, s=90, marker="o", label="Regular Season")
plt.scatter(top10["clutch_3p_pct"], y, s=90, marker="D", label="Clutch")

plt.yticks(y, top10["Short_Team"])
plt.xlabel("3P%")
plt.ylabel("Team")
plt.title("Top 10 Clutch Teams: Regular-Season vs Clutch 3P%")
plt.legend()
plt.tight_layout()
plt.savefig("plots/rq3_plot2_3p_pct_dumbbell.png")
plt.show()