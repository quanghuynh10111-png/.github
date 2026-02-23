"""Simple CLI to demonstrate a unified Python system."""

from __future__ import annotations

import argparse

from .core import UnifiedSystem


def build_system() -> UnifiedSystem:
    system = UnifiedSystem()
    system.add_module("echo", lambda text: text)
    system.add_module("sum", lambda *values: sum(float(v) for v in values))
    return system


def main() -> None:
    parser = argparse.ArgumentParser(description="Unified Python Source System")
    parser.add_argument("module", help="Registered module name (echo|sum)")
    parser.add_argument("args", nargs="*", help="Arguments for the module")
    parsed = parser.parse_args()

    system = build_system()
    result = system.run(parsed.module, *parsed.args)
    print(result)


if __name__ == "__main__":
    main()
