{
  'targets': [
    {
      'target_name': 'kepler-glfw-native',
      'type': 'shared_library',
      'sources': [
        "glfw/src/context.c",
        "glfw/src/init.c",
        "glfw/src/input.c",
        "glfw/src/monitor.c",
        "glfw/src/vulkan.c",
        "glfw/src/window.c"
      ],
      'include_dirs': ["<!@(node -p \"require('node-addon-api').include\")", "glfw/include"],
      "conditions":[
        ["OS=='linux'", {
          "sources": [
              "glfw/src/x11_init.c",
              "glfw/src/x11_monitor.c",
              "glfw/src/x11_window.c",
              "glfw/src/xkb_unicode.c",
              "glfw/src/posix_time.c",
              "glfw/src/posix_thread.c",
              "glfw/src/glx_context.c",
              "glfw/src/egl_context.c",
              "glfw/src/osmesa_context.c",
              "glfw/src/linux_joystick.c"
          ],
          "defines": [ "_GLFW_X11" ],
          "libraries": [ "-lX11" ]
        }],
        ["OS=='mac'", {
          "sources": [
              "glfw/src/cocoa_init.m",
              "glfw/src/cocoa_joystick.m",
              "glfw/src/cocoa_monitor.m",
              "glfw/src/cocoa_window.m",
              "glfw/src/cocoa_time.c",
              "glfw/src/posix_thread.c",
              "glfw/src/nsgl_context.m",
              "glfw/src/egl_context.c",
              "glfw/src/osmesa_context.c"
          ],
          "defines": [ "_GLFW_COCOA" ]
        }],
        ["OS=='win'", {
          "sources": [
              "src/glfw/win32_init.c",
              "src/glfw/win32_joystick.c",
              "src/glfw/win32_monitor.c",
              "src/glfw/win32_time.c",
              "src/glfw/win32_thread.c",
              "src/glfw/win32_window.c",
              "src/glfw/wgl_context.c",
              "src/glfw/egl_context.c",
              "src/glfw/osmesa_context.c"
          ],
          "defines": [ "_GLFW_WIN32" ]
        }]
      ],
      'dependencies': ["<!(node -p \"require('node-addon-api').gyp\")"],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'xcode_settings': {
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'CLANG_CXX_LIBRARY': 'libc++',
        'MACOSX_DEPLOYMENT_TARGET': '10.7'
      },
      'msvs_settings': {
        'VCCLCompilerTool': { 'ExceptionHandling': 1 },
      }
    }
  ]
}
