
create TABLE UserType(
    id integer PRIMARY KEY autoincrement,
    name varchar(50)
);

create TABLE Users(
    id integer PRIMARY KEY autoincrement,
    fio varchar(50),
    phone_number varchar(50),
    login varchar(50) not null unique,
    password varchar(50) not null,
    user_type_id integer,
    foreign key (user_type_id) references UserType(id)
);

create TABLE TaskStatus(
    id integer PRIMARY KEY autoincrement,
    name varchar(50)
);

create TABLE TechType(
    id integer PRIMARY KEY autoincrement,
    name varchar(50)
);

create TABLE TechModel(
    id integer PRIMARY KEY autoincrement,
    name varchar(50)
);

create TABLE TechBrand(
    id integer PRIMARY KEY autoincrement,
    name varchar(50)
);

create TABLE Tech(
    id integer primary key autoincrement,
    type_id integer,
    model_id integer,
    brand_id integer,
    foreign key(type_id) references TechType(id),
    foreign key(model_id) references TechModel(id),
    foreign key(brand_id) references TechBrand(id)
);

create TABLE Task(
    id integer PRIMARY KEY autoincrement,
    status_id integer,
    tech_id integer,
    problem_description varchar(100),
    start_date date,
    completion_date date,
    master_id integer,
    client_id integer,
    foreign key (status_id) references TaskStatus(id),
    foreign key (tech_id) references Tech(id),
    foreign key (master_id) references Users(id),
    foreign key (client_id) references Users(id)
);

create TABLE Comments(
    id integer PRIMARY KEY autoincrement,
    text varchar(200),
    task_id integer,
    master_id integer,
    foreign key (task_id) references  Task(id),
    foreign key (master_id) references  Users(id)
);

create TABLE Part(
    id integer PRIMARY KEY autoincrement,
    name varchar(50)
);

create TABLE PartRequest(
    id integer primary key autoincrement,
    received bool,
    part_id integer,
    task_id integer,
    foreign key(part_id) references Part(id),
    foreign key(task_id) references Task(id)
);

insert into TechType(name) values("Кондиционер") , ("Увлажнитель воздуха"), ("Сушилка для рук");

insert into TechBrand(name) values("TCL TAC-12CHSA"), ("Electrolux EACS"), ("Xiaomi"), ("Polaris"), ("Ballu");

insert into TechModel(name)
    values("TPG-W белый"), ("I-09HAT/N3_21Y белый"), ("Smart Humidifier 2"), ("PUH 2300 WIFI IQ Home"), ("BAHD-1250");

insert into Tech(type_id,brand_id,model_id)
    values("1","1","1"), ("1","2","2"), ("2","3","3"), ("2","4","4"), ("3","5","5");

insert into UserType(name) values("Пользователь"), ("Специалист"), ("Оператор"),("Менеджер");

insert into TaskStatus(name)
    values("Новая заявка"), ("В процессе ремонта"), ("Готова к выдаче"), ("Ожидание Комплектующих");

insert into Users(fio, phone_number, login, password, user_type_id)
    values("fio", "111-111-111", "1", "1", "3");