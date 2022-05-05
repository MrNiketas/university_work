INSERT salon(name_salon, address) 
VALUES ('Глобус', '​Бастионная, 29/5э'),
('RTD', '​Бульвар Строителей, 55');

INSERT manager(manager_name, telephone, experience) 
VALUES ('Bob', 79537220909, 3 ),
('Nick', 5515115, 5 );

INSERT client(clien_name, address, telephone, discount) 
VALUES ('Rob','Советская 21',  79531111, 10);

INSERT avto(model, avto_name, date_production, color, country) 
VALUES ('Tesla', 'Model 3', '2001', 'black', 'USA' );

INSERT orders(id_avto, id_manager, id_client, date_buy, name_salon) 
VALUES (1, 1, 1, 2020, 'Глобус');
