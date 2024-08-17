<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/built-to-scale/master/game/gui/window_icon.png" alt="Built to Scale">
</p>

# Built to Scale

![release](https://img.shields.io/github/v/release/remarkablegames/built-to-scale)
[![build](https://github.com/remarkablegames/built-to-scale/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/built-to-scale/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/built-to-scale/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/built-to-scale/actions/workflows/lint.yml)

📖 Write visual novels with Ren'Py Template.

Play the game on:

- [remarkablegames](https://remarkablegames.org/built-to-scale)

## Prerequisites

Download [Ren'Py SDK](https://www.renpy.org/latest.html):

```sh
git clone https://github.com/remarkablegames/renpy-sdk.git
```

Symlink `renpy`:

```sh
sudo ln -sf "$(realpath renpy-sdk/renpy.sh)" /usr/local/bin/renpy
```

## Install

Clone the repository to the `Projects Directory`:

```sh
git clone https://github.com/remarkablegames/built-to-scale.git
cd built-to-scale
```

Rename the project:

```sh
git grep -l 'Built to Scale' | xargs sed -i '' -e 's/Built to Scale/My Novel/g'
```

```sh
git grep -l 'Built to Scale' | xargs sed -i '' -e 's/built-to-scale/my-novel/g'
```

## Run

Launch the project:

```sh
renpy .
```

Or open the `Ren'Py Launcher`:

```sh
renpy
```

Press `Shift`+`R` to reload the game.

Clean the cache:

```sh
find game -name "*.rpyc" -delete
```

## Lint

Lint the game:

```sh
renpy game lint
```

## License

[MIT](LICENSE)
