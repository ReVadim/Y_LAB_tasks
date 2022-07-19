import time
import datetime


def func_repeater(call_count, start_sleep_time, factor, border_sleep_time):
    """
    :param call_count: число, описывающее количество раз запуска функции
    :param start_sleep_time: начальное время повтора
    :param factor: во сколько раз нужно увеличить время ожидания
    :param border_sleep_time: граничное время ожидания
    :return:
    """
    def func(function):

        def wrapper(*args, **kwargs):
            t = start_sleep_time
            print(f'Кол-во запусков = {call_count}\nНачало работы')
            for step in range(1, call_count + 1):
                time.sleep(t)
                func_result = function(*args, **kwargs)
                print(f'Запуск номер {step}. Ожидание {t} секунд. Результат декорируемой функции = {func_result}')
                time_delta = start_sleep_time * (factor ** step)
                t = border_sleep_time if time_delta >= border_sleep_time else time_delta
            print('Конец работы')

        return wrapper
    return func


@func_repeater(call_count=6, start_sleep_time=1, factor=2, border_sleep_time=25)
def test_repeat_function():
    return datetime.datetime.now()


print(test_repeat_function())
