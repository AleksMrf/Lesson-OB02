class User:

    def __init__(self, user_id, name):
       self._user_id = user_id
       self._name = name
       self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

    def __str__(self):
        return f"User(ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level})"

class Admin(User):
    def __init__(self, user_id, name, admin_level):
        super().__init__(user_id, name)
        self._access_level = 'admin'  # Уровень доступа для администраторов
        self.admin_level = admin_level  # Дополнительный уровень доступа

    def add_user(self, user_list, user_id, name):
        new_user = User(user_id, name)
        user_list.append(new_user)
        print(f"Пользователь '{name}' добавлен.")

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь '{user.get_name()}' удален.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    def __str__(self):
        return (f"Admin(ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level}, "
                f" Admin Level: {self.admin_level})")

users = []

admin1 = Admin(1, "Анна", "супер")
admin2 = Admin(2, "Алексей", "модератор")

admin1.add_user(users, 3, "Виктор")
admin1.add_user(users, 4, "Мария")

print("\nТекущие пользователи:")
for user in users:
    print(user)

admin1.remove_user(users, 3)

print("\nПользователи после удаления:")
for user in users:
    print(user)

