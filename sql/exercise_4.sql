SELECT *,
(revenue-budget) as profit,
(((revenue-budget)/budget) * 100) as profit_percent
from financials
