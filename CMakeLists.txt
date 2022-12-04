cmake_minimum_required(VERSION 3.16)
project(tga_viewer)

set_property(GLOBAL PROPERTY USE_FOLDERS ON)

set(CMAKE_PREFIX_PATH ${CMAKE_SOURCE_DIR}/external/glfw;${CMAKE_PREFIX_PATH})
find_package(glfw3 REQUIRED)

add_subdirectory(external/glad)
add_subdirectory(external/getopt)
add_subdirectory(external/tgaimage)

set_target_properties(getopt PROPERTIES FOLDER external)
set_target_properties(tgaimage PROPERTIES FOLDER external)

find_package(Python3 COMPONENTS Interpreter REQUIRED)

add_custom_command(OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/shaders.h
        ${CMAKE_CURRENT_BINARY_DIR}/shaders.cpp
    COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/shaders/generate_shader_src.py ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_BINARY_DIR} shaders texture.fs texture.vs
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    COMMENT "show a message"
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/shaders/generate_shader_src.py
        ${CMAKE_CURRENT_SOURCE_DIR}/shaders/texture.fs
        ${CMAKE_CURRENT_SOURCE_DIR}/shaders/texture.vs
)

add_executable(tgaview textures.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/shaders.h
    ${CMAKE_CURRENT_BINARY_DIR}/shaders.cpp
)

target_link_libraries(tgaview glfw glad getopt tgaimage)

#add_custom_command(TARGET tgaview POST_BUILD
#    COMMAND ${CMAKE_COMMAND} -E copy_if_different ${CMAKE_SOURCE_DIR}/4.1.texture.vs ${CMAKE_BINARY_DIR}/4.1.texture.vs
#    COMMAND ${CMAKE_COMMAND} -E copy_if_different ${CMAKE_SOURCE_DIR}/4.1.texture.fs ${CMAKE_BINARY_DIR}/4.1.texture.fs
#)
