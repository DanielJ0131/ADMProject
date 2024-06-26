"""Test file for the register module."""

from tkinter import ttk
import unittest
from unittest.mock import patch
from app.ui.register_frame import RegisterFrame
from app.src.database import Database


def main():
    """Run the test."""
    TestRegisterFrame.setUp()
    unittest.main()


class TestRegisterFrame(unittest.TestCase):
    """Test class for the RegisterFrame class."""

    def setUp(self):
        """Set up the TestRegisterFrame."""
        # Create the database class
        self.db = Database()

        self.font_size = {
            'xxs': int(1920 / -110),
            'xs': int(1920 / -100),
            's': int(1920 / -90),
            'm': int(1920 / -75),
            'l': int(1920 / -60),
            'xl': int(1920 / -50),
            'xxl': int(1920 / -30),
        }


        # Create register frame
        self.RegisterFrame = RegisterFrame(None, None, self.db, self.font_size)

    def test_RegisterFrame(self):
        """Test the RegisterFrame class."""
        self.assertIsInstance(self.RegisterFrame, RegisterFrame)

    def test_toggle_password(self):
        """Test the toggle_password method."""
        self.pass_entry = ttk.Entry()
        self.show_pass_button = ttk.Button()

        # Set the password entry to show asterisks
        self.pass_entry.configure(show="*")
        self.assertEqual(self.pass_entry.cget("show"), "*")

        # Toggle the password visibility
        self.RegisterFrame.toggle_password()

        # Assert that the password entry now shows plain text
        self.assertEqual(self.pass_entry.get(), "")

    def test_toggle_confirm_password(self):
        """Test the toggle_confirm_password method."""
        self.pass_confirmation_entry = ttk.Entry()
        self.show_confirm_pass_button = ttk.Button()

        # Set the password entry to show asterisks
        self.pass_confirmation_entry.configure(show="*")
        self.assertEqual(self.pass_confirmation_entry.cget("show"), "*")

        # Toggle the password visibility
        self.RegisterFrame.toggle_confirm_password()

        # Assert that the password entry now shows plain text
        self.assertEqual(self.pass_confirmation_entry.get(), "")

    def test_create_account(self):
        """Test the create_account method."""
        self.RegisterFrame.user_entry.insert(0, "test")
        self.RegisterFrame.pass_entry.insert(0, "test")
        self.RegisterFrame.pass_confirmation_entry.insert(0, "test")
        with patch("app.ui.register_frame.messagebox.showinfo"):
            self.RegisterFrame.create_account()

        # Assert that a user has been created
        self.assertTrue(self.db.check_user_existance("test", "test"))
        assert self.RegisterFrame.user_entry.get() == "test"
        assert self.RegisterFrame.pass_entry.get() == "test"
        assert self.RegisterFrame.pass_confirmation_entry.get() == "test"
        self.db.delete_account("test")


if __name__ == "__main__":
    main()
