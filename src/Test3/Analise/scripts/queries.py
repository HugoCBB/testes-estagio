queries = {
    "top10_trimestre": """
        SELECT operadora, SUM(valor) AS total_despesas
        FROM despesas_saude
        WHERE categoria = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
        AND data >= DATE_TRUNC('quarter', CURRENT_DATE) - INTERVAL '3 months'
        GROUP BY operadora
        ORDER BY total_despesas DESC
        LIMIT 10;
    """,
    "top10_ano": """
        SELECT operadora, SUM(valor) AS total_despesas
        FROM despesas_saude
        WHERE categoria = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
        AND data >= DATE_TRUNC('year', CURRENT_DATE) - INTERVAL '1 year'
        GROUP BY operadora
        ORDER BY total_despesas DESC
        LIMIT 10;
    """
}
