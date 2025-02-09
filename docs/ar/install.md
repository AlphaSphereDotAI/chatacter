# الجزء الخلفي

## ملخص

```plaintext
backend
├── app
├── video_generator
└── voice_generator
```

## تثبيت

### تنزيل المستودع

```bash
git clone https://github.com/AlphaSphereDotAI/chatacter_backend.git
cd chatacter_backend
git submodule update --init --recursive
```

#### حاوية

- عامل ميناء

```bash
docker compose up
```

- بودمان

```bash
podman compose up
```

#### محلي

- تثبيت التبعيات

```bash
uv sync
```

- تشغيل الخادم

```bash
uv run fastapi dev
```
