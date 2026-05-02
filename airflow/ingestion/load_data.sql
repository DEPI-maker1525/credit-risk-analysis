CREATE OR REPLACE TABLE application_test AS
SELECT * FROM read_csv_auto('Data/application_test.csv');

CREATE OR REPLACE TABLE application_train AS 
SELECT * FROM read_csv_auto('Data/application_train.csv');

CREATE OR REPLACE TABLE bureau_balance AS 
SELECT * FROM read_csv_auto('Data/bureau_balance.csv');

CREATE OR REPLACE TABLE bureau AS 
SELECT * FROM read_csv_auto('Data/bureau.csv');

CREATE OR REPLACE TABLE credit_card_balance AS 
SELECT * FROM read_csv_auto('Data/credit_card_balance.csv');

CREATE OR REPLACE TABLE installments_payments AS 
SELECT * FROM read_csv_auto('Data/installments_payments.csv');

CREATE OR REPLACE TABLE pos_cash_balance AS 
SELECT * FROM read_csv_auto('Data/POS_CASH_balance.csv');

CREATE OR REPLACE TABLE previous_application AS 
SELECT * FROM read_csv_auto('Data/previous_application.csv');

CREATE OR REPLACE TABLE sample_submission AS 
SELECT * FROM read_csv_auto('Data/sample_submission.csv');