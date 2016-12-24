#/usr/bin/python3

from conan.packager import ConanMultiPackager
import platform


if __name__ == "__main__":
    builder = ConanMultiPackager(visual_runtimes=["MT", "MD"])
    
    if platform.system() == "Windows":
        builder.add_common_builds(visual_versions=[14])
    
    if platform.system() == "Linux":
        for ver in ["6.2"]:
            for bt in [ "Release"]:
                builder.add(
                    {"arch": "x86_64", 
                     "build_type": bt,
                     "compiler": "gcc",
                     "compiler.version": ver,
                     "compiler.libcxx": "libstdc++11"})
    
    builder.run()
