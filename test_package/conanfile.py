from conans.model.conan_file import ConanFile
from conans import CMake
import os


channel = os.getenv("CONAN_CHANNEL", "stable")
username = os.getenv("CONAN_USERNAME", "russelltg")


class DefaultNameConan(ConanFile):
    settings = "os", "compiler", "arch", "build_type"
    requires = "KConfig/5.29.0@%s/%s" % (username, channel)
    generators = "cmake"

    def build(self):
        #cmake = CMake(self.settings)
        
        #self.run('echo %s' % self.conanfile_directory)
        #self.run('cmake %s %s' % (self.conanfile_directory, cmake.command_line))
        #self.run("cmake --build . %s" % cmake.build_config)
        pass
    def test(self):
        pass
    
