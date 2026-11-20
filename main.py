"""Entry script for the 20 November 2026 news-image bounty.

The artwork itself lives in entry.png next to this script; this program
does no drawing of its own. Its only job is to place an exact copy of
that picture where the grader looks for it -- entry.png inside the output
folder, which is /output in the grading container and whatever
MAKEFUN_OUTPUT_DIR names when the script is run by hand.

The run is fully repeatable: no network access, no clock, no randomness,
and nothing but the Python standard library, so identical input bytes
always yield identical output bytes. Once the copy lands, the script
weighs both files and aborts loudly if their sizes disagree, so a short
or truncated write can never slip through unnoticed."""

from os import environ
from pathlib import Path


IMAGE_NAME = "entry.png"
FALLBACK_FOLDER = "/output"
OUTPUT_VARIABLE = "MAKEFUN_OUTPUT_DIR"


def source_path():
    """Return the picture bundled with this repository."""
    return Path(__file__).resolve().parent.joinpath(IMAGE_NAME)


def destination_path():
    """Return where the graded copy belongs, creating the folder first."""
    folder = Path(environ.get(OUTPUT_VARIABLE, FALLBACK_FOLDER))
    folder.mkdir(parents=True, exist_ok=True)
    return folder.joinpath(IMAGE_NAME)


def place_copy(origin, target):
    """Write an exact copy of origin to target and report its size."""
    payload = origin.read_bytes()
    target.write_bytes(payload)
    original_size = origin.stat().st_size
    copied_size = target.stat().st_size
    if copied_size != original_size:
        raise SystemExit(
            "copy failed: source holds %d bytes but the copy holds %d"
            % (original_size, copied_size)
        )
    return copied_size


def run():
    picture = source_path()
    goal = destination_path()
    size = place_copy(picture, goal)
    print("entry.png delivered: %d bytes written to %s" % (size, goal))


if __name__ == "__main__": run()
