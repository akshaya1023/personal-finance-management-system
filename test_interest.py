import pytest
from unittest.mock import patch
import Interest_Calculator


@patch("Interest_Calculator.loading")
@patch("builtins.input", side_effect=["10000", "10", "2"])
def test_simple_interest(mock_input, mock_loading, capsys):
    Interest_Calculator.simple_interest()

    output = capsys.readouterr().out

    assert "Interest Earned" in output
    assert "2,000.00" in output
    assert "12,000.00" in output


@patch("Interest_Calculator.loading")
@patch("builtins.input", side_effect=["10000", "10", "2"])
def test_compound_interest(mock_input, mock_loading, capsys):
    Interest_Calculator.compound_interest()

    output = capsys.readouterr().out

    assert "Compound Interest" in output
    assert "12,100.00" in output


@patch("Interest_Calculator.loading")
@patch("builtins.input", side_effect=["100000", "7", "5"])
def test_fd_calculator(mock_input, mock_loading, capsys):
    Interest_Calculator.fd_calculator()

    output = capsys.readouterr().out

    assert "Maturity Value" in output
    assert "Interest Earned" in output


@patch("Interest_Calculator.loading")
@patch("builtins.input", side_effect=["500000", "8", "20"])
def test_emi_calculator(mock_input, mock_loading, capsys):
    Interest_Calculator.emi_calculator()

    output = capsys.readouterr().out

    assert "Monthly EMI" in output
    assert "Total Payment" in output
    assert "Loan Amount" in output


@patch("Interest_Calculator.loading")
@patch("builtins.input", side_effect=["5000", "12", "10"])
def test_sip_calculator(mock_input, mock_loading, capsys):
    Interest_Calculator.sip_calculator()

    output = capsys.readouterr().out

    assert "Total Invested" in output
    assert "Maturity Value" in output


@patch("Interest_Calculator.loading")
@patch("builtins.input", side_effect=["50000", "30000"])
def test_budget_analysis(mock_input, mock_loading, capsys):
    Interest_Calculator.budget_analysis()

    output = capsys.readouterr().out

    assert "Monthly Savings" in output
    assert "20,000.00" in output


@patch("Interest_Calculator.loading")
@patch("builtins.input", side_effect=["100", "150"])
def test_profit_calculation(mock_input, mock_loading, capsys):
    Interest_Calculator.profit_loss()

    output = capsys.readouterr().out

    assert "Profit Amount" in output
    assert "50.00%" in output


@patch("Interest_Calculator.loading")
@patch("builtins.input", side_effect=["100", "80"])
def test_loss_calculation(mock_input, mock_loading, capsys):
    Interest_Calculator.profit_loss()

    output = capsys.readouterr().out

    assert "Loss Amount" in output
    assert "20.00%" in output


@patch("Interest_Calculator.loading")
@patch("builtins.input", side_effect=["1000", "20"])
def test_discount_calculator(mock_input, mock_loading, capsys):
    Interest_Calculator.discount_calculator()

    output = capsys.readouterr().out

    assert "Discount Saved" in output
    assert "800.00" in output


@patch("Interest_Calculator.loading")
@patch("builtins.input", side_effect=["120000", "12"])
def test_savings_goal(mock_input, mock_loading, capsys):
    Interest_Calculator.savings_goal()

    output = capsys.readouterr().out

    assert "Monthly Saving Need" in output
    assert "10,000.00" in output


def test_financial_tip(capsys):
    Interest_Calculator.financial_tip()

    output = capsys.readouterr().out

    assert "FINANCIAL TIP OF THE DAY" in output
    assert "20%" in output
