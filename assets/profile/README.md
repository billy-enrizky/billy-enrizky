# Profile visuals

The GitHub profile README embeds the animated `profile-focus.gif` and links to
the static `profile-focus.png` poster. A `<picture>` source selects the PNG when
the browser requests reduced motion. Both show three separate areas of work:
LLM inference, browser tooling, and applied research.

`index.html` is the HyperFrames source. It uses local CSS keyframes, the local
Geist font, original vector icons, and the existing OpenBrowser project mark.
It does not load external assets or display client data or a personal photo.

The OpenBrowser mark came from the profile owner's existing project artwork.
The four SVG icons were drawn for this profile. Geist is distributed under the
SIL Open Font License in `assets/fonts/geist-OFL.txt`.

## Rebuild

Run these commands from the repository root:

```sh
(cd assets/profile && npm run check && npm run snapshot && npm run render)
ffmpeg -ss 1.35 -i assets/profile/profile-focus.gif -frames:v 1 \
  -update 1 assets/profile/profile-focus.png
```

The GIF loops for six seconds at 15 frames per second. The animation returns to
its starting visual state at each loop boundary. The poster provides a still
alternative. HyperFrames account usage remains unverified when no subscription
login is available; these commands use the local renderer.
