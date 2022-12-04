find_package(Python3 COMPONENTS Interpreter REQUIRED)

add_custom_command(OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/shaders.h
        ${CMAKE_CURRENT_BINARY_DIR}/shaders.cpp
    COMMAND echo ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/generate_shader_src.py ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_BINARY_DIR} shaders texture.fs texture.vs
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/generate_shader_src.py ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_BINARY_DIR} shaders texture.fs texture.vs
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    COMMENT "show a message"
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/generate_shader_src.py
        ${CMAKE_CURRENT_SOURCE_DIR}/texture.fs
        ${CMAKE_CURRENT_SOURCE_DIR}/texture.vs
)

add_library(shaders STATIC 
    ${CMAKE_CURRENT_BINARY_DIR}/shaders.h
    ${CMAKE_CURRENT_BINARY_DIR}/shaders.cpp
)
target_include_directories(shaders PUBLIC ${CMAKE_CURRENT_BINARY_DIR})
