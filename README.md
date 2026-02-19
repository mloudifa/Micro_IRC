# IRC Server

A minimal TCP-based IRC-style server built with Python, focusing on a clean, event-driven architecture.

The server handles multiple clients concurrently using non-blocking sockets and an efficient I/O multiplexing loop.

---

## Features

- Non-blocking TCP server
- Event-driven architecture using `selectors`
- Concurrent client handling
- Structured server and client abstractions
- CLI-based configuration

---

## Usage

```bash
python main.py <PORT> <PASSWORD>
