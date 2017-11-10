Colors
======

Always use class names to target data-driven colors.

Our convention for color class names is:

::

  .{palette}-{length}-{index}-{property}

- **palette**

    The name of the palette. For example, `gop` or `dem`.

- **length**

    If applicable, the length of the palette ramp. For example, `8` for an 8-color palette ramp.

- **index**

    If applicable, the index of the color within the palette ramp to use. For example, `1` for the first color in the palette ramp.

- **property**

  The property to target with the specified color. For example, `stroke` or `fill`. Concatenate multipart properties into camel-case, for example, `backgroundColor`.


Some example of fully specified color classes:

- ``.gop-4-1-stroke``
- ``.gop-fill``
- ``.dem-backgroundColor``
