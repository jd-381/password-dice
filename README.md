# Password Dice

Roll dice to generate secure and memorable passwords right to your clipboard.

## Features

- Generate strong, memorable passphrases
- Dice rolling technology (tracks Yahtzee's and critical rolls)
- Customize password length, capitalization, numbers, and special characters
- Passphrases are copied to your clipboard and never printed or logged

## Install

Install it locally then launch a new terminal session.

```sh
pipx install .
```

## Usage

```
 Usage: password_dice [OPTIONS]                                                                      
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --words               -w                     INTEGER RANGE [1<=x<=24]  Number of words [default: 6]                                                       │
│ --separator           -s                     TEXT                      Character to separate words. One of: hyphen, underscore, space [default: hyphen]   │
│ --numbers                 --no-numbers                                 Include numbers [default: numbers]                                                 │
│ --capitalize              --no-capitalize                              Capitalize words [default: capitalize]                                             │
│ --dice                    --no-dice                                    Print your dice rolls [default: no-dice]                                           │
│ --help                                                                 Show this message and exit.                                                        │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

Running `password_dice` with no options will create a passphrase like this:
```sh
$ password_dice
Nice rolls! Your new passphrase has been copied to your clipboard.
# Example in clipboard:
# Malformed35-Haggler58-Shining59-Shrapnel29-Outdoors14-Scrubber54
```

Passing `--dice` will print your rolls (but not your passphrase):
```sh
$ password_dice --dice
Rolling for memorable words...
Rolling 5 D6...
You rolled: 6, 6, 6, 6, 6 (YAHTZEE)
Your memorable word: zoom
Rolling 5 D6...
You rolled: 1, 2, 1, 5, 5
Your memorable word: anybody
Rolling 5 D6...
You rolled: 3, 5, 1, 5, 1
Your memorable word: jitters
Rolling 5 D6...
You rolled: 4, 4, 1, 2, 4
Your memorable word: paver
Rolling 5 D6...
You rolled: 4, 4, 1, 3, 3
Your memorable word: payable
Rolling 5 D6...
You rolled: 6, 2, 4, 1, 6
Your memorable word: traction
Rolling for damage...
Rolling 1 D100...
You rolled: 92
Rolling 1 D100...
You rolled: 1 (CRITICAL FAILURE)
Rolling 1 D100...
You rolled: 90
Rolling 1 D100...
You rolled: 29
Rolling 1 D100...
You rolled: 3
Rolling 1 D100...
You rolled: 100 (CRITICAL SUCCESS)
Nice rolls! Your new passphrase has been copied to your clipboard.
# Example in clipboard:
# Zoom92-Anybody1-Jitters90-Paver29-Payable3-Traction100
```

Create a 12 (or 24) word seed phrase:
```sh
$ password_dice --words 12 --separator space --no-capitalize --no-numbers
Nice rolls! Your new passphrase has been copied to your clipboard.
# Example in clipboard:
# overfed unhappy onstage barman reggae shifting unpaved contest spoilage modulator reversing number
```

## FAQ

### How are passwords generated?

Password Dice was created based on this blog post [EFF Dice-Generated Passphrases](https://www.eff.org/dice).

For each word in the passphrase, the app will roll 5 D6 and use the corresponding word from the [EFF Large Word List](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt). Additionally, for each word, the app will roll 1 D100 and append the result to the word.