from dataclasses import dataclass
from enum import Enum


class Separator(Enum):
    HYPHEN = "-"
    UNDERSCORE = "_"
    SPACE = " "


@dataclass(frozen=True)
class Passphrase:
    capitalize: bool
    include_numbers: bool
    length: int
    numbers: list[int]
    separator: Separator
    words: list[str]

    def __post_init__(self):
        errors: list[str] = []
        if len(self.words) != self.length:
            errors.append(f"Invalid length for words. Expected {self.length}; Received {len(self.words)}")
        if self.include_numbers:
            if self.numbers:
                if len(self.numbers) != self.length:
                    errors.append(f"Invalid length for numbers. Expected {self.length}; Received {len(self.numbers)}")
        if errors:
            raise ValueError(". ".join(errors) + ".")

    def make(self) -> str:
        words: list[str] = [w.capitalize() for w in self.words] if self.capitalize else self.words
        if self.include_numbers:
            words = [f"{word}{num}" for word, num in zip(words, self.numbers)]
        return self.separator.value.join(words)
