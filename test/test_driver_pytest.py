import driver_pytest as dp

n = 4

def test_build():
    for i in range(1, n + 1):
        dp.build("test/example" + str(i) + ".nateve")
        f1 = open("test/example" + str(i) + ".py", "r")
        f2 = open("test/example" + str(i) + ".txt", "r")
        assert f1.read() == f2.read()
        f1.close()
        f2.close()

def test_compile():
    for i in range(1, n + 1):
        dp.compile("test/example" + str(i) + ".nateve")

def test_run():
    for i in range(1, n + 1):
        dp.run("test/example" + str(i) + ".nateve")