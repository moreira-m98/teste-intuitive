LOAD DATA INFILE './data/1T2023.csv'
INTO TABLE despesas
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data_movimentacao, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
SET data_movimentacao = STR_TO_DATE(@data_movimentacao, '%d/%m/%Y');