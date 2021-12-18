import driver_pytest as dp

n = 7

def test_build():  
    for i in range(1, n + 1):
        assert dp.build("example" + str(i) + ".nate")

def test_compile():
    for i in range(1, n + 1):
        name = "example" + str(i)
        assert dp.compile(name + ".nate", name)

def test_run():
    for i in range(1, n + 1):
        assert dp.run("example" + str(i) + ".nate")
