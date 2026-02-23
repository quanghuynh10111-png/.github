# Python Unified System

Kho mẫu để **hợp nhất mã nguồn Python thành một hệ thống thống nhất** và hỗ trợ đồng bộ hóa các nền tảng: **GitHub, ChatGPT, OpenAI, Codex, MDN Plus**.

## Ý tưởng

- Tất cả module nội bộ đăng ký qua `ModuleRegistry`.
- Mọi lời gọi chạy qua `UnifiedSystem` để thống nhất điểm điều phối.
- Danh sách provider (GitHub/ChatGPT/OpenAI/Codex/MDN Plus) quản lý tập trung.
- Có API `sync_provider` và `sync_all` để đồng bộ hóa theo từng provider hoặc toàn bộ.

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
python -m unified_system.cli sync all --payload nightly
python -m unified_system.cli sync github --payload repos
python -m unified_system.cli run sum 1 2 3
```

## Kiểm thử

```bash
python -m pytest
```
