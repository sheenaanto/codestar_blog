from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About


class TestAboutViews(TestCase):

    def setUp(self):
        """
      create About me context for testing
        """

        self.about_context = About(
            title="About Me", content='About content')

        self.about_context.save()

    def test_render_about_with_collaborate_form(self):
        """
       Verifies get request for about me containing a collaboration form
        """
        response = self.client.get(reverse(
            'about'))
        # print(response.context)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About Me", response.content)

        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)

    def test_successful_collaborate_submission(self):
        """Test for posting a collaborate on the about me page"""

        post_data = {
            'name': 'name collaborator',
            'email': 'test@test.com',
            'message': 'This is a test collaboration message.'
        }
        response = self.client.post(reverse(
            'about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Collaboration request received! I endeavour to respond within 2 working days.",
            response.content
        )
