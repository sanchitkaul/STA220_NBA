import time
import pandas as pd
from nba_api.stats.endpoints import leaguedashteamclutch, leaguedashteamstats

SEASON = "2024-25"
SEASON_TYPE = "Regular Season"

def save_df(df: pd.DataFrame, filename: str) -> None:
    df.to_csv(filename, index=False)
    print(f"Saved {filename} | shape={df.shape}")

# 1) Clutch Traditional
clutch_traditional = leaguedashteamclutch.LeagueDashTeamClutch(
    season=SEASON,
    season_type_all_star=SEASON_TYPE,
    per_mode_detailed="PerGame",
    measure_type_detailed_defense="Base",
    clutch_time="Last 5 Minutes",
    ahead_behind="Ahead or Behind",
    point_diff=5,
).get_data_frames()[0]

save_df(clutch_traditional, "data/clutch_traditional.csv")
time.sleep(1)

# 2) Clutch Four Factors
clutch_four_factors = leaguedashteamclutch.LeagueDashTeamClutch(
    season=SEASON,
    season_type_all_star=SEASON_TYPE,
    per_mode_detailed="PerGame",
    measure_type_detailed_defense="Four Factors",
    clutch_time="Last 5 Minutes",
    ahead_behind="Ahead or Behind",
    point_diff=5,
).get_data_frames()[0]

save_df(clutch_four_factors, "clutch_four_factors.csv")
time.sleep(1)

# 3) Regular Season Traditional
regular_traditional = leaguedashteamstats.LeagueDashTeamStats(
    season=SEASON,
    season_type_all_star=SEASON_TYPE,
    per_mode_detailed="PerGame",
    measure_type_detailed_defense="Base",
).get_data_frames()[0]

save_df(regular_traditional, "data/regular_traditional.csv")

print("Done.")