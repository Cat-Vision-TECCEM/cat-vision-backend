/*permissions*/
/*permissions*/
INSERT INTO public.permission_level(name, admin_number,user_number,store_number, product_number) VALUES ('Free plan', 1, 1, 1,5);
INSERT INTO public.permission_level(name, admin_number,user_number,store_number, product_number) VALUES ('Basic', 2, 5, 10,10);
INSERT INTO public.permission_level(name, admin_number,user_number,store_number, product_number) VALUES ('Standard' , 3, 10, 20,15);
INSERT INTO public.permission_level(name, admin_number,user_number,store_number, product_number) VALUES ('Pro' ,5 , 50, 100,20);
INSERT INTO public.permission_level(name, admin_number,user_number,store_number, product_number) VALUES ('Unlimited' , 25, 1500, 5000,25);


/*company*/
INSERT INTO public.company(name, email, logo, permission_level) VALUES ( 'DonasLandia', 'donas1@gmail.com','https://www.tailorbrands.com/wp-content/uploads/2020/07/mcdonalds-logo.jpg', 1);
INSERT INTO public.company(name, email, logo, permission_level) VALUES ( 'Company2', 'Company2@gmail.com','https://www.tailorbrands.com/wp-content/uploads/2020/07/mcdonalds-logo.jpg', 2);
INSERT INTO public.company(name, email, logo, permission_level) VALUES ( 'Company3', 'Company3@gmail.com','https://www.tailorbrands.com/wp-content/uploads/2020/07/mcdonalds-logo.jpg', 3);
INSERT INTO public.company(name, email, logo, permission_level) VALUES ( 'Company4', 'Company4@gmail.com','https://www.tailorbrands.com/wp-content/uploads/2020/07/mcdonalds-logo.jpg', 4);
INSERT INTO public.company(name, email, logo, permission_level) VALUES ( 'Company5', 'Company5@gmail.com','https://www.tailorbrands.com/wp-content/uploads/2020/07/mcdonalds-logo.jpg', 1);
INSERT INTO public.company(name, email, logo, permission_level) VALUES ( 'Company6', 'Company6@gmail.com','https://www.tailorbrands.com/wp-content/uploads/2020/07/mcdonalds-logo.jpg',2);

/*store*/
INSERT INTO public.store(name, state, street, "number", city, lat, lng) VALUES ('Abarrotes La Diana','Gustavo A. Madero', 'Eten', 604, 'Ciudad de México',19.572791262524557, -99.13816381543546);
INSERT INTO public.store(name, state, street, "number", city, lat, lng) VALUES ('Tienda La vaquita Bel','Gustavo A. Madero', 'Cobán', 562, 'Ciudad de México',19.572791262524557, -99.13816381543546);
INSERT INTO public.store(name, state, street, "number", city, lat, lng) VALUES ('Tienda de Abarrotes La Lupita','Cuauhtémoc', 'Buen Tono', 23, 'Ciudad de México',19.446161734062628, -99.13760835044452);
INSERT INTO public.store(name, state, street, "number", city, lat, lng) VALUES ('Abarrotes Santa Fe','Álvaro Obregón', 'Hidalgo', 57, 'Ciudad de México',19.359304815590463, -99.223313877995);
INSERT INTO public.store(name, state, street, "number", city, lat, lng) VALUES ('Abarrotes Gaby','Benito Juárez', 'Monte Alegre', 33, 'Ciudad de México',19.359304815590463, -99.223313877995);
INSERT INTO public.store(name, state, street, "number", city, lat, lng) VALUES ('Abarrotes La Perla','Cuauhtémoc', 'Roldán', 68, 'Ciudad de México',19.446161734062628, -99.13760835044452);
INSERT INTO public.store(name, state, street, "number", city, lat, lng) VALUES ('Abarrotes Lety','Venustiano Carranza', 'Hojalatería', 64, 'Ciudad de México',19.38647849376789, -99.1589672128544);
INSERT INTO public.store(name, state, street, "number", city, lat, lng) VALUES ('Tienda de Abarrotes Laura','Venustiano Carranza', 'Ferrocarril de Cintura', 43, 'Ciudad de México', 19.433985492158794, -99.10209421628694);
INSERT INTO public.store(name, state, street, "number", city, lat, lng) VALUES ('Abarrotes 2 Hermanos','Iztapalapa', 'Sta.María la Purísima', 337, 'Ciudad de México',19.355749262902567, -99.05292623323336);
INSERT INTO public.store(name, state, street, "number", city, lat, lng) VALUES ('Abarrotes El Gansito','Cuauhtémoc', 'Alfredo Chavero', 131, 'Ciudad de México',19.44429685819842, -99.16048276105165);
INSERT INTO public.store(name, state, street, "number", city, lat, lng)VALUES ('Abarrotes La Luna','Gustavo A. Madero', 'Estela', 60, 'Ciudad de México', 19.503388872220018, -99.12769199719283);
INSERT INTO public.store(name, state, street, "number", city, lat, lng)VALUES ('Abarrotes Reyes','Venustiano Carranza', 'Rosario', 200, 'Ciudad de México',19.436899324864275, -99.10758738025662);

/*company_store*/
INSERT INTO public.company_store(company_id, store_id) VALUES (1, 1);
INSERT INTO public.company_store(company_id, store_id) VALUES (2, 3);
INSERT INTO public.company_store(company_id, store_id) VALUES (2, 2);
INSERT INTO public.company_store(company_id, store_id) VALUES (3, 4);
INSERT INTO public.company_store(company_id, store_id) VALUES (3, 7);
INSERT INTO public.company_store(company_id, store_id) VALUES (3, 5);
INSERT INTO public.company_store(company_id, store_id) VALUES (4, 6);
INSERT INTO public.company_store(company_id, store_id) VALUES (4, 8);
INSERT INTO public.company_store(company_id, store_id) VALUES (5, 10);
INSERT INTO public.company_store(company_id, store_id) VALUES (5, 11);
INSERT INTO public.company_store(company_id, store_id) VALUES (6, 9);
INSERT INTO public.company_store(company_id, store_id) VALUES (6, 12);

/*store_user*/
INSERT INTO public.store_user(store_id,username,password,is_admin,access_token,reset_token) VALUES (1, 'username1', 'Password4321', true, 'accesstoken1', 'resettoken1');
INSERT INTO public.store_user(store_id,username,password,is_admin,access_token,reset_token) VALUES (1, 'username2', 'Password4321', false, 'accesstoken1', 'resettoken1');
INSERT INTO public.store_user(store_id,username,password,is_admin,access_token,reset_token) VALUES (2, 'username3', 'Password4321', true, 'accesstoken1', 'resettoken1');
INSERT INTO public.store_user(store_id,username,password,is_admin,access_token,reset_token) VALUES (2, 'username4', 'Password4321', false, 'accesstoken1', 'resettoken1');
INSERT INTO public.store_user(store_id,username,password,is_admin,access_token,reset_token) VALUES (3, 'username5', 'Password4321', true, 'accesstoken1', 'resettoken1');
INSERT INTO public.store_user(store_id,username,password,is_admin,access_token,reset_token) VALUES (3, 'username6', 'Password4321', false, 'accesstoken1', 'resettoken1');
INSERT INTO public.store_user(store_id,username,password,is_admin,access_token,reset_token) VALUES (4, 'username7', 'Password4321', true, 'accesstoken1', 'resettoken1');
INSERT INTO public.store_user(store_id,username,password,is_admin,access_token,reset_token) VALUES (4, 'username8', 'Password4321', false, 'accesstoken1', 'resettoken1');
INSERT INTO public.store_user(store_id,username,password,is_admin,access_token,reset_token) VALUES (5, 'username9', 'Password4321', false, 'accesstoken1', 'resettoken1');
INSERT INTO public.store_user(store_id,username,password,is_admin,access_token,reset_token) VALUES (5, 'username10', 'Password4321', true, 'accesstoken1', 'resettoken1');
INSERT INTO public.store_user(store_id,username,password,is_admin,access_token,reset_token) VALUES (6, 'username11', 'Password4321', true, 'accesstoken1', 'resettoken1');
INSERT INTO public.store_user(store_id,username,password,is_admin,access_token,reset_token) VALUES (7, 'username12', 'Password4321', true, 'accesstoken1', 'resettoken1');
INSERT INTO public.store_user(store_id,username,password,is_admin,access_token,reset_token) VALUES (8, 'username13', 'Password4321', true, 'accesstoken1', 'resettoken1');
INSERT INTO public.store_user(store_id,username,password,is_admin,access_token,reset_token) VALUES (9, 'username13', 'Password4321', true, 'accesstoken1', 'resettoken1');
INSERT INTO public.store_user(store_id,username,password,is_admin,access_token,reset_token) VALUES (10, 'username14', 'Password4321', true, 'accesstoken1', 'resettoken1');
INSERT INTO public.store_user(store_id,username,password,is_admin,access_token,reset_token) VALUES (11, 'username15', 'Password4321', true, 'accesstoken1', 'resettoken1');
INSERT INTO public.store_user(store_id,username,password,is_admin,access_token,reset_token) VALUES (12, 'username16', 'Password4321', true, 'accesstoken1', 'resettoken1');
INSERT INTO public.store_user(store_id,username,password,is_admin,access_token,reset_token) VALUES (12, 'username17', 'Password4321', true, 'accesstoken1', 'resettoken1');

/*ticket*/
INSERT INTO public.ticket(company_id, body, status, name) VALUES (1, 'Entrega Pendiente', 'pending', 'name1');
INSERT INTO public.ticket(company_id, body, status, name) VALUES (2, 'Productos Entregados', 'closed', 'name2');
INSERT INTO public.ticket(company_id, body, status, name) VALUES (3, 'Ticket Iniciado', 'open', 'name3');
INSERT INTO public.ticket(company_id, body, status, name) VALUES (4, 'Ticket Iniciado', 'open', 'name4');
INSERT INTO public.ticket(company_id, body, status, name) VALUES (5, 'Nuevos productos a entregar', 'received', 'name5');
INSERT INTO public.ticket(company_id, body, status, name) VALUES (6, 'Productos Entregados', 'closed', 'name6');
INSERT INTO public.ticket(company_id, body, status, name) VALUES (6, 'Entrega Pendiente', 'pending', 'name7');
INSERT INTO public.ticket(company_id, body, status, name) VALUES (6, 'Productos Entregados', 'closed', 'name8');
INSERT INTO public.ticket(company_id, body, status, name) VALUES (1, 'Nuevos productos a entregar', 'received', 'name9');
INSERT INTO public.ticket(company_id, body, status, name) VALUES (2, 'Productos Entregados', 'closed', 'name10');
INSERT INTO public.ticket(company_id, body, status, name) VALUES (2, 'Ticket Iniciado', 'open', 'name11');
INSERT INTO public.ticket(company_id, body, status, name) VALUES (3, 'Entrega Pendiente', 'pending', 'name12');
INSERT INTO public.ticket(company_id, body, status, name) VALUES (3, 'Entrega Recibida', 'received', 'name13');
INSERT INTO public.ticket(company_id, body, status, name) VALUES (4, 'Entrega Pendiente', 'pending', 'name14');
INSERT INTO public.ticket(company_id, body, status, name) VALUES (4, 'Ticket Iniciado', 'open', 'name15');
INSERT INTO public.ticket(company_id, body, status, name) VALUES (5, 'Entrega Recibida', 'received', 'name16');
INSERT INTO public.ticket(company_id, body, status, name) VALUES (5, 'Ticket Iniciado', 'open', 'name17');
INSERT INTO public.ticket(company_id, body, status, name) VALUES (2, 'Productos Entregados', 'closed', 'name18');
INSERT INTO public.ticket(company_id, body, status, name) VALUES (1, 'Productos Entregados', 'closed', 'name19');

/*company_user*/
INSERT INTO public.company_user(company_id, username, password, is_admin, access_token, reset_token) VALUES (1, 'username1', 'Password4321', true, 'accesstoken1', 'resettoken1');
INSERT INTO public.company_user(company_id, username, password, is_admin, access_token, reset_token) VALUES (1, 'username2', 'Password4321', false, 'accesstoken2', 'resettoken2');
INSERT INTO public.company_user(company_id, username, password, is_admin, access_token, reset_token) VALUES (2, 'username3', 'Password4321', false, 'accesstoken3', 'resettoken3');
INSERT INTO public.company_user(company_id, username, password, is_admin, access_token, reset_token) VALUES (2, 'username4', 'Password4321', true, 'accesstoken4', 'resettoken4');
INSERT INTO public.company_user(company_id, username, password, is_admin, access_token, reset_token) VALUES (3, 'username5', 'Password4321', true, 'accesstoken5', 'resettoken5');
INSERT INTO public.company_user(company_id, username, password, is_admin, access_token, reset_token) VALUES (4, 'username6', 'Password4321', true, 'accesstoken6', 'resettoken6');
INSERT INTO public.company_user(company_id, username, password, is_admin, access_token, reset_token) VALUES (5, 'username7', 'Password4321', true, 'accesstoken7', 'resettoken7');
INSERT INTO public.company_user(company_id, username, password, is_admin, access_token, reset_token) VALUES (6, 'username8', 'Password4321', true, 'accesstoken8', 'resettoken8');

/*Order*/
/*primer tanda*/
INSERT INTO public."order"(company_id, store_id, products, total, status) VALUES (1, 1,  '{ciel 600ml,coca cola 600ml,del valle manzana 600ml}',1500.88,  'fulfilled');
INSERT INTO public."order"(company_id, store_id, products, total, status) VALUES (2, 3,  '{fresca 600ml,fresca 600ml,del valle manzana 600ml}', 1200.00,  'active');
INSERT INTO public."order"(company_id, store_id, products, total, status) VALUES (1, 2,  '{coca cola 600ml,ciel 600ml,mundet 600ml}',999.99,  'active');
INSERT INTO public."order"(company_id, store_id, products, total, status) VALUES (2, 1,  '{fuze tea limon blanco 600ml,fresca 600ml,mundet 600ml}',899.48, 'fulfilled');
INSERT INTO public."order"(company_id, store_id, products, total, status) VALUES (6, 9,  '{powerade azul 600ml,ciel 600ml,fuze tea limon blanco 600ml}',500.00,  'active');
INSERT INTO public."order"(company_id, store_id, products, total, status) VALUES (5, 11, '{powerade azul 600ml,coca cola 600ml,powerade azul 600ml}',1800.88, 'active');
INSERT INTO public."order"(company_id, store_id, products, total, status) VALUES (6, 12, '{coca cola 600ml,ciel mineral 600ml,ciel 600ml}',759.99,  'fulfilled');
INSERT INTO public."order"(company_id, store_id, products, total, status) VALUES (4, 10, '{coca cola 600ml,fanta 600ml,leche santa clara fresa 600ml}',687.48,  'active');
/*Segunda tanda*/ /*con fecha editada*/
INSERT INTO public."order"(company_id, store_id, products, datetime, total, status) VALUES (1, 1,  '{ciel 600ml,coca cola 600ml,del valle manzana 600ml}','2022-11-14'::timestamp,1500.88,  'fulfilled');
INSERT INTO public."order"(company_id, store_id, products, datetime, total, status) VALUES (2, 3,  '{fresca 600ml,fresca 600ml,del valle manzana 600ml}','2022-11-15'::timestamp, 1200.00,  'active');
INSERT INTO public."order"(company_id, store_id, products, datetime, total, status) VALUES (1, 2,  '{coca cola 600ml,ciel 600ml,mundet 600ml}','2022-10-14'::timestamp,999.99,  'active');
INSERT INTO public."order"(company_id, store_id, products, datetime, total, status) VALUES (2, 1,  '{fuze tea limon blanco 600ml,fresca 600ml,mundet 600ml}','2022-10-15'::timestamp,899.48, 'fulfilled');
INSERT INTO public."order"(company_id, store_id, products, datetime, total, status) VALUES (6, 9,  '{powerade azul 600ml,ciel 600ml,fuze tea limon blanco 600ml}','2022-09-14'::timestamp,500.00,  'active');
INSERT INTO public."order"(company_id, store_id, products, datetime, total, status) VALUES (5, 11, '{powerade azul 600ml,coca cola 600ml,powerade azul 600ml}','2022-09-15'::timestamp,1800.88, 'active');
INSERT INTO public."order"(company_id, store_id, products, datetime, total, status) VALUES (6, 12, '{coca cola 600ml,ciel mineral 600ml,ciel 600ml}','2022-08-14'::timestamp,759.99, 'fulfilled');
INSERT INTO public."order"(company_id, store_id, products, datetime, total, status) VALUES (4, 10, '{coca cola 600ml,fanta 600ml,leche santa clara fresa 600ml}','2022-08-15'::timestamp,687.48,  'active');

/*product*/
/*primera tanda*/
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (1,'sku_000', 'ciel 600ml', 10, 'https://drive.google.com/uc?export=view&id=1nHx5OICXWu760uK20j10p0K1QTBRsPtv');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (1,'sku_001','ciel mineral 600ml', 12, 'https://drive.google.com/uc?export=view&id=1BzzXXX-_5l1-1yRO0sWr_wXyq6_-YTS1');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (1,'sku_002','coca cola 600ml', 14, 'https://drive.google.com/uc?export=view&id=1BzzXXX-_5l1-1yRO0sWr_wXyq6_-YTS1');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (1,'sku_003','coca cola lata 355ml', 13, 'https://drive.google.com/uc?export=view&id=1402gdlK3JzqhEatQtCi__6lFZ_AzhA_K');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (1,'sku_004','coca cola light 600ml', 14, 'https://drive.google.com/uc?export=view&id=1tNEVw2dBO8Cx6AVP9sMbFXuQjUZ2SoOE');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (1,'sku_005','del valle mango 400ml', 13, 'https://drive.google.com/uc?export=view&id=1JNyIUnBzl3DzlXm8hDZlmcaeUkldQ9fM');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (1,'sku_006','del valle manzana 400ml', 13, 'https://drive.google.com/uc?export=view&id=1kATESXaq7DkBNm-LSHdUz5qyNN8p7JKv');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (1,'sku_007','fanta 600ml', 15, 'https://drive.google.com/uc?export=view&id=1NhBniy-xfIQjV0n0ukH_0YKiXAj1y5up');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (1,'sku_008','fresca 600ml', 15, 'https://drive.google.com/uc?export=view&id=1MlJ-wRHk2pIgeFH9LFgMJJ26RvpLqU37');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (1,'sku_009','fuze tea durazno 600ml', 14, 'https://drive.google.com/uc?export=view&id=1kOzNAu1qRLEoWWAjdKgREft5ANx5w9s1');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (1,'sku_010','fuze tea limon blanco 600ml', 14, 'https://drive.google.com/uc?export=view&id=1RYJQsmMnZ2z7bovUJ4tL8dYwBIHul4qY');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (1,'sku_011','leche santa clara fresa 600ml', 11, 'https://drive.google.com/uc?export=view&id=1m0IDs2oF8jS8OoFO4OCJX8K6PJsX-AZX');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (1,'sku_012','mundet 600ml', 14, 'https://drive.google.com/uc?export=view&id=1CC-B1JztkK8AjhFTP7ytw2ViFW9KppqB');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (1,'sku_013','naranja y nada 600ml', 15, 'https://drive.google.com/uc?export=view&id=17OKKrwCjKEaArdppmG41wQSN_XqB6xzb');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (1,'sku_014','powerade moras 355ml', 13, 'https://drive.google.com/uc?export=view&id=1Ez7t6UKUK2unogQazeHeh343Kfkc1WFi');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (1,'sku_015','powerade moras 600ml', 14, 'https://drive.google.com/uc?export=view&id=1TBQ-KeHRRsESjxxLdxOMOw8Lj9Oc1NxU');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (1,'sku_016','powerade ponche 600ml', 14, 'https://drive.google.com/uc?export=view&id=1klNuA4y6JjSnKC9yL89PqkiRfyxtNJyF');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (1,'sku_017','sprite 355ml', 14, 'https://drive.google.com/uc?export=view&id=1psmVDdIkPENMCOPpnS8yDmc8Ce_xp7HV');

INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (2,'sku_000', 'ciel 600ml', 10, 'https://drive.google.com/uc?export=view&id=1nHx5OICXWu760uK20j10p0K1QTBRsPtv');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (2,'sku_001','ciel mineral 600ml', 12, 'https://drive.google.com/uc?export=view&id=1BzzXXX-_5l1-1yRO0sWr_wXyq6_-YTS1');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (2,'sku_002','coca cola 600ml', 14, 'https://drive.google.com/uc?export=view&id=1BzzXXX-_5l1-1yRO0sWr_wXyq6_-YTS1');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (2,'sku_003','coca cola lata 355ml', 13, 'https://drive.google.com/uc?export=view&id=1402gdlK3JzqhEatQtCi__6lFZ_AzhA_K');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (2,'sku_004','coca cola light 600ml', 14, 'https://drive.google.com/uc?export=view&id=1tNEVw2dBO8Cx6AVP9sMbFXuQjUZ2SoOE');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (2,'sku_005','del valle mango 400ml', 13, 'https://drive.google.com/uc?export=view&id=1JNyIUnBzl3DzlXm8hDZlmcaeUkldQ9fM');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (2,'sku_006','del valle manzana 400ml', 13, 'https://drive.google.com/uc?export=view&id=1kATESXaq7DkBNm-LSHdUz5qyNN8p7JKv');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (2,'sku_007','fanta 600ml', 15, 'https://drive.google.com/uc?export=view&id=1NhBniy-xfIQjV0n0ukH_0YKiXAj1y5up');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (2,'sku_008','fresca 600ml', 15, 'https://drive.google.com/uc?export=view&id=1MlJ-wRHk2pIgeFH9LFgMJJ26RvpLqU37');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (2,'sku_009','fuze tea durazno 600ml', 14, 'https://drive.google.com/uc?export=view&id=1kOzNAu1qRLEoWWAjdKgREft5ANx5w9s1');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (2,'sku_010','fuze tea limon blanco 600ml', 14, 'https://drive.google.com/uc?export=view&id=1RYJQsmMnZ2z7bovUJ4tL8dYwBIHul4qY');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (2,'sku_011','leche santa clara fresa 600ml', 11, 'https://drive.google.com/uc?export=view&id=1m0IDs2oF8jS8OoFO4OCJX8K6PJsX-AZX');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (2,'sku_012','mundet 600ml', 14, 'https://drive.google.com/uc?export=view&id=1CC-B1JztkK8AjhFTP7ytw2ViFW9KppqB');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (2,'sku_013','naranja y nada 600ml', 15, 'https://drive.google.com/uc?export=view&id=17OKKrwCjKEaArdppmG41wQSN_XqB6xzb');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (2,'sku_014','powerade moras 355ml', 13, 'https://drive.google.com/uc?export=view&id=1Ez7t6UKUK2unogQazeHeh343Kfkc1WFi');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (2,'sku_015','powerade moras 600ml', 14, 'https://drive.google.com/uc?export=view&id=1TBQ-KeHRRsESjxxLdxOMOw8Lj9Oc1NxU');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (2,'sku_016','powerade ponche 600ml', 14, 'https://drive.google.com/uc?export=view&id=1klNuA4y6JjSnKC9yL89PqkiRfyxtNJyF');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (2,'sku_017','sprite 355ml', 14, 'https://drive.google.com/uc?export=view&id=1psmVDdIkPENMCOPpnS8yDmc8Ce_xp7HV');

INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (3,'sku_000', 'ciel 600ml', 10, 'https://drive.google.com/uc?export=view&id=1nHx5OICXWu760uK20j10p0K1QTBRsPtv');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (3,'sku_001','ciel mineral 600ml', 12, 'https://drive.google.com/uc?export=view&id=1BzzXXX-_5l1-1yRO0sWr_wXyq6_-YTS1');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (3,'sku_002','coca cola 600ml', 14, 'https://drive.google.com/uc?export=view&id=1BzzXXX-_5l1-1yRO0sWr_wXyq6_-YTS1');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (3,'sku_003','coca cola lata 355ml', 13, 'https://drive.google.com/uc?export=view&id=1402gdlK3JzqhEatQtCi__6lFZ_AzhA_K');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (3,'sku_004','coca cola light 600ml', 14, 'https://drive.google.com/uc?export=view&id=1tNEVw2dBO8Cx6AVP9sMbFXuQjUZ2SoOE');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (3,'sku_005','del valle mango 400ml', 13, 'https://drive.google.com/uc?export=view&id=1JNyIUnBzl3DzlXm8hDZlmcaeUkldQ9fM');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (3,'sku_006','del valle manzana 400ml', 13, 'https://drive.google.com/uc?export=view&id=1kATESXaq7DkBNm-LSHdUz5qyNN8p7JKv');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (3,'sku_007','fanta 600ml', 15, 'https://drive.google.com/uc?export=view&id=1NhBniy-xfIQjV0n0ukH_0YKiXAj1y5up');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (3,'sku_008','fresca 600ml', 15, 'https://drive.google.com/uc?export=view&id=1MlJ-wRHk2pIgeFH9LFgMJJ26RvpLqU37');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (3,'sku_009','fuze tea durazno 600ml', 14, 'https://drive.google.com/uc?export=view&id=1kOzNAu1qRLEoWWAjdKgREft5ANx5w9s1');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (3,'sku_010','fuze tea limon blanco 600ml', 14, 'https://drive.google.com/uc?export=view&id=1RYJQsmMnZ2z7bovUJ4tL8dYwBIHul4qY');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (3,'sku_011','leche santa clara fresa 600ml', 11, 'https://drive.google.com/uc?export=view&id=1m0IDs2oF8jS8OoFO4OCJX8K6PJsX-AZX');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (3,'sku_012','mundet 600ml', 14, 'https://drive.google.com/uc?export=view&id=1CC-B1JztkK8AjhFTP7ytw2ViFW9KppqB');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (3,'sku_013','naranja y nada 600ml', 15, 'https://drive.google.com/uc?export=view&id=17OKKrwCjKEaArdppmG41wQSN_XqB6xzb');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (3,'sku_014','powerade moras 355ml', 13, 'https://drive.google.com/uc?export=view&id=1Ez7t6UKUK2unogQazeHeh343Kfkc1WFi');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (3,'sku_015','powerade moras 600ml', 14, 'https://drive.google.com/uc?export=view&id=1TBQ-KeHRRsESjxxLdxOMOw8Lj9Oc1NxU');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (3,'sku_016','powerade ponche 600ml', 14, 'https://drive.google.com/uc?export=view&id=1klNuA4y6JjSnKC9yL89PqkiRfyxtNJyF');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (3,'sku_017','sprite 355ml', 14, 'https://drive.google.com/uc?export=view&id=1psmVDdIkPENMCOPpnS8yDmc8Ce_xp7HV');

INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (4,'sku_000', 'ciel 600ml', 10, 'https://drive.google.com/uc?export=view&id=1nHx5OICXWu760uK20j10p0K1QTBRsPtv');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (4,'sku_001','ciel mineral 600ml', 12, 'https://drive.google.com/uc?export=view&id=1BzzXXX-_5l1-1yRO0sWr_wXyq6_-YTS1');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (4,'sku_002','coca cola 600ml', 14, 'https://drive.google.com/uc?export=view&id=1BzzXXX-_5l1-1yRO0sWr_wXyq6_-YTS1');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (4,'sku_003','coca cola lata 355ml', 13, 'https://drive.google.com/uc?export=view&id=1402gdlK3JzqhEatQtCi__6lFZ_AzhA_K');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (4,'sku_004','coca cola light 600ml', 14, 'https://drive.google.com/uc?export=view&id=1tNEVw2dBO8Cx6AVP9sMbFXuQjUZ2SoOE');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (4,'sku_005','del valle mango 400ml', 13, 'https://drive.google.com/uc?export=view&id=1JNyIUnBzl3DzlXm8hDZlmcaeUkldQ9fM');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (4,'sku_006','del valle manzana 400ml', 13, 'https://drive.google.com/uc?export=view&id=1kATESXaq7DkBNm-LSHdUz5qyNN8p7JKv');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (4,'sku_007','fanta 600ml', 15, 'https://drive.google.com/uc?export=view&id=1NhBniy-xfIQjV0n0ukH_0YKiXAj1y5up');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (4,'sku_008','fresca 600ml', 15, 'https://drive.google.com/uc?export=view&id=1MlJ-wRHk2pIgeFH9LFgMJJ26RvpLqU37');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (4,'sku_009','fuze tea durazno 600ml', 14, 'https://drive.google.com/uc?export=view&id=1kOzNAu1qRLEoWWAjdKgREft5ANx5w9s1');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (4,'sku_010','fuze tea limon blanco 600ml', 14, 'https://drive.google.com/uc?export=view&id=1RYJQsmMnZ2z7bovUJ4tL8dYwBIHul4qY');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (4,'sku_011','leche santa clara fresa 600ml', 11, 'https://drive.google.com/uc?export=view&id=1m0IDs2oF8jS8OoFO4OCJX8K6PJsX-AZX');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (4,'sku_012','mundet 600ml', 14, 'https://drive.google.com/uc?export=view&id=1CC-B1JztkK8AjhFTP7ytw2ViFW9KppqB');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (4,'sku_013','naranja y nada 600ml', 15, 'https://drive.google.com/uc?export=view&id=17OKKrwCjKEaArdppmG41wQSN_XqB6xzb');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (4,'sku_014','powerade moras 355ml', 13, 'https://drive.google.com/uc?export=view&id=1Ez7t6UKUK2unogQazeHeh343Kfkc1WFi');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (4,'sku_015','powerade moras 600ml', 14, 'https://drive.google.com/uc?export=view&id=1TBQ-KeHRRsESjxxLdxOMOw8Lj9Oc1NxU');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (4,'sku_016','powerade ponche 600ml', 14, 'https://drive.google.com/uc?export=view&id=1klNuA4y6JjSnKC9yL89PqkiRfyxtNJyF');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (4,'sku_017','sprite 355ml', 14, 'https://drive.google.com/uc?export=view&id=1psmVDdIkPENMCOPpnS8yDmc8Ce_xp7HV');

INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (5,'sku_000', 'ciel 600ml', 10, 'https://drive.google.com/uc?export=view&id=1nHx5OICXWu760uK20j10p0K1QTBRsPtv');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (5,'sku_001','ciel mineral 600ml', 12, 'https://drive.google.com/uc?export=view&id=1BzzXXX-_5l1-1yRO0sWr_wXyq6_-YTS1');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (5,'sku_002','coca cola 600ml', 14, 'https://drive.google.com/uc?export=view&id=1BzzXXX-_5l1-1yRO0sWr_wXyq6_-YTS1');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (5,'sku_003','coca cola lata 355ml', 13, 'https://drive.google.com/uc?export=view&id=1402gdlK3JzqhEatQtCi__6lFZ_AzhA_K');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (5,'sku_004','coca cola light 600ml', 14, 'https://drive.google.com/uc?export=view&id=1tNEVw2dBO8Cx6AVP9sMbFXuQjUZ2SoOE');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (5,'sku_005','del valle mango 400ml', 13, 'https://drive.google.com/uc?export=view&id=1JNyIUnBzl3DzlXm8hDZlmcaeUkldQ9fM');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (5,'sku_006','del valle manzana 400ml', 13, 'https://drive.google.com/uc?export=view&id=1kATESXaq7DkBNm-LSHdUz5qyNN8p7JKv');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (5,'sku_007','fanta 600ml', 15, 'https://drive.google.com/uc?export=view&id=1NhBniy-xfIQjV0n0ukH_0YKiXAj1y5up');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (6,'sku_008','fresca 600ml', 15, 'https://drive.google.com/uc?export=view&id=1MlJ-wRHk2pIgeFH9LFgMJJ26RvpLqU37');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (6,'sku_009','fuze tea durazno 600ml', 14, 'https://drive.google.com/uc?export=view&id=1kOzNAu1qRLEoWWAjdKgREft5ANx5w9s1');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (6,'sku_010','fuze tea limon blanco 600ml', 14, 'https://drive.google.com/uc?export=view&id=1RYJQsmMnZ2z7bovUJ4tL8dYwBIHul4qY');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (6,'sku_011','leche santa clara fresa 600ml', 11, 'https://drive.google.com/uc?export=view&id=1m0IDs2oF8jS8OoFO4OCJX8K6PJsX-AZX');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (6,'sku_012','mundet 600ml', 14, 'https://drive.google.com/uc?export=view&id=1CC-B1JztkK8AjhFTP7ytw2ViFW9KppqB');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (6,'sku_013','naranja y nada 600ml', 15, 'https://drive.google.com/uc?export=view&id=17OKKrwCjKEaArdppmG41wQSN_XqB6xzb');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (6,'sku_014','powerade moras 355ml', 13, 'https://drive.google.com/uc?export=view&id=1Ez7t6UKUK2unogQazeHeh343Kfkc1WFi');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (6,'sku_015','powerade moras 600ml', 14, 'https://drive.google.com/uc?export=view&id=1TBQ-KeHRRsESjxxLdxOMOw8Lj9Oc1NxU');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (6,'sku_016','powerade ponche 600ml', 14, 'https://drive.google.com/uc?export=view&id=1klNuA4y6JjSnKC9yL89PqkiRfyxtNJyF');
INSERT INTO public.product(company_id,sku,name, selling_price, image) VALUES (6,'sku_017','sprite 355ml', 14, 'https://drive.google.com/uc?export=view&id=1psmVDdIkPENMCOPpnS8yDmc8Ce_xp7HV');




/*store_product*/
/*Primera tanda*/
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (1, 1, false);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (3, 2, true);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (5, 3, true);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (15, 5, false);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (16, 1, true);

/*Segunda Tanda*/
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (1, 1, false);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (31,1, false);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (32,1, true);


INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (15, 2, false);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (16, 2, true);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (1, 2, false);


INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (30,3, true);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (29,3, true);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (28, 3, false);


INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (1, 4, false);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (1, 4, false);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (3, 4, true);


INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (25, 5, false);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (24, 5, true);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (23,5, false);


INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (5, 6, true);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (23,6, true);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (24, 6, false);


INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (2, 7, true);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (3, 7, true);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (29, 7, false);


INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (3, 8, true);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (5, 8, true);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (15, 8, false);


INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (17,9, true);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (18,9, true);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (19, 9, false);



INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (8,10, true);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (9,10, true);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (10, 10, false);


INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (11,11,true);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (12,11,true);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (16,11,false);


INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (13, 12, true);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (14, 12, true);
INSERT INTO public.store_product(product_id, store_id, in_stock)VALUES (15, 12, false);


/*refrigerator*/
INSERT INTO public.refrigerator(company_id) VALUES (1);
INSERT INTO public.refrigerator(company_id) VALUES (1);
INSERT INTO public.refrigerator(company_id) VALUES (2);
INSERT INTO public.refrigerator(company_id) VALUES (2);
INSERT INTO public.refrigerator(Company_id) VALUES (3);
INSERT INTO public.refrigerator(company_id) VALUES (3);
INSERT INTO public.refrigerator(company_id) VALUES (4);
INSERT INTO public.refrigerator(company_id) VALUES (4);
INSERT INTO public.refrigerator(company_id) VALUES (5);
INSERT INTO public.refrigerator(company_id) VALUES (5);
INSERT INTO public.refrigerator(company_id) VALUES (6);
INSERT INTO public.refrigerator(company_id) VALUES (6);
INSERT INTO public.refrigerator(company_id) VALUES (6);
INSERT INTO public.refrigerator(company_id) VALUES (6);
INSERT INTO public.refrigerator(company_id) VALUES (2);
INSERT INTO public.refrigerator(company_id) VALUES (1);
INSERT INTO public.refrigerator(company_id) VALUES (4);
INSERT INTO public.refrigerator(company_id) VALUES (3);

/*refrigerator_product*/
INSERT INTO public.refrigerator_product(refrigerator_id, product_id) VALUES (5, 2);
INSERT INTO public.refrigerator_product(refrigerator_id, product_id) VALUES (6, 1);
INSERT INTO public.refrigerator_product(refrigerator_id, product_id) VALUES (7, 3);
INSERT INTO public.refrigerator_product(refrigerator_id, product_id) VALUES (8, 4);
INSERT INTO public.refrigerator_product(refrigerator_id, product_id) VALUES (9, 6);
INSERT INTO public.refrigerator_product(refrigerator_id, product_id) VALUES (10, 5);
