#/usr/bin/python3

from conan.packager import ConanMultiPackager
import platform


if __name__ == "__main__":
    builder = ConanMultiPackager(visual_runtimes=["MT", "MD"])
    
    if platform.system() == "Windows":
        builder.add_common_builds()
    
    if platform.system() == "Linux":
        for ver in builder.gcc_versions:
            for bt in [ "Release", "Debug"]:
                builder.add(
                    {"arch": "x86_64", 
                     "build_type": bt,
                     "compiler": "gcc",
                     "compiler.version": ver,
                     "compiler.libcxx": "libstdc++11"})
    
    builder.run()
