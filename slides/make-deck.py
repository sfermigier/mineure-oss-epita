#!/usr/bin/env python

from glob import glob
from textwrap import dedent

SESSION = 4
SOURCES = [
    "zack-legal",
    "zack-licenses",
    "riehle-ip",
    "fp",
]

# -------------------------------

HEADER = f"""\
autoscale: true
slidenumbers: true
build-lists: true
slide-transition: true

# Mineure OSS @ EPITA
## Session {SESSION}

---

# Dernières sessions

- Unix et sa "philosophie"
- Emergence du libre et de Linux
- Définitions du logiciel libre et de l'open source

"""

output = open(f"session-{SESSION}.md", "w")

output.write(HEADER)


for src in SOURCES:
    for slide in sorted(glob(f"orig/{src}/*.png")):
        output.write(dedent(f"""
            ---

            ![fit]({slide})
            """))
