cmake_minimum_required(VERSION 3.11)
project(dnp3_test)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(opendnp3 REQUIRED)

add_executable(master-demo     master/main.cpp)
add_executable(outstation-demo outstation/main.cpp)

target_link_libraries(master-demo     PRIVATE opendnp3)
target_link_libraries(outstation-demo PRIVATE opendnp3)