from unified_system.core import ModuleRegistry, UnifiedSystem


def test_register_and_dispatch() -> None:
    registry = ModuleRegistry()
    registry.register("double", lambda value: value * 2)

    assert registry.dispatch("double", 5) == 10


def test_dispatch_missing_module() -> None:
    registry = ModuleRegistry()

    try:
        registry.dispatch("missing")
        raised = False
    except KeyError:
        raised = True

    assert raised


def test_unified_system_run() -> None:
    system = UnifiedSystem()
    system.add_module("concat", lambda left, right: f"{left}{right}")

    assert system.run("concat", "py", "thon") == "python"
