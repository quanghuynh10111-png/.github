# Python Unified System

Kho mẫu để **hợp nhất mã nguồn Python thành một hệ thống thống nhất** và đồng bộ hóa nhiều nền tảng: **GitHub, ChatGPT, OpenAI, Codex, MDN Plus**.

## Điểm chính

- `ModuleRegistry`: đăng ký và điều phối module nội bộ.
- `UnifiedSystem`: facade duy nhất để chạy module + đồng bộ provider.
- `Provider` + `SyncRecord`: mô hình dữ liệu rõ ràng cho các tích hợp.
- `DEFAULT_PROVIDERS`: danh sách provider mặc định ổn định để đồng bộ hóa nhất quán.

## Provider mặc định

`build_default_system()` tự động cấu hình:

- `github` → https://docs.github.com
- `chatgpt` → https://chatgpt.com
- `openai` → https://platform.openai.com/docs
- `codex` → https://developers.openai.com/codex
- `mdn-plus` → https://developer.mozilla.org/plus

## CLI

```bash
python -m unified_system.cli providers
python -m unified_system.cli providers --compact
python -m unified_system.cli sync all --payload nightly
python -m unified_system.cli sync github --payload repos --output json
python -m unified_system.cli run sum 1 2 3
```

## Kiểm thử

```bash
python -m pytest
```
