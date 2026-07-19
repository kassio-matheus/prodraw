# ProDraw

A free-drawing desktop application built with Python and Tkinter, inspired by
[tldraw](https://tldraw.com), MS Paint, and Google Drawings.

ProDraw was built as the term project for the *Programação A* course at
**Universidade Federal de Sergipe (UFS)**. It doubles as a practical exercise
in applying **Object-Oriented Programming**, the **SOLID** principles, and
the **MVC (Model-View-Controller)** architectural pattern to a real,
interactive desktop UI — so the codebase is intentionally structured to be
read, extended, and learned from, not just run.

> New to the codebase? Read this file first, then move on to
> [`ARCHITECTURE.md`](./ARCHITECTURE.md) for a deep dive into how the layers
> fit together and a step-by-step guide to adding a new drawing tool.

## Features

- **Shape tools** — Rectangle, Square, Circle, Oval, Line, and Freehand draw.
- **Selection tool (cursor)** — click to select, drag a marquee to
  multi-select, drag to move, `Ctrl+C` / `Ctrl+V` to duplicate,
  `Delete` / `Backspace` to remove.
- **Action panel** — delete, duplicate, raise/lower layer, and clear the
  whole canvas.
- **Color palette** — 12 preset colors, each with a matching low-contrast
  fill so shapes stay legible against the dark canvas.
- **Tool options panel** — three fill styles (solid + border, solid only,
  outline only) and two border styles (solid, dotted).
- **Infinite dotted grid** that redraws on window resize, plus
  scroll-to-zoom centered on the cursor.
- **Save / Load workspace** to a custom `.prodraw` file (serialized with
  `pickle`) via the *Arquivo* menu.
- **Fullscreen window** by default — `F11` toggles fullscreen, `Esc` exits it.

## Tech stack

- **Python 3.10+** (developed and tested with Python 3.12–3.14)
- **Tkinter** — Python's standard GUI toolkit (bundled with CPython)
- **Zero third-party dependencies.** Everything is built on the standard
  library (`tkinter`, `dataclasses`, `abc`, `pickle`, `typing`), which keeps
  onboarding to "clone and run."

## Getting started

```bash
git clone https://github.com/kassio-matheus/prodraw.git
cd prodraw
python src/__main__.py
```

Run the command from the **repository root**, not from inside `src/`. That
matters for two reasons:

1. Python adds the script's own directory (`src/`) to `sys.path`, which is
   what makes `from prodraw.controllers import ...` resolve inside
   `__main__.py` — running it from elsewhere breaks those imports.
2. `LogoImageController` loads `public/icons/logo.png` using a path that's
   relative to the current working directory, so the process must be
   launched from the folder that contains `public/`.

No virtual environment or `pip install` is required — the project has no
external dependencies. If a future contribution adds one (e.g. Pillow for
richer image handling), please add a `requirements.txt` alongside it.

## Project structure

```
prodraw/
├── public/
│   └── icons/                  # PNG icons used by the toolbar & action panel
├── src/
│   ├── __main__.py              # Entry point — creates the window & workspace
│   └── prodraw/
│       ├── config/               # App-wide constants (color palette, bg color)
│       ├── models/                # Data + validation only, no Tkinter widgets
│       │   ├── shapes/             # Shape (ABC) + Rectangle, Circle, Oval, ...
│       │   ├── window/             # Window, Version, menubar models
│       │   └── workspace/          # Toolbar, color picker, tool options, ...
│       ├── views/                 # Tkinter rendering only, no business logic
│       │   ├── shapes/             # One *_view.py per shape, mirrors models/shapes
│       │   ├── window/             # Window & menubar views
│       │   └── workspace/          # Toolbar, panels, grid, zoom, logo views
│       ├── controllers/           # Wires Tkinter events to models & views
│       │   ├── shapes/             # Tools (ABC) + one controller per shape
│       │   ├── window/             # WindowController, create_window()
│       │   └── workspace/          # Cursor, color picker, actions panel, ...
│       └── workspace.py            # Composition root — wires every controller together
├── LICENSE
└── README.md
```

Every shape and every self-contained UI panel follows the same three-file
pattern: a **model** (`models/...`), a **view** (`views/...`), and a
**controller** (`controllers/...`) that connects them. Once you understand
one shape (e.g. `Rectangle`), you understand the shape of the whole codebase —
see [`ARCHITECTURE.md`](./ARCHITECTURE.md) for the details.

## Keyboard shortcuts

| Shortcut         | Action                          |
|-------------------|----------------------------------|
| `F11`             | Toggle fullscreen                |
| `Esc`             | Exit fullscreen                  |
| `Delete` / `Backspace` | Delete the selected shape(s) |
| `Ctrl+C` / `Ctrl+V`    | Copy / paste the selected shape(s) |
| Mouse wheel       | Zoom in/out, centered on the cursor |

## Known limitations & good first issues

Being upfront about the current state of the code will save new contributors
time:

- **Undo/Redo are not implemented yet.** The action panel buttons exist and
  are wired up, but `ActionsPanelController._trigger_undo` /
  `_trigger_redo` currently just `print()` a placeholder message. This is a
  great first contribution — see the "Command history" note in
  [`ARCHITECTURE.md`](./ARCHITECTURE.md#known-limitations--suggested-next-steps).
- **No automated tests.** There's no `pytest`/`unittest` suite yet, which
  makes refactors risky. Adding tests around the `Shape` subclasses (pure
  logic, no Tkinter involved) would be a good, low-risk starting point.
- **No linting/formatting config.** Consider adding `ruff` or `black` plus a
  CI workflow before the codebase grows further.

## Contributing

1. Fork the repository and create a feature branch.
2. Keep the MVC boundaries intact: views never contain business logic,
   models never import `tkinter`, and controllers are the only layer allowed
   to touch both.
3. Follow the existing shape/tool pattern when adding new functionality —
   see the step-by-step guide in
   [`ARCHITECTURE.md`](./ARCHITECTURE.md#adding-a-new-shape-tool).
4. Open a pull request describing what changed and why.

## License

Distributed under the MIT License — see [`LICENSE`](./LICENSE) for details.

## Authors

Built by Italo, Kássio, and Hendric, Computer Science students at
Universidade Federal de Sergipe (UFS), São Cristóvão campus.
