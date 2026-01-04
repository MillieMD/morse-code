# IMPORTS
import sys
import time
import winsound
import argparse

TIME_UNIT = 300
FREQ = 700

morse = { 
"A":".-",
"B":"-...",
"C":"-.-.",
"D":"-..",
"E":".",
"F":"..-.",
"G":"--.",
"H":"....",
"I":"..",
"J":".---",
"K":"-.-",
"L":".-..",
"M":"--",
"N":"-.",
"O":"---",
"P":".--.",
"Q":"--.-",
"R":".-.",
"S":"...",
"T":"-",
"U":"..-",
"V":"...-",
"W":".--",
"X":"-..-",
"Y":"-.--",
"Z":"--..",
"0":"-----",
"1":".----",
"2":"..---",
"3":"...--",
"4":"....-",
"5":".....",
"6":"-....",
"7":"--...",
"8":"---..",
"9":"----." }

# DICTIONARY STUFF
def init_dict(d, filename) -> dict:
    """Initialise a given dictionary from a .txt file.
    The file should use comma seperated key-value pairs, each on a new line.
    
    d -- dictionary to initialise
    filename -- string, filename to read data from
    """
    f = open(filename)
    content = f.read()

    for line in content.split("\n"):
        key, value = line.split(",")
        d[key.strip()] = value.strip()
    

def key_from_dict_value(d, value):
    return [key for key, item in d.items() if item == value]


# MORSE CODE STUFF
def play_from_string(string : str, freq : int, time_unit_ms : int):
    for c in string:
        if c == ".":
            winsound.Beep(freq, time_unit_ms)

        if c == "-":
            winsound.Beep(freq, time_unit_ms * 3)

def main():

    parser = argparse.ArgumentParser(
        prog="morse-code",
        description="Play morse code from a string",
    )

    parser.add_argument("message", help="the message to convert to morse code")
    parser.add_argument("-o", "--oddity", action="store_true", help="play the three note oddity identifier")
    parser.add_argument("--time", default=300, help="the length of a single time unit (.) in milliseconds. default is 300ms", type=int)
    parser.add_argument("--freq", default=700, help="beep sound frequency in hertz. default is 700hz", type=int)

    args = parser.parse_args()

    message = args.message.upper()
    frequency = args.freq
    time_unit_ms = args.time
    time_unit_s = time_unit_ms/1000

    if args.oddity:

        ID_REPEAT = 3

        for i in range(ID_REPEAT):
            winsound.Beep(512, 1000)
            winsound.Beep(739, 1000)
            winsound.Beep(899, 1000)
            time.sleep(1)

        time.sleep(0.5)

    for c in message:

        if c == " ":
            time.sleep(time_unit_s * 7)
            continue

        morse_string = morse[c]
        play_from_string(morse_string, frequency, time_unit_ms)
        time.sleep(time_unit_s * 3)

if __name__ == '__main__':
    main()