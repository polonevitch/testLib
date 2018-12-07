from conans import ConanFile, tools


class HelloConan(ConanFile):
    name = "Stacy"
    version = "0.3"
    settings = "os", "compiler", "build_type", "arch"
    description = "Hello, Stacy!"
    url = "None"
    license = "None"
    author = "None"
    topics = None
    generators = "cmake"

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
