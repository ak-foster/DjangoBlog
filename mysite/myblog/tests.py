# add this import at the top
from myblog.models import Post

# and this test method to the PostTestCase
def test_string_representation(self):
    expected = "This is a title"
    p1 = Post(title=expected)
    actual = str(p1)
    self.assertEqual(expected, actual)