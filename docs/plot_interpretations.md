# Plot Interpretations: NBA Clutch Performance Analysis

This document describes and interprets the visualizations produced for the NBA clutch performance statistics project. The project examines team clutch performance in relation to regular-season performance and investigates which team-level factors best explain clutch success.

---

## 1. `rq1_plot1_reg_vs_clutch_win_shortnames.png`

This is a scatter plot of regular-season win percentage versus clutch win percentage, with abbreviated team names for improved readability.

**Interpretation:** The plot shows a general positive relationship between regular-season success and clutch success. Teams with higher regular-season win percentages tend to also have higher clutch win percentages. However, the relationship is not perfect, and some teams perform better or worse in clutch situations than their overall season record would suggest. The use of short team names reduces label overlap and makes individual teams easier to identify.

**How it helps:** This plot addresses whether strong regular-season teams are also strong clutch teams by directly comparing team success in both contexts.

---

## 2. `rq1_plot2_clutch_minus_reg_win_shortnames.png`

This is a bar chart showing the difference between clutch win percentage and regular-season win percentage for each team, with abbreviated team names.

**Interpretation:** This plot highlights teams that overperform or underperform in clutch situations relative to their overall regular-season level. Teams with positive values are relatively better in clutch moments than their season record suggests, while teams with negative values are relatively worse in clutch moments. The shorter labels improve readability along the x-axis.

**How it helps:** This plot complements the first RQ1 scatter plot by identifying exceptions to the overall trend and showing that clutch performance is not explained entirely by regular-season success.

---

## 3. `rq2_heatmap.png`

This is a correlation heatmap of clutch success factors.

**Variables included:**
- clutch_win_pct
- clutch_fg_pct
- clutch_3p_pct
- clutch_ft_pct
- clutch_efg_pct
- clutch_tov
- clutch_tov_pct
- clutch_reb
- clutch_orb_pct
- clutch_ft_rate
- clutch_fta

**Interpretation:** The heatmap indicates that clutch success is most strongly associated with shooting efficiency and turnover control. Among the positive relationships, clutch effective field goal percentage has the strongest positive correlation with clutch win percentage. Clutch three-point percentage and clutch free-throw rate also show positive relationships. Among the negative relationships, clutch turnovers and clutch turnover percentage show the strongest negative correlations with clutch win percentage. Rebounding appears to have a weaker relationship with clutch success.

**How it helps:** This plot gives the broad exploratory view for RQ2 and helps identify which factors appear most important before selecting more focused follow-up plots.

---

## 4. `rq2_scatter_efg_vs_win.png`

This is a scatter plot of clutch effective field goal percentage versus clutch win percentage.

**Interpretation:** The plot shows that teams with higher clutch effective field goal percentages generally tend to have higher clutch win percentages. This supports the idea that shooting efficiency is a major driver of clutch success. The plot also allows identification of team-level outliers that do not follow the overall trend perfectly.

**How it helps:** This plot directly investigates the strongest positive factor identified in the heatmap and provides focused evidence that efficient scoring is strongly related to clutch success.

---

## 5. `rq2_quadrant_efg_vs_tov.png`

This is a quadrant plot of clutch effective field goal percentage versus clutch turnover percentage, with mean reference lines.

**Interpretation:** The plot suggests that the strongest clutch team profile is high clutch eFG% combined with low clutch turnover percentage. Teams in the favorable quadrant tend to combine efficient shooting with strong ball security, while teams in the opposite quadrant tend to show the weakest clutch statistical profile. This indicates that clutch success is best explained by the joint effect of scoring efficiency and turnover control rather than by either factor alone.

**How it helps:** This plot combines the strongest positive and strongest negative clutch indicators found in the heatmap, helping explain how the two most important factors work together to shape clutch performance.

---

## 6. `rq2_top10_bottom10_dotplot.png`

This is a side-by-side horizontal dot plot comparing the top 10 and bottom 10 teams by clutch win percentage using clutch eFG%, clutch TOV%, and clutch FT%.

**Interpretation:** The plot compares the strongest and weakest clutch teams across key clutch indicators. In general, the top clutch teams tend to show higher clutch eFG% and lower clutch turnover percentage than the bottom clutch teams. Free-throw percentage may also differ, but the contrast is usually strongest for shooting efficiency and turnover control.

**How it helps:** This plot gives a more concrete team-level comparison between successful and unsuccessful clutch teams, reinforcing the conclusion that shooting efficiency and ball security are the strongest explanatory factors for clutch success.

---

## 7. `rq3_plot1_fg_pct_slopechart_clean.png`

This is a slope chart comparing regular-season field goal percentage to clutch field goal percentage for the top 10 teams by clutch win percentage.

**Interpretation:** Each line connects a team's regular-season FG% to its clutch FG%. The plot reveals whether top clutch teams maintain, improve, or decline in two-point and overall field goal efficiency when moving from regular-season to clutch play. Steep slopes indicate large shifts between contexts.

**How it helps:** This plot addresses how shooting efficiency changes from regular season to clutch for the best clutch teams, complementing RQ2 by focusing on within-team variation across contexts.

---

## 8. `rq3_plot2_3p_pct_dumbbell.png`

This is a dumbbell plot comparing regular-season three-point percentage to clutch three-point percentage for the top 10 teams by clutch win percentage.

**Interpretation:** Each horizontal line connects a team's regular-season 3P% (one marker) to its clutch 3P% (another marker). The plot shows whether top clutch teams shoot better or worse from beyond the arc in clutch situations compared with the full season. The horizontal layout makes team-by-team comparison straightforward.

**How it helps:** This plot isolates three-point shooting as a factor that may change between regular season and clutch play, supporting analysis of whether long-range efficiency contributes to clutch success.

---

## 9. `rq3_plot3_ft_pct_slopechart_clean.png`

This is a slope chart comparing regular-season free-throw percentage to clutch free-throw percentage for the top 10 teams by clutch win percentage.

**Interpretation:** Each line connects a team's regular-season FT% to its clutch FT%. The plot shows whether top clutch teams maintain or change their free-throw accuracy in clutch moments. Free throws are often critical in close games, so stability or improvement in FT% in clutch situations may be relevant to clutch success.

**How it helps:** This plot examines free-throw generation and accuracy in the regular season versus clutch, contributing to the analysis of which shooting factors matter most for clutch performance.
