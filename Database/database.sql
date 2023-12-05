CREATE DATABASE SmartLeave;
    USE SmartLeave;
        CREATE TABLE user_info (
            user_id INTEGER NOT NULL AUTO_INCREMENT,
            user_name VARCHAR(20) NOT NULL,
            user_total_al INTEGER NOT NULL,
            user_remaining_al INTEGER,
            PRIMARY KEY(user_id)
        );

        INSERT INTO user_info (user_name, user_total_al, user_remaining_al)
        VALUES
            ('Kate', 20, 20),
            ('Ayo', 28, 24),
            ('Mari', 30, 27),
            ('Neha', 32, 31),
            ('Teni', 35, 25);

        CREATE TABLE holidays (
            holiday_id INTEGER NOT NULL AUTO_INCREMENT,
            user_id INTEGER NOT NULL,
            start_date DATE,
            end_date DATE,
            holiday_length INTEGER,
            annual_leave_used INTEGER,
            PRIMARY KEY(holiday_id)
        );

        INSERT INTO holidays(user_id, start_date, end_date, holiday_length, annual_leave_used)
        VALUES
            (2, 2024-07-04, 2024-07-09, 6, 4),
            (3, 2024-01-25, 2024-01-29, 5, 3),
            (4, 2024-03-22, 2024-03-24, 3, 1),
            (5, 2024-09-07, 2024-09-15, 9, 5),
            (5, 2024-10-05, 2024-10-13, 9, 5);


