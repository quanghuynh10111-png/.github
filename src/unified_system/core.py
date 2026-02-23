"""Core abstractions for unifying Python source code into one system."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Callable

ProviderSyncHandler = Callable[[str], str]


@dataclass
class ModuleRegistry:
    """Registry that stores logical modules and their handlers."""

    handlers: dict[str, Callable[..., object]] = field(default_factory=dict)

    def register(self, name: str, handler: Callable[..., object]) -> None:
        if not name.strip():
            raise ValueError("Module name must not be empty.")
        self.handlers[name] = handler

    def dispatch(self, name: str, *args: object, **kwargs: object) -> object:
        if name not in self.handlers:
            available = ", ".join(sorted(self.handlers)) or "<none>"
            raise KeyError(f"Module '{name}' is not registered. Available: {available}")
        return self.handlers[name](*args, **kwargs)


@dataclass(frozen=True)
class Provider:
    """Represents an external platform that can be synchronized."""

    key: str
    display_name: str
    doc_url: str

    def __post_init__(self) -> None:
        if not self.key.strip():
            raise ValueError("Provider key must not be empty.")
        if not self.display_name.strip():
            raise ValueError("Provider display_name must not be empty.")
        if not self.doc_url.startswith("https://"):
            raise ValueError("Provider doc_url must be an https URL.")


@dataclass(frozen=True)
class SyncRecord:
    """State of a synchronization action for one provider."""

    provider_key: str
    provider_name: str
    provider_url: str
    payload: str
    status: str
    message: str
    timestamp_utc: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


DEFAULT_PROVIDERS: tuple[Provider, ...] = (
    Provider("chatgpt", "ChatGPT", "https://chatgpt.com"),
    Provider("codex", "Codex", "https://developers.openai.com/codex"),
    Provider("github", "GitHub", "https://docs.github.com"),
    Provider("mdn-plus", "MDN Plus", "https://developer.mozilla.org/plus"),
    Provider("openai", "OpenAI", "https://platform.openai.com/docs"),
)


class UnifiedSystem:
    """Facade that unifies all module calls and provider synchronization."""

    def __init__(self, registry: ModuleRegistry | None = None) -> None:
        self.registry = registry or ModuleRegistry()
        self.providers: dict[str, Provider] = {}
        self.sync_handlers: dict[str, ProviderSyncHandler] = {}

    def add_module(self, name: str, handler: Callable[..., object]) -> None:
        self.registry.register(name, handler)

    def run(self, module_name: str, *args: object, **kwargs: object) -> object:
        return self.registry.dispatch(module_name, *args, **kwargs)

    def register_provider(
        self,
        provider: Provider,
        sync_handler: ProviderSyncHandler | None = None,
    ) -> None:
        """Registers an external provider and an optional sync strategy."""

        self.providers[provider.key] = provider
        self.sync_handlers[provider.key] = sync_handler or self._default_sync_handler

    def list_providers(self) -> list[Provider]:
        """Returns providers sorted by key for deterministic output."""

        return [self.providers[key] for key in sorted(self.providers)]

    def sync_provider(self, provider_key: str, payload: str = "default") -> SyncRecord:
        """Synchronizes a provider and returns a machine-readable record."""

        if provider_key not in self.providers:
            available = ", ".join(sorted(self.providers)) or "<none>"
            raise KeyError(
                f"Provider '{provider_key}' is not registered. Available: {available}"
            )

        provider = self.providers[provider_key]
        result = self.sync_handlers[provider_key](payload)
        return SyncRecord(
            provider_key=provider.key,
            provider_name=provider.display_name,
            provider_url=provider.doc_url,
            payload=payload,
            status="synced",
            message=result,
            timestamp_utc=datetime.now(timezone.utc).isoformat(),
        )

    def sync_all(self, payload: str = "default") -> list[SyncRecord]:
        """Synchronizes all registered providers in sorted order."""

        return [self.sync_provider(provider.key, payload) for provider in self.list_providers()]

    @staticmethod
    def _default_sync_handler(payload: str) -> str:
        return f"Synchronized with payload='{payload}'"


def build_default_system() -> UnifiedSystem:
    """Builds a system preconfigured with common AI/dev knowledge providers."""

    system = UnifiedSystem()

    for provider in DEFAULT_PROVIDERS:
        system.register_provider(provider)

    system.add_module("echo", lambda text: text)
    system.add_module("sum", lambda *values: sum(float(v) for v in values))
    return system
