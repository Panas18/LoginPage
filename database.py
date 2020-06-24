import sqlite3

class table:
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()

    # if  not os.path.isfile("loginData.db"):
    c.execute('''create table login_data(
                full_name text,
                user_name text,
                password text
                )''')


    def insert_data(self, user):

        with self.conn:
            self.c.execute('insert into login_data values(:full_name, :user_name, :password)',
                           {"full_name": user.s_full_name.text, "user_name": user.s_user_name.text,
                            "password": user.s_password.text}
                           )


    def print_data(self):
        
        self.c.execute('select *from login_data')     
        print(self.c.fetchall())
