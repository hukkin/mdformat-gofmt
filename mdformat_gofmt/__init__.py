import subprocess

__version__ = "0.0.2"  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT


def format_go(unformatted: str, _info_str: str) -> str:
    unformatted_bytes = unformatted.encode("utf-8")
    result = subprocess.run(
        ["gofmt"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        input=unformatted_bytes,
    )
    if result.returncode:
        raise Exception("Failed to format Go code")
    return result.stdout.decode("utf-8")
