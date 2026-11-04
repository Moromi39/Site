import unittest

# Change this to wherever extract_title lives in your project
from extracttitle import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_basic_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_title_with_surrounding_whitespace(self):
        self.assertEqual(extract_title("#   Hello World   "), "Hello World")

    def test_title_with_multiple_words(self):
        self.assertEqual(extract_title("# My Great Page"), "My Great Page")

    def test_title_not_on_first_line(self):
        md = "Some intro text\n\n# The Title\n\nMore text"
        self.assertEqual(extract_title(md), "The Title")

    def test_title_followed_by_content(self):
        md = "# Title\n\nParagraph one.\n\nParagraph two."
        self.assertEqual(extract_title(md), "Title")

    def test_ignores_h2(self):
        md = "## Subheading\n\n# Real Title"
        self.assertEqual(extract_title(md), "Real Title")

    def test_ignores_h3_and_deeper(self):
        md = "### Third\n#### Fourth\n# Real Title"
        self.assertEqual(extract_title(md), "Real Title")

    def test_first_h1_wins(self):
        md = "# First\n\n# Second"
        self.assertEqual(extract_title(md), "First")

    def test_inline_markdown_is_preserved(self):
        self.assertEqual(extract_title("# Hello **bold** world"), "Hello **bold** world")

    def test_hash_inside_title(self):
        self.assertEqual(extract_title("# C# is fun"), "C# is fun")

    def test_windows_line_endings(self):
        md = "intro\r\n# Title\r\nbody"
        self.assertEqual(extract_title(md), "Title")

    def test_no_title_raises(self):
        with self.assertRaises(Exception):
            extract_title("Just a paragraph with no heading.")

    def test_only_h2_raises(self):
        with self.assertRaises(Exception):
            extract_title("## Only a subheading")

    def test_empty_string_raises(self):
        with self.assertRaises(Exception):
            extract_title("")

    def test_hash_without_space_raises(self):
        with self.assertRaises(Exception):
            extract_title("#NoSpace")

    def test_lone_hash_raises(self):
        with self.assertRaises(Exception):
            extract_title("#")

    def test_hash_in_middle_of_line_raises(self):
        with self.assertRaises(Exception):
            extract_title("not a heading # Title")


if __name__ == "__main__":
    unittest.main()
