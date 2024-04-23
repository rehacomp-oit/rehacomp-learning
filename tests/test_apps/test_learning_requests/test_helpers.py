from collections import namedtuple

from server.apps.learning_requests.helpers import build_upload_path


learning_request_model_stub = namedtuple('learning_request_model_stub', ('target_name',))


def test_build_upload_path() -> None:
    expected_path = 'learning_requests/testfile.test'
    fake_model = learning_request_model_stub(target_name='testfile')
    actual_path = build_upload_path(fake_model, 'source.test')
    assert expected_path == actual_path
