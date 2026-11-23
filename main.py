"""Write one line to /output/entry.txt (stdlib only, deterministic)."""
import os

# The judged text: exactly one line, kept byte-identical — do not edit the wording.
LINE = "She still saves the burnt corner of the toast for herself, because the part nobody else wants is the part she loves most \u2014 and that is how I learned to love her."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
