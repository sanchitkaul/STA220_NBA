import pandas as pd

clutch_trad = pd.read_csv("data/clutch_traditional.csv")
clutch_ff = pd.read_csv("data/clutch_four_factors.csv")
reg_trad = pd.read_csv("data/regular_traditional.csv")

clutch_trad = clutch_trad[
    ["TEAM_NAME", "GP", "W", "L", "W_PCT", "PTS", "FG_PCT", "FG3A", "FG3_PCT", "FT_PCT", "FTA", "REB", "AST", "TOV", "PLUS_MINUS"]
].copy()

clutch_ff = clutch_ff[
    ["TEAM_NAME", "EFG_PCT", "FTA_RATE", "TM_TOV_PCT", "OREB_PCT"]
].copy()

reg_trad = reg_trad[
    ["TEAM_NAME", "GP", "W", "L", "W_PCT", "PTS", "FG_PCT", "FG3A", "FG3_PCT", "FT_PCT", "FTA", "REB", "AST", "TOV", "PLUS_MINUS"]
].copy()

for df in [clutch_trad, clutch_ff, reg_trad]:
    df["TEAM_NAME"] = df["TEAM_NAME"].astype(str).str.strip()

clutch_trad = clutch_trad.rename(columns={
    "TEAM_NAME": "Team",
    "GP": "clutch_gp",
    "W": "clutch_w",
    "L": "clutch_l",
    "W_PCT": "clutch_win_pct",
    "PTS": "clutch_pts",
    "FG_PCT": "clutch_fg_pct",
    "FG3A": "clutch_3pa",
    "FG3_PCT": "clutch_3p_pct",
    "FT_PCT": "clutch_ft_pct",
    "FTA": "clutch_fta",
    "REB": "clutch_reb",
    "AST": "clutch_ast",
    "TOV": "clutch_tov",
    "PLUS_MINUS": "clutch_plus_minus"
})

clutch_ff = clutch_ff.rename(columns={
    "TEAM_NAME": "Team",
    "EFG_PCT": "clutch_efg_pct",
    "FTA_RATE": "clutch_ft_rate",
    "TM_TOV_PCT": "clutch_tov_pct",
    "OREB_PCT": "clutch_orb_pct"
})

reg_trad = reg_trad.rename(columns={
    "TEAM_NAME": "Team",
    "GP": "reg_gp",
    "W": "reg_w",
    "L": "reg_l",
    "W_PCT": "reg_win_pct",
    "PTS": "reg_pts",
    "FG_PCT": "reg_fg_pct",
    "FG3A": "reg_3pa",
    "FG3_PCT": "reg_3p_pct",
    "FT_PCT": "reg_ft_pct",
    "FTA": "reg_fta",
    "REB": "reg_reb",
    "AST": "reg_ast",
    "TOV": "reg_tov",
    "PLUS_MINUS": "reg_plus_minus"
})

print("Duplicates in clutch_trad:", clutch_trad["Team"].duplicated().sum())
print("Duplicates in clutch_ff:", clutch_ff["Team"].duplicated().sum())
print("Duplicates in reg_trad:", reg_trad["Team"].duplicated().sum())

print("Rows:")
print("clutch_trad:", clutch_trad.shape)
print("clutch_ff:", clutch_ff.shape)
print("reg_trad:", reg_trad.shape)

merged = clutch_trad.merge(clutch_ff, on="Team", how="inner")
merged = merged.merge(reg_trad, on="Team", how="inner")

print("\nMerged shape:", merged.shape)
print("Merged teams:", merged["Team"].nunique())
print("\nColumns:")
print(merged.columns.tolist())

merged.to_csv("data/nba_clutch_merged.csv", index=False)

print("\nSaving it as nba_clutch_merged.csv")
print(merged.head())