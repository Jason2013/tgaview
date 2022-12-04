# Simple TGA Image Viewer

[![Windows Build](https://github.com/Jason2013/tgaview/actions/workflows/windows.yml/badge.svg?branch=master)](https://github.com/Jason2013/tgaview/actions/workflows/windows.yml?query=branch%3Amaster)

A simple TGA image viewer with the ability to scale the image.

## How to use

```
Usage: tgaview [-s SCALE] [-h] <image.tga>
Options:
 -s SCALE, --scale SCALE  = Scale factor, default: 1
 -h, --help               = Show this usage help
```

## How to build

Requires:

* `Visual Studio 2019` and above.
* `CMake` 3.16 and above.

Build commands:

```
cmake -S . -B build
cmake --build build
```
