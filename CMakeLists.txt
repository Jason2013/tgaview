cmake_minimum_required(VERSION 3.16)
project(tga_viewer)

set_property(GLOBAL PROPERTY USE_FOLDERS ON)

list(PREPEND CMAKE_PREFIX_PATH ${CMAKE_SOURCE_DIR}/external/glfw)
find_package(glfw3 REQUIRED)

add_subdirectory(external/glad)
add_subdirectory(external/getopt)
add_subdirectory(external/tgaimage)
add_subdirectory(shaders)

set_target_properties(glad PROPERTIES FOLDER external)
set_target_properties(getopt PROPERTIES FOLDER external)
set_target_properties(tgaimage PROPERTIES FOLDER external)


add_executable(tgaview src/textures.cpp src/shader_s.h)
target_include_directories(tgaview PRIVATE src)

target_link_libraries(tgaview glfw glad getopt tgaimage shaders)
