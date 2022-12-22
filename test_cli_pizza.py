import pytest
from click.testing import CliRunner
from cli_pizza import cli


@pytest.fixture(scope="session")
def runner():
    return CliRunner()


def test_menu(runner):
    result = runner.invoke(cli, ["menu"])
    assert result.exit_code == 0


def test_order_delivery(runner):
    result = runner.invoke(cli, ["order", "Margherita", "--delivery"])
    assert result.exit_code == 0
    assert "Made in" in result.output and "Delivered in" in result.output


def test_order(runner):
    result = runner.invoke(cli, ["order", "Margherita"])
    assert result.exit_code == 0
    assert "Made in" in result.output


def test_order_wrong_pizza(runner):
    result = runner.invoke(cli, ["order", "diablo"])
    assert result.exit_code == 0
    assert "We dont have" in result.output and "Choose between" in result.output


def test_order_wrong_pizza_size(runner):
    result = runner.invoke(cli, ["order", "Pepperoni", "--size=S"])
    assert result.exit_code == 0
    assert "We dont have such pizza size" in result.output


def test_no_pizza(runner):
    result = runner.invoke(cli, "")
    assert result.stdout is not None
