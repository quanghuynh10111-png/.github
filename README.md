# Python Unified System

Kho mẫu để **hợp nhất mã nguồn Python thành một hệ thống thống nhất**.

## Ý tưởng

- Tất cả module được đăng ký qua `ModuleRegistry`.
- Mọi lệnh chạy qua `UnifiedSystem` để tránh gọi trực tiếp, rời rạc.
- Có CLI mẫu (`unified_system.cli`) để chạy module theo tên.

## Chạy nhanh

```bash
python -m unified_system.cli echo "xin chao"
python -m unified_system.cli sum 1 2 3
```

## Kiểm thử

```bash
python -m pytest
```
