from os import listdir, path
from argparse import ArgumentParser
from subprocess import call

dir_path = path.join(path.dirname(path.realpath(__file__)), "commands")


def parse_comments(command: str) -> dict:
    with open(path.join(dir_path, f"{command}.sh"), "r") as f:
        lines = f.read().splitlines()
        comments = [
            l.replace("# ", "")
            for l in lines
            if l.startswith("#") and not l.startswith("#!")
        ]
        return {key: val.strip() for key, val in (line.split(":") for line in comments)}


def main():
    commands = [x.replace(".sh", "") for x in listdir(dir_path)]

    parser = ArgumentParser(
        prog="guzzy",
        description="Interactive CLI git client inside fzf.",
        allow_abbrev=False,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subcommands = {}
    for cmd in commands:
        p = parse_comments(cmd)
        subcommands[cmd] = subparsers.add_parser(cmd, help=p["help"])

    args = parser.parse_args()

    call(path.join(dir_path, f"{args.command}.sh"), shell=True)
