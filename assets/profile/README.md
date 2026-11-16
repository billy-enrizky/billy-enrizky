# Profile visuals

The GitHub profile README shows an animated banner and picks a still image for
readers who request reduced motion or a dark theme.

| File | Used when |
| --- | --- |
| `profile/profile-focus.gif` | Default: light theme, motion allowed |
| `profile/profile-focus.png` | Reduced motion, light theme |
| `profile-dark/profile-focus-dark.gif` | Dark theme (see the note below) |
| `profile-dark/profile-focus-dark.png` | Reduced motion, dark theme |

The page is one file, `profile/index.html`, rendered by HyperFrames. The dark
version is generated from it by `profile/make-dark.py`, which changes only six
colour variables, so the two never drift apart. Do not edit the dark file by hand.

GitHub does not offer a theme-specific GIF in a README. The dark GIF is kept
so the dark still and the dark animation match, and the README selects them with
`<picture>` where the reader's browser supports it.

The composition loads GSAP 3.14.2 from `profile/assets/vendor/gsap.min.js`
(licence in `gsap-LICENSE.txt`). No file is loaded from the network at render
time, and no value depends on the clock, a random number or the reader's device.

## Rebuild

From `assets/profile`:

```sh
npx --yes hyperframes@0.9.55 check .
npx --yes hyperframes@0.9.55 render . --format gif --fps 15 --gif-loop 0 --output profile-focus.gif
ffmpeg -ss 4.8 -i profile-focus.gif -frames:v 1 profile/profile-focus.png
```

The dark project repeats the same steps from `assets/profile-dark`. The posters
are taken at 4.8 s, which is the fully composed frame. The GIF loops every
9.6 s and its final frame is the start of the next loop.

The project check reports two structural warnings, `nested_structure_needs_subcomposition`,
which are accepted: this is one banner, and splitting it into scene files would
add files without changing the output.
