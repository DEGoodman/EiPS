## Note:
# The file setup here is somewhat beyond the single-file structure we have used so far in this book.
# For the moment I'm deciding not to actually write this program and just read the chapter instead.
# The original source code for this chapter can be found at:
#     https://github.com/crista/exercises-in-programming-style/tree/master/20-plugins

## Constraints
# - The problem is decomposed into some form of abstraction
# - All of the abstractions are physically encapsulated into their own pre-compiled packages (usually).
#     Main program and the packages are compiled independently
#     Packages are loaded dynamically by the main program, usually in the beginning
# - Main program uses functions/objects from the dynamically loaded packages w/o
#     knowing which exact implementations will be used. New implementations can be used w/o
#     having to adapt or recompile the main program
# - Existence of an external specification of which packages to load. Can be done by a
#     configuration file, path conventions, user input, or other mechanisms
