# Data Cleaning Notes

## 1. Project Overview

This project analyzes NBA clutch performance and compares clutch stats with regular season stats. The goal is to produce a single merged dataset suitable for visualization and statistical analysis.

---

## 2. Source Datasets

| Dataset | Description |
|---------|-------------|
| `clutch_traditional.csv` | Per-game traditional stats for teams in clutch situations (last 5 minutes, score within 5 points). |
| `clutch_four_factors.csv` | Four Factors metrics (shooting efficiency, free throw rate, turnover rate, offensive rebounding) in clutch situations. |
| `regular_traditional.csv` | Full-season per-game traditional stats for all teams. |

---

## 3. Columns Kept

**clutch_traditional.csv**
- TEAM_NAME, GP, W, L, W_PCT, PTS, FG_PCT, FG3_PCT, FT_PCT, REB, AST, TOV, PLUS_MINUS

**clutch_four_factors.csv**
- TEAM_NAME, EFG_PCT, FTA_RATE, TM_TOV_PCT, OREB_PCT

**regular_traditional.csv**
- TEAM_NAME, GP, W, L, W_PCT, PTS, FG_PCT, FG3_PCT, FT_PCT, REB, AST, TOV, PLUS_MINUS

---

## 4. Column Renaming

**Clutch Traditional**
| Original | Renamed |
|----------|---------|
| TEAM_NAME | Team |
| GP | clutch_gp |
| W | clutch_w |
| L | clutch_l |
| W_PCT | clutch_win_pct |
| PTS | clutch_pts |
| FG_PCT | clutch_fg_pct |
| FG3_PCT | clutch_3p_pct |
| FT_PCT | clutch_ft_pct |
| REB | clutch_reb |
| AST | clutch_ast |
| TOV | clutch_tov |
| PLUS_MINUS | clutch_plus_minus |

**Clutch Four Factors**
| Original | Renamed |
|----------|---------|
| TEAM_NAME | Team |
| EFG_PCT | clutch_efg_pct |
| FTA_RATE | clutch_ft_rate |
| TM_TOV_PCT | clutch_tov_pct |
| OREB_PCT | clutch_orb_pct |

**Regular Traditional**
| Original | Renamed |
|----------|---------|
| TEAM_NAME | Team |
| GP | reg_gp |
| W | reg_w |
| L | reg_l |
| W_PCT | reg_win_pct |
| PTS | reg_pts |
| FG_PCT | reg_fg_pct |
| FG3_PCT | reg_3p_pct |
| FT_PCT | reg_ft_pct |
| REB | reg_reb |
| AST | reg_ast |
| TOV | reg_tov |
| PLUS_MINUS | reg_plus_minus |

**Column meanings:** Team = team name; _gp = games played; _w/_l = wins/losses; _win_pct = win percentage; _pts = points per game; _fg_pct, _3p_pct, _ft_pct = field goal, three-point, free throw percentage; _reb, _ast, _tov = rebounds, assists, turnovers per game; _plus_minus = plus/minus per game; clutch_efg_pct = effective field goal %; clutch_ft_rate = free throw attempt rate; clutch_tov_pct = team turnover %; clutch_orb_pct = offensive rebound %.

---

## 5. Data Cleaning Steps

- Only relevant columns were kept; all others were dropped.
- Team names were stripped of extra whitespace.
- Columns were renamed for clarity and to distinguish clutch vs. regular stats.
- Data types were checked.
- Duplicate team names were checked before merging.

---

## 6. Merge Process

The three datasets were merged using the `Team` column with inner joins. Clutch traditional was merged with clutch four factors first, then the result was merged with regular traditional. The final output is saved as `nba_clutch_merged.csv`.

---

## 7. Final Dataset Purpose

The merged dataset will be used for visualizations and statistical analysis of clutch performance, including comparisons between clutch and regular-season metrics.
