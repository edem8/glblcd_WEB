def deco(func):
	def wrap():
		cap_name = func()
		return cap_name.title()
	return wrap

@deco
def print_name():
	return "hello world"


print(print_name())
