import itertools
import math
from dataclasses import dataclass
from typing import Iterator, Union

import settings


@dataclass
class FizzBuzzNumber:
    num: int
    replace: str


class FizzBuzz:
    def __init__(self, rules: dict):
        self.rules = self.__generate_rules(rules)

    def __generate_rules(self, rules: dict) -> list:
        """
        Внутренняя функция, необходима для генерации всех комбинаций замен.
        :param rules: Базовые правила игры
        :return: Дополненные правила игры
        """
        appended_rules = []
        for i in range(1, len(rules) + 1):
            for comb in itertools.combinations(rules, i):
                appended_rules.append(
                    FizzBuzzNumber(
                        num=math.prod(comb),
                        replace=''.join(rules[k] for k in comb)
                    )
                )
        appended_rules.reverse()
        return appended_rules

    def generator(
            self,
            *,
            min: int = 1,
            max: int = 15
    ) -> Iterator[Union[str, int]]:
        """
        Функция возвращает генератор, вывод которого зависит от self.rules
        :param min: Минимальное для итерации число
        :param max: Максимальное для итерации число
        :return:
        """
        for num in range(min, max + 1):
            for rule in self.rules:
                if num % rule.num == 0:
                    yield rule.replace
                    break
            else:
                yield num


fizzbuzz = FizzBuzz(settings.RULES)
