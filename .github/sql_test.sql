CREATE TABLE email_result AS SELECT * FROM data_table FULL OUTER JOIN email_table ON data_table.join_id = email_table.join_id;
SELECT * FROM email_result WHERE (column_1%2=0 AND column_2<column_1 AND column_3 LIKE '%1');
