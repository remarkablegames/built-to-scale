<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/built-to-scale/master/design/cover.jpg" width="450px" alt="Built to Scale">
</p>

# Built to Scale

![release](https://img.shields.io/github/v/release/remarkablegames/built-to-scale)
[![build](https://github.com/remarkablegames/built-to-scale/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/built-to-scale/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/built-to-scale/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/built-to-scale/actions/workflows/lint.yml)

⚖️ Play as an entrepreneur building a business to scale!

Play the game on:

- [remarkablegames](https://remarkablegames.org/built-to-scale)
- [itch.io](https://remarkablegames.itch.io/built-to-scale)
- [newgrounds](https://www.newgrounds.com/portal/view/945558)

This was made for the [GMTK Game Jam 2024](https://itch.io/jam/gmtk-2024), which the theme was `Built to Scale` (see [submission](https://itch.io/jam/gmtk-2024/rate/2910953)).

Read the [blog post](https://remarkablegames.org/posts/built-to-scale/).

## Credits

### Art

- [Uncle Mugen](https://lemmasoft.renai.us/forums/viewtopic.php?t=17302)
- [Mad Scientist](https://twitter.com/mad_scientist92) ([NSAID](https://itch.io/c/4241605/free-art-assets-from-me))
- Photo by [Andrew Neel](https://unsplash.com/@andrewtneel) on [Unsplash](https://unsplash.com/photos/macbook-pro-white-ceramic-mugand-black-smartphone-on-table-cckf4TsHAuw)

### Audio

- [Kenney Interface Sounds](https://kenney.nl/assets/interface-sounds)
- [Knock knock knock](https://pixabay.com/sound-effects/knock-knock-knock-40474/)
- [Writing,Pen,Signature,Paper](https://pixabay.com/sound-effects/writingpensignaturepaper-102967/)
- [rotary phone ring medium](https://pixabay.com/sound-effects/rotary-phone-ring-medium-103869/)
- [Cell Phone Vibrate (High Quality)](https://pixabay.com/sound-effects/cell-phone-vibrate-high-quality-34034/)

### Font

- [Queensides Font](https://www.fontspace.com/queensides-font-f90306)

### Music

- Guilain de Coligny

## Ideation

- [Excalidraw](https://excalidraw.com/#json=y8nO6uwZN7OQLXonmG9WB,TJgAuz71GFU8QkH8YdFVoA)
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
