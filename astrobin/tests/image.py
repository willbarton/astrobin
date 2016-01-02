# Django
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

class ImageTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'test', 'test@test.com', 'password')

    def tearDown(self):
        self.user.delete()

    def _do_upload(self, filename):
        return self.client.post(
            reverse('image_upload_process'),
            {'image_file': open(filename, 'rb')},
            follow = True)

    def _assert_message(self, response, tags, content):
        storage = response.context[0]['messages']
        for message in storage:
            self.assertEqual(message.tags, tags)
            self.assertTrue(content in message.message)

    def test_upload(self):
        self.client.login(username = 'test', password = 'password')

        # Test file with invalid extension
        response = self._do_upload('astrobin/fixtures/invalid_file')
        self.assertRedirects(
            response,
            reverse('image_upload'),
            status_code = 302,
            target_status_code = 200)
        self._assert_message(response, "error unread", "Invalid image")

        # Test file with invalid content
        response = self._do_upload('astrobin/fixtures/invalid_file.jpg')
        self.assertRedirects(
            response,
            reverse('image_upload'),
            status_code = 302,
            target_status_code = 200)
        self._assert_message(response, "error unread", "Invalid image")

        # Test successful upload
        response = self._do_upload('astrobin/fixtures/test.jpg')
        self.assertRedirects(
            response,
            reverse('image_edit_watermark', kwargs = {'id': 1}),
            status_code = 302,
            target_status_code = 200)

