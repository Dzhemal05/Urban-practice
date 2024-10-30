import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.age = age
        self.password = self.hash_password(password)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def __repr__(self):
        return f"User({self.nickname}, {self.age})"


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"Video({self.title}, {self.duration}s)"


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == self.hash_password(password):
                self.current_user = user
                print(f"Пользователь {nickname} успешно вошёл.")
                return
        print("Неверный логин или пароль.")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} успешно зарегистрирован и вошёл.")

    def log_out(self):
        print(f"Пользователь {self.current_user.nickname} вышел.")
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if all(video.title != v.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_term):
        search_term = search_term.lower()
        return [video.title for video in self.videos if search_term in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                for second in range(video.time_now + 1, video.duration + 1):
                    print(second, end=' ', flush=True)
                    time.sleep(1)
                print("\nКонец видео")
                video.time_now = 0
                return

        print("Видео не найдено")

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)


    ur.add(v1, v2)


    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))


    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')


    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)


    ur.watch_video('Лучший язык программирования 2024 года!')