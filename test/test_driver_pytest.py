import driver_pytest as dp

n = 7

def test_build():
    for i in range(1, n + 1):
        dp.build("example" + str(i) + ".nate")
        f1 = open("example" + str(i) + ".py", "r")
        f2 = open("test/example" + str(i) + ".py", "r")
        assert f1.read() == f2.read()
        f1.close()
        f2.close()

def test_compile():
    for i in range(1, n + 1):
        dp.compile("example" + str(i) + ".nate")

def test_run():
    for i in range(1, n + 1):
        dp.run("example" + str(i) + ".nate")
