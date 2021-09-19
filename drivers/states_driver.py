from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):

    @abstractmethod
    def return_state(self):
        pass


class Repose(State):

    def __doc__(self):
        """
        Авто не работает
        """

    def __init__(self, car):
        self.car = car

    def return_state(self):
        return f'Авто {self.car} не работает'


class CallWaiting(State):

    def __doc__(self):
        """
        Авто ожидает вызова
        """

    def __init__(self, car):
        self.car = car

    def return_state(self):
        return f'Авто {self.car} ожидает вызова'


class RidesOnCall(State):

    def __doc__(self):
        """
        Авто едет на вызов

        """

    def __init__(self, car):
        self.car = car

    def return_state(self):
        return f'Авто {self.car} едет на вызов'


class WaitingClient(State):

    def __doc__(self):
        """
        Авто ожидает клиента
        """

    def __init__(self, car):
        self.car = car

    def return_state(self):
        return f'Авто {self.car} ожидает клиента'


class Run(State):

    def __doc__(self):
        """
        Авто выполняет рейс
        """

    def __init__(self, car):
        self.car = car

    def return_state(self):
        return f'Авто {self.car} выполняет рейс'


if __name__ == '__main__':
    print(CallWaiting('5347').__doc__())
