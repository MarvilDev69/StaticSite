import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty_props(self):
        # Test when props is None
        node = HTMLNode("p", "Hello, world!")
        self.assertEqual(node.props_to_html(), "")
        
        # Test when props is an empty dict
        node = HTMLNode("p", "Hello, world!", props={})
        self.assertEqual(node.props_to_html(), "")
        
    def test_props_to_html_single_prop(self):
        # Test with a single property
        node = HTMLNode("a", "Click me!", props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')
        
    def test_props_to_html_multiple_props(self):
        # Test with multiple properties
        node = HTMLNode(
            "a", 
            "Click me!", 
            props={
                "href": "https://example.com",
                "target": "_blank",
                "class": "link"
            }
        )
        # The order of properties in a dictionary isn't guaranteed, so we need to check
        # that each property is in the output string
        result = node.props_to_html()
        self.assertIn(' href="https://example.com"', result)
        self.assertIn(' target="_blank"', result)
        self.assertIn(' class="link"', result)
        # Also check the total length is correct (accounting for spaces)
        expected_length = len(' href="https://example.com" target="_blank" class="link"')
        self.assertEqual(len(result), expected_length)

if __name__ == "__main__":
    unittest.main()