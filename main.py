
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

SCRIPTS = {
    "B": ROOT / "model B" / "amlResNet18.py",
    "C": ROOT / "model C" / "svcRBF.py",
}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("model", choices=SCRIPTS.keys(), help="B or C")
    args, extra = p.parse_known_args()

    script = SCRIPTS[args.model]
    if not script.exists():
        raise SystemExit(f"Missing: {script}")

    raise SystemExit(subprocess.call([sys.executable, str(script), *extra]))

if __name__ == "__main__":
    main()
