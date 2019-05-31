from myblog.models import Post
from myblog.models import Category

from django.test import TestCase
from django.contrib.auth.models import User

class CategoryTestCase(TestCase):

	def test_string_representation(self):
		expected = "A Category"
		c1 = Category(name=expected)
		actual = str(c1)
		self.assertEqual(expected, actual)

class PostTestCase(TestCase):
    fixtures = ['myblog_test_fixture.json', ]

    def test_string_representation(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)

    def setUp(self):
        self.user = User.objects.get(pk=1)
        from myblog.models import Post  # add this import at the top

