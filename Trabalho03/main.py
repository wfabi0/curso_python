from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print("Email:", message)


class SmsNotification(Notification):
    def send(self, message):
        print("SMS:", message)


class NotificationFactory:
    @staticmethod
    def create(tipo):
        if tipo == "email":
            return EmailNotification()
        if tipo == "sms":
            return SmsNotification()


class LogDecorator(Notification):
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        print("Log: enviando notificação")
        self.notification.send(message)


class User:
    def __init__(self, nome):
        self.nome = nome

    def update(self, message):
        print(self.nome, "recebeu:", message)


class NotificationService:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def notify(self, message):
        for user in self.users:
            user.update(message)


notificacao = NotificationFactory.create("email")
notificacao = LogDecorator(notificacao)

service = NotificationService()
service.add_user(User("Alice"))
service.add_user(User("Bob"))

notificacao.send("Sistema em manutenção")
service.notify("Sistema em manutenção")
