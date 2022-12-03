cmake_minimum_required(VERSION 3.16)
project(tag_viewer)

find_package(glfw3 REQUIRED)

add_executable(tag_viewer main.cpp tgaimage.cpp)
target_link_libraries(tag_viewer glfw)
