FROM mcr.microsoft.com/devcontainers/python:1-3.13-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends \
    make \
    git \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

USER vscode
