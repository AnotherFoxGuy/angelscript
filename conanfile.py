from conans import ConanFile, CMake, tools


class AngelscriptConan(ConanFile):
    name = "AngelScript"
    version = "2.33"
    license = "zlib"
    url = "https://github.com/AnotherFoxGuy/angelscript/issues"
    description = " AngelScript is an extremely flexible cross-platform scripting library designed to allow applications to extend their functionality through external scripts."
    settings = ("os", "build_type", "arch_build")
    generators = "cmake"
    exports_sources = "cmake*", "include*", "source*", "CMakeLists.txt", "angelscript.pc.in"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
