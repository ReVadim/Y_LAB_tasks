## Homework 3

## Задача №1. Задача на декоратор с кешированием результата.    

Напишите функцию-декоратор, которая сохранит (закэширует) значение декорируемой функции multiplier (Чистая функция).    
Если декорируемая функция будет вызвана повторно с теми же параметрами — декоратор должен вернуть сохранённый результат, не выполняя функцию.    

## Задача №2. Задача на декоратор с параметрами.    

Надо написать декоратор для повторного выполнения декорируемой функции через некоторое время.    
Использует наивный экспоненциальный рост времени повтора __(factor)__ до граничного времени ожидания __(border_sleep_time).__

В качестве параметров декоратор будет получать:    

- call_count - число, описывающее кол-во раз запуска функций;
- start_sleep_time - начальное время повтора;
- factor - во сколько раз нужно увеличить время ожидания;
- border_sleep_time - граничное время ожидания.    

Формула:    
```
t = start_sleep_time * 2^(n) if t < border_sleep_time
t = border_sleep_time if t >= border_sleep_time
```

Ожидаемый результат:    
```
Кол-во запусков = call_count (допустим 3)
Начало работы
Запуск номер 1. Ожидание: t секунд. Результат декорируемой функций = func_result.
Запуск номер 2. Ожидание: t секунд. Результат декорируемой функций = func_result.
...
Конец работы
```

## Результат работы:    

![](https://github.com/ReVadim/Y_LAB_tasks/blob/main/printscreen/params_decorator.png)

<hr>    

## Задача №3. Рефакторинг кода.    

Сделать рефакторинг кода согласно принципам SOLID.    
[Ссылка на код](https://github.com/BernarBerdikul/ylab_hw/tree/main/not_solid_code)

Результат выполнения:    
![](https://github.com/ReVadim/Y_LAB_tasks/blob/main/printscreen/refactor_result.png)
<hr>    

## Homework 3. part 2    

## Задача 4. Циклический итератор.    

Написать класс __CyclicIterator__.    
Должен итерироваться по итерируемому объекту __(list, tuple, set, range, и т.д.)__    
По достижении последнего элемента должен начинать снаяала.    

Ожидаемый вывод программы:    
```
1 0
2 1
3 2
4 0
5 1
6 ...
```

## Задача 5. Разжатие массива.    

У каждого фильма есть расписание, по каким дням он идёт в кинотеатрах.    
Для эффективности дни проката хранятся периодами дат.    
Например, прокат фильма проходит с 1 по 7 января, а потом показ возобновляется с 15 января по 7 февраля:    

```
[
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7))
]
```

Дан class Movie. Реализуйте у него метод schedule.    
Он будет генерировать дни, в которые показывают фильм.    
```
from dataclasses import dataclass
from datetime import datetime
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        return []
```

Результат работы:    
![](https://github.com/ReVadim/Y_LAB_tasks/blob/main/printscreen/test_homework_3.png)
