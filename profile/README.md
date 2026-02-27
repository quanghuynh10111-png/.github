## Hi there 👋

Welcome to my GitHub profile repository.

- 🚀 Building and learning in public
- 🧪 Exploring automation and tooling
- 🤝 Open to collaboration on useful projects

## Đồng bộ hoá kiến thức GitHub CLI (`gh`)

Mình duy trì một checklist ngắn để luôn dùng GitHub CLI nhất quán giữa các máy/dev environment:

1. **Xác thực tài khoản**
   - `gh auth login`
   - `gh auth status`
2. **Thiết lập Git protocol & editor mặc định**
   - `gh config set git_protocol ssh`
   - `gh config set editor "code --wait"`
3. **Luồng làm việc hằng ngày**
   - Clone repo: `gh repo clone owner/repo`
   - Tạo nhánh + commit + push
   - Tạo PR: `gh pr create --fill`
   - Theo dõi review/check: `gh pr status`
4. **Đồng bộ extension hữu ích**
   - Liệt kê extension: `gh extension list`
   - Cài extension: `gh extension install <owner/extension>`
5. **Cập nhật phiên bản CLI**
   - Kiểm tra: `gh --version`
   - Nâng cấp theo package manager (brew/apt/choco)

> Tip: Có thể lưu các bước trên thành script bootstrap để onboarding máy mới nhanh hơn.

<!--
**quanghuynh10111-png/.github** is a ✨ _special_ ✨ repository because its `profile/README.md` (this file) appears on your GitHub profile.
-->
