from conans import ConanFile, CMake, tools


class AngelscriptConan(ConanFile):
    name = "AngelScript"
    version = "2.32"
    license = "zlib"
    url = "https://github.com/AnotherFoxGuy/angelscript/issues"
    description = " AngelScript is an extremely flexible cross-platform scripting library designed to allow applications to extend their functionality through external scripts."
    settings = "os", "compiler", "build_type", "arch"
    #options = {"shared": [True, False]}
    #default_options = "shared=False"
    generators = "cmake"
    exports_sources = "include*", "source*", "CMakeLists.txt", "angelscript.pc.in"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["angelscript"]
