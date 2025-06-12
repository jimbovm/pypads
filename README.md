# pypads

`pypads` is a Python implementation of [Nasca Octavian Paul's PADsynth algorithm](https://zynaddsubfx.sourceforge.io/doc/PADsynth/PADsynth.htm).

It uses the algorithm to generate perfectly looped samples which can sound like polysynths, bells, strings, choirs or some unearthly combination of all of them.

For a more intuitive interface to the algorithm, try [ZynAddSubFx](https://zynaddsubfx.sourceforge.io/) or [padthv1](https://padthv1.sourceforge.io/). `pypads` is more for generating clean PCM samples to load into samplers or sample-and-synthesis instruments.

## System requirements

Requires `numpy` and `scipy`. Only tested on Linux, but should run anywhere.