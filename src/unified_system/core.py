"""Core abstractions for unifying Python source code into one system."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable


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


class UnifiedSystem:
    """Facade that unifies all module calls behind a single API."""

    def __init__(self, registry: ModuleRegistry | None = None) -> None:
        self.registry = registry or ModuleRegistry()

    def add_module(self, name: str, handler: Callable[..., object]) -> None:
        self.registry.register(name, handler)

    def run(self, module_name: str, *args: object, **kwargs: object) -> object:
        return self.registry.dispatch(module_name, *args, **kwargs)
