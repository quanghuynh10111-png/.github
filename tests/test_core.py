import pytest

from unified_system.core import (
    DEFAULT_PROVIDERS,
    ModuleRegistry,
    Provider,
    UnifiedSystem,
    build_default_system,
)


def test_register_and_dispatch() -> None:
    registry = ModuleRegistry()
    registry.register("double", lambda value: value * 2)

    assert registry.dispatch("double", 5) == 10


def test_dispatch_missing_module() -> None:
    registry = ModuleRegistry()

    with pytest.raises(KeyError):
        registry.dispatch("missing")


def test_unified_system_run() -> None:
    system = UnifiedSystem()
    system.add_module("concat", lambda left, right: f"{left}{right}")

    assert system.run("concat", "py", "thon") == "python"


def test_sync_one_provider() -> None:
    system = UnifiedSystem()
    system.register_provider(Provider("github", "GitHub", "https://docs.github.com"))

    result = system.sync_provider("github", payload="repos")

    assert result.provider_key == "github"
    assert result.provider_name == "GitHub"
    assert result.provider_url == "https://docs.github.com"
    assert result.status == "synced"
    assert result.payload == "repos"
    assert "repos" in result.message


def test_default_system_has_expected_providers() -> None:
    system = build_default_system()

    keys = [provider.key for provider in system.list_providers()]

    assert keys == ["chatgpt", "codex", "github", "mdn-plus", "openai"]


def test_sync_all_returns_all_providers() -> None:
    system = build_default_system()

    records = system.sync_all(payload="nightly")

    assert len(records) == 5
    assert all(record.status == "synced" for record in records)


def test_default_providers_export_is_stable() -> None:
    assert [provider.key for provider in DEFAULT_PROVIDERS] == [
        "chatgpt",
        "codex",
        "github",
        "mdn-plus",
        "openai",
    ]


def test_provider_validation_requires_https_url() -> None:
    with pytest.raises(ValueError):
        Provider("docs", "Docs", "http://example.com")
