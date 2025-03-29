SELECT
    reg_ans AS operadora,
    SUM(vl_saldo_final - vl_saldo_inicial) AS total_despesa
FROM despesas
WHERE descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
AND data_movimentacao >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH)
GROUP BY reg_ans
ORDER BY total_despesa DESC
LIMIT 10;
