# Weather Email Automation

Tự động gửi email dự báo thời tiết Hà Nội mỗi ngày lúc 6h sáng và 12h trưa.

## Tech Stack
- **Python** — requests, smtplib
- **Open-Meteo API** — free weather API, no key required
- **GitHub Actions** — cloud scheduler, runs without local machine

## How it works
Open-Meteo API → Python script → Gmail SMTP → Inbox
↑
GitHub Actions (cron: 6AM & 12PM UTC+7)

## Setup
1. Clone repo
2. Add GitHub Secrets: `GMAIL_USER`, `GMAIL_PASSWORD`, `RECEIVER_EMAIL`
3. Enable GitHub Actions → Run workflow
