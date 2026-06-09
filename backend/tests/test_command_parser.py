from app.chat.command_parser import CommandParser

def test_command_parser_valid():
    parser = CommandParser()

    res = parser.parse("/lisa plan build auth system")
    assert res.is_valid
    assert res.command == "/lisa plan"
    assert res.args == "build auth system"

def test_command_parser_nl_alias():
    parser = CommandParser()
    res = parser.parse("Lisa plan this: deploy app")
    assert res.is_valid
    assert res.command == "/lisa plan"
    assert res.args == "deploy app"

def test_command_parser_invalid():
    parser = CommandParser()
    res = parser.parse("hello world")
    assert not res.is_valid
    assert res.command == "unknown"
