#
Таблица продукты
INSERT INTO Products (Product_name, Product_calories, Product_proteins, Product_fats, Product_carbohydrates)
VALUES
    # Молочная продукция
    ('Творог 5%', 121, 17, 5, 1),
    ('Творог 9%', 161, 17, 9, 1),
    ('Творог 10%', 171, 17, 10, 1),
    ('Творог 15%', 211, 17, 15, 1),
    ('Сыр 15%', 255, 28, 15, 8),
    ('Сыр 20%', 320, 28, 20, 8),
    ('Сыр 25%', 385, 28, 25, 8),
    ('Сыр 30%', 450, 28, 30, 8),
    ('Молоко 2%', 38, 3, 2, 3),
    ('Молоко 3%', 62, 3, 3, 4),
    ('Молоко 4%', 65, 3, 4, 4),
    ('Молоко 5%', 68, 3, 5, 4),
    ('Йогурт', 106, 7, 3, 13),
    ('Кефир', 40, 3, 2, 4),
    ('Сметана 10%', 100, 1, 10, 1),
    ('Сметана 15%', 150, 1, 15, 1),
    ('Сметана 20%', 200, 1, 20, 1),
    ('Масло сливочное', 748, 1, 82, 1),
    #Масла
    ('Масло подсолнечное', 900, 0, 100, 0),
    ('Масло оливковое', 900, 0, 100, 0),
    ('Масло кукурузное', 900, 0, 100, 0),
    ('Масло соевое', 900, 0, 100, 0),
    ('Масло кунжутное', 900, 0, 100, 0),
    ('Масло кокосовое', 900, 0, 100, 0),
    #Мясо и птица
    ('Шея говядина', 150, 19, 11, 0),
    ('Шея свинина', 200, 17, 13, 0),
    ('Говядина вырезка', 146, 21, 7, 0),
    ('Свинина вырезка', 200, 17, 13, 0),
    ('Говядина реберо', 150, 19, 11, 0),
    ('Свинина реберо', 200, 17, 13, 0),
    ('Говядина грудинка', 150, 19, 11, 0),
    ('Свинина грудинка', 200, 17, 13, 0),
    ('Говядина тушка', 150, 19, 11, 0),
    ('Свинина тушка', 200, 17, 13, 0),
    ('Говядина язык', 150, 19, 11, 0),
    ('Свинина язык', 200, 17, 13, 0),
    ('Говядина печень', 150, 19, 11, 0),
    ('Свинина печень', 200, 17, 13, 0),
    ('Говядина сердце', 150, 19, 11, 0),
    ('Свинина сердце', 200, 17, 13, 0),
    ('Говядина почка', 150, 19, 11, 0),
    ('Свинина почка', 200, 17, 13, 0),
    ('Куринное бедро', 221, 17, 16, 0),
    ('Куринное грудка', 172, 21, 9, 0),
    ('Куринное крыло', 221, 17, 16, 0),
    ('Куринное филе', 120, 21, 2, 0),
    ('Куринное сердце', 175, 19, 11, 0),
    ('Куринное печень', 175, 19, 11, 0),
    ('Куринное почка', 175, 19, 11, 0),
    ('Куринное яйцо', 140, 10, 10, 1),
    ('Утка филе', 135, 18, 6, 0),
    ('Утка грудка', 163, 18, 9, 0),
    ('Индейка филе', 111, 21, 1, 0),
    ('Индейка грудка', 163, 18, 9, 0),
    ('Индейка крыло', 210, 18, 14, 0),
    # Рыба и морепродукты
    ('Семга', 170, 20, 9, 0),
    ('Скумбрия', 205, 19, 14, 0),
    ('Сельдь', 158, 18, 9, 0),
    ('Креветка', 100, 24, 0, 0),
    ('Краб', 87, 18, 0, 0),
    ('Кальмар', 100, 18, 2, 0),
    ('Мидии', 80, 17, 0, 0),
    ('Морская капуста', 52, 3, 0, 10),
    #Крупы и макаранные изделия
    ('Гречка', 350, 12, 1, 75),
    ('Рис длиннозерный ', 317, 7, 1, 80),
    ('Рис коричневый', 350, 7, 1, 80),
    ('Рис белый', 350, 7, 1, 80),
    ('Макароны', 350, 11, 1, 75),
    ('Макароны из цельнозерновой муки', 350, 11, 1, 75),
    ('Овсяная крупа', 342, 12, 1, 60),
    ('Пшеничная крупа', 350, 12, 1, 75),
    ('Пшеничная мука', 350, 12, 1, 75),
    ('Пшеничная мука цельнозерновая', 350, 12, 1, 75),
    ('сахар', 400, 0, 0, 100),
    # Овощи
    ('Картофель', 77, 2, 0, 17),
    ('Картофель жареный', 150, 2, 10, 17),
    ('Картофель отварной', 77, 2, 0, 17),
    ('Картофель запеченный', 132, 2, 8, 17),
    ('Морковь', 41, 1, 0, 10),
    ('Морковь отварная', 41, 1, 0, 10),
    ('Морковь запеченная', 77, 1, 5, 10),
    ('Помидоры', 18, 1, 0, 4),
    ('Огурцы', 15, 1, 0, 3),
    ('Редис', 15, 1, 0, 3),
    ('Перец чили', 18, 1, 0, 4),
    ('Артишоки', 15, 1, 0, 3),
    ('Баклажаны', 25, 1, 0, 5),
    ('Эдамаме', 100, 10, 5, 10),
    ('Руккола', 15, 1, 0, 3),
    ('Сельдерей', 15, 1, 0, 3),
    ('Тыква', 26, 1, 0, 6),
    ('Брюссельская капуста', 25, 2, 0, 5),
    ('Оливки', 115, 1, 10, 3),
    ('Цукини', 15, 1, 0, 3),
    ('Капуста белокочанная', 25, 1, 0, 5),
    ('Спаржа', 20, 2, 0, 4),
    ('Цветная капуста', 34, 3, 0, 6),
    ('Салат айсберг', 15, 1, 0, 3),
    ('Лук красный', 40, 1, 0, 9),
    ('Горох зеленый', 100, 20, 0, 0),
    ('Салат латук', 15, 1, 0, 3),
    ('Перец болгарский', 15, 1, 0, 3),
    ('Грибы', 20, 3, 0, 2),
    ('Грибы вареные', 20, 3, 0, 2),
    ('Грибы запеченые', 40, 3, 2, 2),
    ('Фасоль', 80, 4, 0, 15),
    ('Свекла', 41, 1, 0, 10),
    ('Батат', 77, 2, 0, 17),
    ('Салат ромэн', 15, 1, 0, 3),
    ('Кукуруза', 86, 3, 1, 18),
    ('Шпинат', 23, 3, 0, 3),
    ('Авокадо', 160, 2, 15, 8),
    ('Брокколи', 34, 3, 0, 6),
    ('Лук зеленый', 15, 1, 0, 3),
    ('Лук репчатый', 40, 1, 0, 9),
    ('Чеснок', 149, 6, 0, 33),
    # фрукты
    ('Абрикос', 39, 1, 0, 9),
    ('Айва', 42, 0, 0, 11),
    ('Банан', 89, 1, 0, 23),
    ('Виноград', 68, 0, 0, 18),
    ('Гранат', 68, 0, 0, 18),
    ('Груша', 52, 0, 0, 13),
    ('Дыня', 30, 0, 0, 8),
    ('Ежевика', 43, 1, 0, 10),
    ('Киви', 61, 1, 0, 15),
    ('Клубника', 32, 0, 0, 8),
    ('Крыжовник', 43, 0, 0, 11),
    ('Лимон', 29, 1, 0, 7),
    ('Личи', 47, 0, 0, 12),
    ('Малина', 32, 0, 0, 8),
    ('Мандарин', 47, 0, 0, 12),
    ('Манго', 60, 0, 0, 15),
    ('Нектарин', 39, 1, 0, 9),
    ('Персик', 39, 1, 0, 9),
    ('Слива', 39, 1, 0, 9),
    ('Смородина черная', 43, 0, 0, 11),
    ('Смородина красная', 43, 0, 0, 11),
    ('Смородина белая', 43, 0, 0, 11),
    ('Яблоко', 52, 0, 0, 13),
    ('Арбуз', 30, 0, 0, 8),
    ('Апельсин', 47, 0, 0, 12),
    ('Ананас', 50, 0, 0, 13),
    # Орехи
    ('Арахис', 567, 25, 49, 13),
    ('Грецкие орехи', 654, 15, 65, 7),
    ('Кедровые орехи', 654, 15, 65, 7),
    ('Кешью', 654, 15, 65, 7),
    ('Кокосовое молоко', 567, 25, 49, 13),
    ('Кунжут', 567, 25, 49, 13),
    ('Лесной орех', 654, 15, 65, 7),
    ('Миндаль', 654, 15, 65, 7),
    #Напитки
    ('Вода', 0, 0, 0, 0),
    ('Кофе', 2, 0, 0, 0),
    ('Чай', 2, 0, 0, 0),
    ('Квас', 30, 0, 0, 8),
    ('Компот', 30, 0, 0, 8),
    ('Сок', 30, 0, 0, 8),
    ('Сок из свежих фруктов', 30, 0, 0, 8);


INSERT INTO Exercises (Exercise_name, Number_of_approaches, Number_of_repetitions)
VALUES
    # Грудные мышцы
    ('Жим лежа широким хватом, штанги на горизонтальной скамье', 5, 12),
    ('Жим лежа  гантелей на наклонной скамье', 5, 13),
    ('Разводка гантелей на горизонтальной скамье', 3, 15),
    ('Пуловер', 3, 15),
    ('Отжимания на брусьях', 4, 12),
    #Трицепс
    ('Жим лежа узким хватом на горизонтальной скамье', 5, 12),
    ('Французский жим', 4, 13),
    ('Разгибание на трицпс с верхнего блока', 3, 15),
    # Бицепс
    ('Сгибание рук на нижнем блоке', 5, 12),
    ('Сгибание рук с гантелями на скамье', 5, 13),
    ('Сгибание рук на наклонной скамье с гантелями  ', 3, 15),
    ('Поднятие штанги на бицепс обратным хватом', 4, 15),
    ('Поднятие z-грифа на бицепс ', 4, 13),
    # Спина
    ('Гиперэкстензия', 4, 15),
    ('Становая тяга', 5, 12),
    ('Мертвая тяга', 5, 12),
    ('Тяга штанги к подбородку', 5, 13),
    ('Подтягивания широким хватом', 4, 15),
    ('Подтягивания узким хватом', 4, 15),
    ('Тяга горизонтального блока', 4, 15),
    ('Шраги с гантелями', 4, 15),
    ('Тяга гантели к поясу', 4, 15),
    ('Скручивания на пресс', 4, 15),
    # Ноги
    ('Приседания со штангой на плечах', 5, 12),
    ('Приседания со штангой на груди', 5, 12),
    ('Выпады с гантелями', 4, 15),
    ('Жим ногами', 5, 15),
    ('Разгибания на бицепс бедра в тренажёре', 4, 12),
    ('Сгибания на заднюю поверхность бедра в тренажере', 4, 15),
    # Плечи
    ('Армейский жим', 5, 13),
    ('Махи гантелями', 4, 12),
    ('Жим сидя гантелей', 4, 15);



INSERT INTO Methods (Method_name)
VALUES ('Split'),
       ('FullBody');

INSERT INTO Days (Day_count)
VALUES (2),
       (3);
INSERT INTO Places (Place_name)
VALUES ('Дом'),
       ('Тренажёрный зал');
INSERT INTO Programs(Program_name, Method_id, Place_id, Day_id)
VALUES ('Программа 3', 1, 2, 2);

INSERT
Exercises_Programs (Exercise_id, Program_id)
VALUES (2, 3),
       (29, 3),
       (6, 3),
       (17, 3),
       (3, 3),
       (11, 3),
       (19, 3),
       (9, 3),
       (30, 3),
       (23, 3),
       (31, 3),
       (27, 3),
       (28, 3);
INSERT INTO Diets (Diet_name, Diet_calories, Diet_proteins, Diet_fats, Diet_carbohydrates)
VALUES ('Похудение', 0, 0, 0, 0),
       ('Набор мышечной массы', 0, 0, 0, 0),
       ('Поддержание формы', 0, 0, 0, 0);


INSERT INTO Products_Diets
VALUES (1, 1),
       (2, 1),
       (3, 1),
       (4, 1),
       (5, 1),
       (6, 1),
       (7, 1),
       (8, 1),
       (9, 1),
       (10, 1),
       (11, 1),
       (12, 1),
       (13, 1),
       (14, 1),
       (15, 1);
INSERT INTO Products_Diets
VALUES (16, 2),
       (17, 2),
       (18, 2),
       (19, 2),
       (20, 2),
       (21, 2),
       (22, 2),
       (23, 2),
       (24, 2),
       (25, 2),
       (26, 2),
       (27, 2),
       (28, 2),
       (29, 2),
       (30, 2),
       (31, 2);

INSERT INTO Products_Diets (Product_id, Diet_id)
VALUES (32, 3),
       (33, 3),
       (34, 3),
       (35, 3),
       (36, 3),
       (37, 3),
       (38, 3),
       (39, 3),
       (40, 3),
       (41, 3),
       (42, 3),
       (43, 3),
       (44, 3),
       (45, 3),
       (46, 3),
       (47, 3),
       (48, 3),
       (49, 3),
       (50, 3),
       (51, 3),
       (52, 3),
       (53, 3),
       (54, 3),
       (55, 3),
       (56, 3),
       (57, 3),
       (58, 3),
       (59, 3),
       (60, 3),
       (61, 3),
       (62, 3),
       (63, 3),
       (64, 3),
       (65, 3),
       (66, 3),
       (67, 3);


INSERT INTO Users (Program_id, Diet_id, User_name, User_surname, Password_hash, Email, Brith_date, Gender, Height,
                   Weight, Physical_activity_id, Metabolism) VALUE (3, 1, 'Иван', 'Иванов', '123', '1@mail.ru',
                                                                    '1999-01-01', 'М', 180, 80, 1, 2000);
INSERT INTO Users (Program_id, Diet_id, User_name, User_surname, Password_hash, Email, Brith_date, Gender, Height,
                   Weight, Physical_activity_id, Metabolism)
VALUES (3, 2, 'Петр', 'Петров', '123', '2@mail.ru', '1999-01-01', 'М', 180, 90, 2, 2500);
INSERT INTO Users (Program_id, Diet_id, User_name, User_surname, Password_hash, Email, Brith_date, Gender, Height,
                   Weight, Physical_activity_id, Metabolism)
VALUES (1, 3, 'Сидор', 'Сидоров', '123', '3@mail.ru', '1999-01-01', 'М', 180, 100, 3, 3000),
       (1, 2, 'Светлана', 'Андреева', '123', '4@mail.ru', '2000-01-01', 'Ж', 170, 60, 1, 2000);

INSERT INTO Users (User_name, User_surname, Password_hash, Email, Brith_date, Gender, Height,
                   Weight, Physical_activity_id, Metabolism)
VALUES ('Петр', 'Петров', '123', '12@mail.ru', '1999-01-01', 'М', 180, 90, 2, 2500);

INSERT INTO healthy_people.Physical_activities(Physical_activity_name, Coefficient)
VALUES ('Основной обмен веществ', 1),
       ('Низкая активность', 1.2),
       ('1-3 Тренировки в неделю', 1.375),
       ('5 Тренировок в неделю', 1.55),
       ('Ежедневные тренировки', 1.6375);
INSERT INTO Users (Program_id, Diet_id, User_name, User_surname, Password_hash, Email, Brith_date, Gender, Height,
                   Weight, Physical_activity_id, Metabolism)
VALUES (1, 1, 'Андрей', 'Андреев', '1223', '5@mail.ru', '1999-01-01', 'М', 180, 80, 1, 2000),
       (2, 2, 'Александр', 'Александров', '1223', '6@mail.ru', '1999-01-01', 'М', 180, 90, 2, 2500),
       (2, 3, 'Алексей', 'Алексеев', '1223', '7@mail.ru', '1999-01-01', 'М', 180, 100, 3, 3000),
       (2, 1, 'Анна', 'Андреева', '1223', '8@mail.ru', '2000-10-20', 'Ж', 170, 60, 1, 2000),
       (2, 2, 'Антон', 'Андреев', '1223', '9@mail.ru', '1999-01-01', 'М', 180, 80, 1, 2000),
       (2, 3, 'Александр', 'Александров', '1223', '10@mail.ru', '1999-01-01', 'М', 180, 90, 2, 2500);



INSERT INTO Products_Diets (Product_id, Diet_id)
VALUES (142, 1);
INSERT INTO Users ()
