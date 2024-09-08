# Backend Part

## Overview

```plaintext
backend
├── app
├── video_generator
└── voice_generator
```

## Installation

### Download the repository

```bash
git clone https://github.com/AlphaSphereDotAI/chatacter_backend.git
cd chatacter_backend
git submodule update --init --recursive
```

#### Container

- Docker

    ```bash
    docker compose up
    ```

- Podman

    ```bash
    podman compose up
    ```

#### Local

- Install the dependencies

    ```bash
    uv sync
    ```

- Run the server

    ```bash
    uv run fastapi dev
    ```
