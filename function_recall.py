# def first():
#     a ="this is first funcion"
#     return a
#
# def second(b=first()):
#     return b
#
#
# print(second())

# class Movie:
#     def __init__(self, name, title):
#         self.name = name.title()
#         self.title = title.title()
#
#     def python(self):
#         if self.name == "Python":
#             print("Knows  python")
#         else:
#             print("JS and C++")
#
# python = Movie("python",".py")
# cpp = Movie("c++","cpp")
# print(python.python())
# print(Movie.python(cpp))

# class person:
#     def __init__(self, name, language):
#         self.name = name
#         self.language = language
#
#
#     def profession(self):
#         return "Technology"
#
# class developer(person):
#     def __init__(self,name,language,skill):
#         super().__init__(name,language)
#         self.skill = skill
#     def programmer(self):
#         print(self.name,self.skill,"is a A Web Developer and knows",self.language)
#
#
# # p = person("M","python")
#
# human = developer("M", "python","webdeveloper")
#
# print(human.profession())


a =7
b = a > 5 and 'a' or 'b'

print(b)