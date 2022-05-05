CREATE TABLE manager (
  id_manager integer primary key auto_increment,
  manager_name varchar(50),
  telephone BIGINT,
  experience int
);

CREATE TABLE client (
  id_client integer primary key auto_increment,
  clien_name varchar(50),
  address varchar(20),
  telephone int,
  discount int
);

CREATE TABLE salon (
  name_salon varchar(20) primary key,
  address varchar(20)
);

create table avto (
	id_avto integer primary key auto_increment,
    model varchar(20),
    avto_name varchar(20),
    date_production int,
    color varchar(20),
    country varchar(20)
);
    
create table orders (
order_id integer primary key auto_increment,
id_avto int not null,
id_manager integer,
id_client integer,
date_buy int,
name_salon varchar(20),
foreign key (id_avto) references avto(id_avto),
foreign key (id_manager) references manager(id_manager),
foreign key (id_client) references client(id_client),
foreign key (name_salon) references salon(name_salon)
);


