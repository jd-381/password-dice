import logging
from typing import Annotated, Dict

import pyperclip
import typer

from password_dice.data import load_word_list
from password_dice.models import Passphrase, Separator
from password_dice.services import Dice

logging.basicConfig(level=logging.INFO, format="%(message)s")

app = typer.Typer(add_completion=False)
logger = logging.getLogger(__name__)


@app.command()
def main(
    words_option: Annotated[int, typer.Option("--words", "-w", min=1, max=24, help="Number of words")] = 6,
    separator_option: Annotated[
        str,
        typer.Option(
            "--separator",
            "-s",
            help="Character to separate words. One of: hyphen, underscore, space",
        ),
    ] = "hyphen",
    numbers_option: Annotated[bool, typer.Option("--numbers/--no-numbers", help="Include numbers")] = True,
    capitalize_option: Annotated[bool, typer.Option("--capitalize/--no-capitalize", help="Capitalize words")] = True,
    dice_option: Annotated[bool, typer.Option("--dice/--no-dice", help="Print your dice rolls")] = False,
):
    if dice_option:
        logging.getLogger().setLevel(logging.DEBUG)

    separator: Separator = _validate_separator_option(separator_option)
    word_list: Dict[str, str] = _load_word_list()
    words: list[str] = _generate_words(word_list, words_option)
    numbers: list[int] = []
    if numbers_option:
        numbers = _generate_numbers(words_option)
    passphrase: Passphrase = _build_passphrase(
        capitalize_option,
        numbers_option,
        words_option,
        numbers,
        separator,
        words,
    )
    _copy_passphrase_to_clipboard(passphrase)


def _validate_separator_option(separator_option: str) -> Separator:
    try:
        separator: Separator = Separator[separator_option.upper()]
        return separator
    except KeyError:
        logger.error(f'"--separator/-s {separator_option}" is invalid. Must be one of: hyphen, underscore, space')
        raise typer.Exit(1)
    except Exception as e:
        logger.error(e)
        raise typer.Exit(1)


def _load_word_list() -> Dict[str, str]:
    try:
        return load_word_list()
    except Exception as e:
        logger.error(e)
        raise typer.Exit(code=1)


def _generate_words(word_list: Dict[str, str], total_words: int) -> list[str]:
    logger.debug("Rolling for memorable words...")
    try:
        dice: Dice = Dice(number_of_dice=5)
        memorable_words: list[str] = []
        words: int = 1
        while words <= total_words:
            results: list[str] = [str(num) for num in dice.roll_d6()]
            id: str = "".join(results)
            memorable_word: str = word_list[id]
            memorable_words.append(memorable_word)
            logger.debug(f"Your memorable word: {memorable_word}")
            words += 1
        return memorable_words
    except Exception as e:
        logger.error(e)
        raise typer.Exit(code=1)


def _generate_numbers(total_words: int) -> list[int]:
    logger.debug("Rolling for damage...")
    try:
        dice: Dice = Dice(number_of_dice=1)
        numbers: list[int] = []
        words: int = 1
        while words <= total_words:
            result: int = dice.roll_d100()[0]
            numbers.append(result)
            words += 1
        return numbers
    except Exception as e:
        logger.error(e)
        raise typer.Exit(code=1)


def _build_passphrase(
    capitalize_option: bool,
    numbers_option: bool,
    words_option: int,
    numbers: list[int],
    separator: Separator,
    words: list[str],
) -> Passphrase:
    try:
        return Passphrase(
            capitalize_option,
            numbers_option,
            words_option,
            numbers,
            separator,
            words,
        )
    except Exception as e:
        logger.error(e)
        raise typer.Exit(1)


def _copy_passphrase_to_clipboard(passphrase: Passphrase) -> None:
    try:
        passphrase_str: str = passphrase.make()
        pyperclip.copy(passphrase_str)
        logger.info("Nice rolls! Your new passphrase has been copied to your clipboard.")
    except Exception as e:
        logger.error(e)
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
