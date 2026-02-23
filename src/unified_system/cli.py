"""CLI for a unified system that can run modules and sync providers."""

from __future__ import annotations

import argparse

from .core import UnifiedSystem, build_default_system


def build_system() -> UnifiedSystem:
    return build_default_system()


def main() -> None:
    parser = argparse.ArgumentParser(description="Unified Python Source System")
    subcommands = parser.add_subparsers(dest="command", required=True)

    run_parser = subcommands.add_parser("run", help="Run a registered module")
    run_parser.add_argument("module", help="Registered module name (echo|sum)")
    run_parser.add_argument("args", nargs="*", help="Arguments for the module")

    list_parser = subcommands.add_parser("providers", help="List sync providers")
    list_parser.add_argument("--compact", action="store_true", help="Only print provider keys")

    sync_parser = subcommands.add_parser("sync", help="Sync one or all providers")
    sync_parser.add_argument("provider", help="Provider key or 'all'")
    sync_parser.add_argument("--payload", default="default", help="Sync payload")

    parsed = parser.parse_args()
    system = build_system()

    if parsed.command == "run":
        print(system.run(parsed.module, *parsed.args))
        return

    if parsed.command == "providers":
        for provider in system.list_providers():
            line = provider.key if parsed.compact else (
                f"{provider.key}\t{provider.display_name}\t{provider.doc_url}"
            )
            print(line)
        return

    if parsed.command == "sync":
        if parsed.provider == "all":
            for record in system.sync_all(payload=parsed.payload):
                print(f"{record.provider_key}: {record.message}")
            return

        record = system.sync_provider(parsed.provider, payload=parsed.payload)
        print(f"{record.provider_key}: {record.message}")


if __name__ == "__main__":
    main()
