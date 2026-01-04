# morse-code

Play morse code from a string

## Usage

```
usage: morse-code [-h] [-o] [--time TIME] [--freq FREQ] message
```
`-o` or `--oddity` can be used to play the [Three Note Oddity](https://www.numbers-stations.com/german/g04-three-note-oddity/) identifier before the morse-code message.

`--time` is the length of a single time unit (.), in milliseconds

`--freq` is the frequency of a beep, in Hertz.

## Installation

Run `install.bat` *or* run `pip3 install -e .` from the root directory of the repository, to install as a CLI tool.