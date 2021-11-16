import driver_pytest as dp

n = 2

def test_build():
    for i in range(1, n + 1):
        dp.build("test/example" + str(i) + ".nateve")

def test_compile():
    for i in range(1, n + 1):
        dp.compile("test/example" + str(i) + ".nateve")

def test_run():
    for i in range(1, n + 1):
        dp.run("test/example" + str(i) + ".nateve")