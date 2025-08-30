import logging
import random

logger = logging.getLogger()


class Dice:
    def __init__(self, number_of_dice: int):
        if number_of_dice == 0:
            raise ValueError("Number of dice cannot be 0.")
        self._number_of_dice: int = number_of_dice

    def roll_d6(self) -> list[int]:
        logger.debug(f"Rolling {self._number_of_dice} D6...")
        die: int = 1
        int_result: list[int] = []
        while die <= self._number_of_dice:
            int_result.append(random.randint(1, 6))
            die += 1
        yahtzee_message: str = ""
        if self._number_of_dice == 5:
            yahtzee_message = " (YAHTZEE)" if len(set(int_result)) == 1 else ""
        str_result = [str(i) for i in int_result]
        logger.debug(f"You rolled: {', '.join(str_result)}{yahtzee_message}")
        return int_result

    def roll_d100(self) -> list[int]:
        logger.debug(f"Rolling {self._number_of_dice} D100...")
        die: int = 1
        int_result: list[int] = []
        while die <= self._number_of_dice:
            int_result.append(random.randint(1, 100))
            die += 1
        critical_messages = {1: " (CRITICAL FAILURE)", 100: " (CRITICAL SUCCESS)"}
        critical_message = ""
        if self._number_of_dice == 1:
            critical_message = critical_messages.get(int_result[0], "")
        str_result = [str(i) for i in int_result]
        logger.debug(f"You rolled: {', '.join(str_result)}{critical_message}")
        return int_result
