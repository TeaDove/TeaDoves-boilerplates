from package_name import main


class TestClass:
    def test_hello(self):
        result = main.hello_world("TeaDove")
        print(result)
        assert result == "Hello, TeaDove"
