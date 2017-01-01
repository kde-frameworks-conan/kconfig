from conans import ConanFile, tools, CMake
import platform, os, sys
import multiprocessing


framework = "KConfig"
version = "5.29.0"
shortversion = "5.29"

className = framework + "Conan"

class className(ConanFile):
    name = framework
    version = version
    requires = "QtBase/5.7.1@russelltg/stable"
    description = "KDE Config framework"
    settings = "os", "arch", "compiler", "build_type"
    
    options = {}
    default_options = {}
    
    url = "https://github.com/kde-frameworks-conan/%s" % name
    license = "LGPLv2"
    
    folder_name = "%s-%s" % (name.lower(), version)
    
    def config_options(self):
        pass
    
    def configure(self):
        pass
    
    def source(self):
        zip_name = "%s.zip" % self.folder_name 
        url = "http://download.kde.org/stable/frameworks/%s/%s" % (shortversion, zip_name)
        self.output.info("Downloading %s..." % url)
        tools.download(url, zip_name)
        tools.unzip(zip_name)
        os.unlink(zip_name)
    
    def build(self):
        cm = CMake(self.settings)
        
        print(self.folder_name)
        self.run('cmake -DCMAKE_INSTALL_PREFIX="%s" %s %s' % 
                 (os.path.join(self.conanfile_directory, "install"), 
                  self.conanfile_directory + "/" + self.folder_name, 
                  cm.command_line))
        if platform.os == "Windows":
            self.run("cmake --build . %s" % cm.build_config)
        else:
            self.run("make -j %d" % multiprocessing.cpu_count())
        
        self.run("cmake --build . %s --target install" % cm.build_config)
        
    def package(self):
        print("packaging!")
        self.copy("*", dst="include", src="install/include")
        
        self.copy("*", dst="lib", src="install/lib")
        self.copy("*", dst="lib", src="install/lib64")
        
        self.copy("*", dst="bin", src="install/bin")
        
        self.copy("*", dst="mkspecs", src="install/mkspecs")
        
        self.copy("*", dst="share", src="install/share")
        
