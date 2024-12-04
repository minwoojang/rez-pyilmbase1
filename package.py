name = "pyilmbase"

version = "2.3.0"

description = \
    """
    IlmBase Python bindings
    """

variants = [['platform-linux', 'arch-x86_64']]

requires = [
    "ilmbase-%s" % (version),
    "python",
    "boost-1.86",
    "gcc-11",
    "numpy"
]

uuid = "repository.pyilmbase"

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python3.9/site-packages")
