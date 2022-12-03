cmake_minimum_required(VERSION 3.16)
project(tag_viewer)

find_package(glfw3 REQUIRED)

add_executable(tag_viewer textures.cpp tgaimage.cpp)
target_link_libraries(tag_viewer glfw)
target_include_directories(tag_viewer PRIVATE ${GLAD_INCLUDE})

add_custom_command(TARGET tag_viewer POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_if_different ${CMAKE_SOURCE_DIR}/4.1.texture.vs ${CMAKE_BINARY_DIR}/4.1.texture.vs
    COMMAND ${CMAKE_COMMAND} -E copy_if_different ${CMAKE_SOURCE_DIR}/4.1.texture.fs ${CMAKE_BINARY_DIR}/4.1.texture.fs
    )
