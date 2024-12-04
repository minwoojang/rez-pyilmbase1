CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(openexr_version ${PYILMBASE_VERSION})

set(url_openexr https://github.com/openexr/openexr.git)
set(tag_openexr v${openexr_version})

message(STATUS  ${PROJECT_BINARY_DIR})
message(STATUS  ${PROJECT_BINARY_DIR})
message(STATUS  ${PROJECT_BINARY_DIR})


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

# Just Clone and checkout the right tag.
# The build is made in the next External Command.
ExternalProject_add(
  openexr
  GIT_REPOSITORY ${url_openexr}
  GIT_TAG ${tag_openexr}
  PREFIX openexr
  UPDATE_COMMAND ""
  CONFIGURE_COMMAND ""
  BUILD_COMMAND ""
  INSTALL_COMMAND ""
)

ExternalProject_add(
    ilmbase
    DEPENDS openexr
    DOWNLOAD_COMMAND ""
    PREFIX ilmbase
    SOURCE_DIR ${PROJECT_BINARY_DIR}/openexr/src/openexr/PyIlmBase
    UPDATE_COMMAND ./bootstrap
    CONFIGURE_COMMAND ./configure --disable-boostpythontest --prefix=${CMAKE_INSTALL_PREFIX} --with-pic --disable-ilmbasetest --with-ilmbase-prefix=$ENV{REZ_ILMBASE_ROOT} --with-boost-include-dir=$ENV{REZ_BOOST_ROOT}/include --with-boost-lib-dir=$ENV{REZ_BOOST_ROOT}/lib --with-python-include-dir=$ENV{REZ_PYTHON_ROOT}/include/python3.9 --with-python-lib-dir=$ENV{REZ_PYTHON_ROOT}/lib
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make ${make_args}
    CMAKE_ARGS -DBOOST_INCLUDEDIR=$ENV{REZ_BOOST_ROOT}/include -DBOOST_LIBRARYDIR=$ENV{REZ_BOOST_ROOT}/lib
)

rez_install_files(
    cmake/pyilmbase.cmake
    DESTINATION .
)
