CREATE TABLE public.company
(
    company_id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    name varchar(20) NOT NULL,
    email varchar(20) NOT NULL,
    CONSTRAINT companyID_pk PRIMARY KEY(company_id)
);

CREATE TYPE status as ENUM('open','closed','pending','received');
CREATE TABLE public.ticket
(
    ticket_id  INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    company_id INT NOT NULL,
    body varchar(150) NOT NULL,
    status status default 'received',
    name varchar(20) NOT NULL,
    CONSTRAINT ticketID_pk PRIMARY KEY(ticket_id),
    CONSTRAINT ticketCompanyForeign_fk FOREIGN KEY(company_id) REFERENCES public.company(company_id)
);


CREATE TABLE public.store
(
    store_id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    name varchar(50) NOT NULL,
    state varchar(30) NOT NULL,
    street varchar(30) NOT NULL,
    number varchar(10) NOT NULL,
    city varchar(50) NOT NULL,
    lat float NOT NULL,
    lng float NOT NULL,
    CONSTRAINT storeID_pk PRIMARY KEY(store_id),
    CONSTRAINT unique_store UNIQUE(name, state, street, number, city)
);


CREATE TABLE public.company_store
(
    company_store_id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    company_id int NOT NULL,
    store_id int NOT NULL,
    CONSTRAINT companyStoreID_pk PRIMARY KEY(company_store_id),
    CONSTRAINT companyUnionForeign_fk FOREIGN KEY(company_id) REFERENCES public.company(company_id),
    CONSTRAINT storeUnionForeign_fk FOREIGN KEY(store_id) REFERENCES public.store(store_id)
);

CREATE TYPE order_status as ENUM('fulfilled','active');
CREATE TABLE public.order
(
    order_id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    company_id int NOT NULL,
    total float NOT NULL,
    store_id int NOT NULL,
    products varchar(1000) NOT NULL,
    datetime timestamp NOT NULL default current_timestamp,
    status order_status default 'active',
    CONSTRAINT orderID_pk PRIMARY KEY(order_id),
    CONSTRAINT orderCompanyForeign_fk FOREIGN KEY(company_id) REFERENCES public.company(company_id),
    CONSTRAINT orderStoreForeign_fk FOREIGN KEY(store_id) REFERENCES public.store(store_id)
);


CREATE TABLE public.company_user
(
    company_user_id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    company_id int NOT NULL,
    username varchar(20) NOT NULL,
    password varchar(50) NOT NULL,
    is_admin bool NOT NULL default false,
    access_token varchar(1000),
    reset_token varchar(1000),
    CONSTRAINT companyUserID_pk PRIMARY KEY(company_user_id),
    CONSTRAINT UserCompanyForeign_fk FOREIGN KEY(company_id) REFERENCES public.company(company_id)
);

CREATE TABLE public.store_user
(
    store_user_id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    store_id int NOT NULL,
    username varchar(20) NOT NULL,
    password varchar(50) NOT NULL,
    is_admin bool NOT NULL default false,
    access_token varchar(1000),
    reset_token varchar(1000),
    CONSTRAINT companyUserID_pk PRIMARY KEY(company_user_id),
    CONSTRAINT UserStoreForeign_fk FOREIGN KEY(store_id) REFERENCES public.store(store_id)
);

CREATE TABLE public.product
(
    product_id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    company_id int NOT NULL,
    sku varchar(50) NOT NULL,
    name varchar(30) NOT NULL,
    selling_price float NOT NULL,
    image varchar(500) NOT NULL,
    CONSTRAINT productID_pk PRIMARY KEY(product_id),
    CONSTRAINT productCompanyForeign_fk FOREIGN KEY(company_id) REFERENCES public.company(company_id),
    CONSTRAINT unique_sku_company UNIQUE(company_id, sku)
);

CREATE TABLE public.store_product
(
    store_product_id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    product_id int NOT NULL,
    store_id int NOT NULL,
    in_stock bool NOT NULL default true,
    CONSTRAINT productStoreID_pk PRIMARY KEY(store_product_id),
    CONSTRAINT  FOREIGN KEY(product_id) REFERENCES public.product(product_id),
    CONSTRAINT storeProductForeign_fk FOREIGN KEY(store_id) REFERENCES public.store(store_id)
);



CREATE TABLE public.refrigerator
(
    refrigerator_id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    company_id int NOT NULL,
    CONSTRAINT refrigeratorID_pk PRIMARY KEY(refrigerator_id),
    CONSTRAINT refrigeratorCompanyForeign_fk FOREIGN KEY(company_id) REFERENCES public.company(company_id)
);


CREATE TABLE public.refrigerator_product
(
    refrigerator_product_id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    refrigerator_id int NOT NULL,
    product_id int NOT NULL,
    CONSTRAINT refriProductID_pk PRIMARY KEY(refrigerator_product_id),
    CONSTRAINT refriProductForeign_fk FOREIGN KEY(refrigerator_id) REFERENCES public.refrigerator(refrigerator_id),
    CONSTRAINT productRefriForeign_fk FOREIGN KEY(product_id) REFERENCES public.product(product_id)
);