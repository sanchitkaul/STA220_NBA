import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/nba_clutch_merged.csv")

# Variables for RQ2 heatmap
rq2_vars = [
    "clutch_win_pct",
    "clutch_fg_pct",
    "clutch_3p_pct",
    "clutch_ft_pct",
    "clutch_efg_pct",
    "clutch_tov",
    "clutch_tov_pct",
    "clutch_reb",
    "clutch_orb_pct",
    "clutch_ft_rate",
    "clutch_fta"
]

corr = df[rq2_vars].corr()

# Plot heatmap
plt.figure(figsize=(12, 8))
plt.imshow(corr, aspect="auto")
plt.colorbar()

plt.xticks(range(len(rq2_vars)), rq2_vars, rotation=45, ha="right")
plt.yticks(range(len(rq2_vars)), rq2_vars)

# Add correlation values inside cells
for i in range(len(corr)):
    for j in range(len(corr.columns)):
        plt.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center", fontsize=8)

plt.title("Correlation Heatmap of Clutch Success Factors")
plt.tight_layout()
plt.savefig("plots/rq2_heatmap.png")
plt.show()

print("Heatmap saved as rq2_heatmap.png")