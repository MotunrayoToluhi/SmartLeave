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
            ('Mari', 30, 27),
            ('Neha', 32, 31),
            ('Teni', 35, 25);

