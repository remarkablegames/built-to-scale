<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/built-to-scale/master/game/gui/window_icon.png" alt="Built to Scale">
</p>

# Built to Scale

![release](https://img.shields.io/github/v/release/remarkablegames/built-to-scale)
[![build](https://github.com/remarkablegames/built-to-scale/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/built-to-scale/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/built-to-scale/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/built-to-scale/actions/workflows/lint.yml)

⚖️ Play as an entrepreneur starting a business!

Play the game on:

- [remarkablegames](https://remarkablegames.org/built-to-scale)

## Credits

### Art

- [Uncle Mugen](https://lemmasoft.renai.us/forums/viewtopic.php?t=17302)
- [Mad Scientist](https://twitter.com/mad_scientist92)
- Photo by [Andrew Neel](https://unsplash.com/@andrewtneel) on [Unsplash](https://unsplash.com/photos/macbook-pro-white-ceramic-mugand-black-smartphone-on-table-cckf4TsHAuw)

### Audio

- Guilain de Coligny
- [Kenney Interface Sounds](https://kenney.nl/assets/interface-sounds)
- [Knock knock knock](https://pixabay.com/sound-effects/knock-knock-knock-40474/)

## Ideation

- [Excalidraw](https://excalidraw.com/#json=14bsj0P8n7aSDsj0kx8m0,nwOMIXvDpKPBRfKXID929w)
- [Game Design Document](https://docs.google.com/document/d/12TN1zvyXvw51Xc1GbXCnBtvcRR2qjR-Qh1HAVmfVAPE/edit)

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
