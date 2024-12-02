few_shots = [
    {
        "Question": "How many t-shirts do we have left for nike in extra small size and white color",
        "SQLQuery": "SELECT SUM(stock_quantity FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size='XS')",
        "SQLResult": "Result of the SQL query",
        "Answer": '43'
    },
    {
        "Question": 'How much is the price of the inventory for all small size t-shirts',
        "SQLQuery": "SELECT SUM(price * stock_quantity FROM t_shirts WHERE size ='S'",
        "SQLResult": "Result of the SQL query",
        "Answer": '18018'
    },
    {
        "Question": "If I have to sell all the Levi's T-shirts today with discounts applied. How much revenue does our store generate (post discounts)",
        "SQLQuery": """SELECT SUM(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue
                        FROM (SELECT SUM(price*stock_quantity) as total_amount, t_shirt_id  
                        FROM t_shirts
                        WHERE brand = 'Levi'
                        GROUP BY t_shirt_id)
                        a
                        LEFT JOIN 
                        discounts
                        ON
                        a.t_shirt_id = discounts.t_shirt_id""",
        "SQLResult": "Result of the SQL query",
        "Answer": '27713.800000'
    },
    {
        "Question": "If we have to sell all the Levi's T-shirts today. How much revenue will our store make",
        "SQLQuery": """SELECT SUM(price * stock_quantity)
                        FROM t_shirts
                        WHERE brand = 'Levi' """,
        "SQLResult": "Result of the SQL query",
        "Answer": '31326'
    },
    {
        "Question": "How many white color Levi's t shirts do we have available",
        "SQLQuery": """SELECT SUM(stock_quantity)
                        FROM t_shirts
                        WHERE brand = 'Levi' AND color = 'White'""",
        "SQLResult": "Result of the SQL query",
        "Answer": '133'
    },
]