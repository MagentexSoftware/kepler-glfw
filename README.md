# Kepler GLFW
NodeJS GLFW module

This module will provide the GLFW source code and headers to any node-gyp project

### Prerequisites

Node.js, NPM, Python 2.7

### Developing

Clone and build the module

```
git clone --recurse-submodules -j8 https://github.com/MagentexSoftware/kepler-glfw.git
cd kepler-glfw
npm i
```

## Installing

```npm i --save kepler-glfw```

## Usage

To use the package as a part of a native module, you'll need to include it in your `binding.gyp` file.

```py
{
  'targets': [
    {
      ...
      'include_dirs': [
        "node_modules/kepler-glfw/glfw/include",
      ],
      ...
      'dependencies': [
        "node_modules/kepler-glfw/binding.gyp:kepler-glfw-native",
      ],
      ...
    }
  ]
}
```

## License

This project is licensed under the ZLib License - see the [LICENSE.md](LICENSE.md) file for details
