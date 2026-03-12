import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load merged dataset
df = pd.read_csv("data/nba_clutch_merged.csv")

# Top 10 and bottom 10 teams by clutch win%
top10 = df.sort_values("clutch_win_pct", ascending=False).head(10).copy()
bottom10 = df.sort_values("clutch_win_pct", ascending=True).head(10).copy()
top10 = top10.sort_values("clutch_win_pct", ascending=True)
bottom10 = bottom10.sort_values("clutch_win_pct", ascending=True)
fig, axes = plt.subplots(1, 2, figsize=(16, 8), sharex=True)

# Left plot: Top 10 clutch teams
teams_top = top10["Team"]
y_top = np.arange(len(teams_top))

axes[0].scatter(top10["clutch_efg_pct"], y_top, label="Clutch eFG%", s=80)
axes[0].scatter(top10["clutch_tov_pct"], y_top, label="Clutch TOV%", s=80)
axes[0].scatter(top10["clutch_ft_pct"], y_top, label="Clutch FT%", s=80)

axes[0].set_yticks(y_top)
axes[0].set_yticklabels(teams_top)
axes[0].set_xlabel("Value")
axes[0].set_title("Top 10 Teams by Clutch Win%")

# Right plot: Bottom 10 clutch teams
teams_bottom = bottom10["Team"]
y_bottom = np.arange(len(teams_bottom))

axes[1].scatter(bottom10["clutch_efg_pct"], y_bottom, label="Clutch eFG%", s=80)
axes[1].scatter(bottom10["clutch_tov_pct"], y_bottom, label="Clutch TOV%", s=80)
axes[1].scatter(bottom10["clutch_ft_pct"], y_bottom, label="Clutch FT%", s=80)

axes[1].set_yticks(y_bottom)
axes[1].set_yticklabels(teams_bottom)
axes[1].set_xlabel("Value")
axes[1].set_title("Bottom 10 Teams by Clutch Win%")

handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc="upper center", ncol=3)

plt.suptitle("Comparison of Key Clutch Stats: Top 10 vs Bottom 10 Teams", y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig("plots/rq2_top10_bottom10_dotplot.png")
plt.show()

print("Saved as rq2_top10_bottom10_dotplot.png")