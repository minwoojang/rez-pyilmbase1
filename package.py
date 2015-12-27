name = "pyilmbase"

version = "2.1.0"

description = \
    """
    IlmBase Python bindings
    """

variants = [
    ["platform-linux"]
]

requires = [
    "ilmbase-%s" % (version),
    "python",
    "boost"
]

uuid = "repository.pyilmbase"

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
