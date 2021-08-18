from loguru._defaults import LOGURU_FORMAT

from app.settings.logger import (
    MAX_FILE_LENGTH,
    format_botx_client_payload,
    format_record,
)


def test_custom_formatter():
    record_dict = {"extra": {}}
    assert format_record(record_dict) == LOGURU_FORMAT + "{exception}\n"

    record_dict = {"extra": {"payload": {}}}
    assert "extra[payload]" in format_record(record_dict)

    incoming_request = {
        "method": "POST",
        "url": "https://cts.ccsteam.ru/api/v3/botx/command/callback",
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer token",
        },
        "query_params": {},
        "request_data": '{"sync_id": "uuid", "recipients": "all", "command_result": {"status": "ok", "body": "", "metadata": {}, "keyboard": [], "bubble": [], "mentions": []}, "file": {"file_name": "d.txt", "data": "data:text/plain;base64, foobar'
        '="}, "opts": {"stealth_mode": false, "notification_opts": {"send": true, "force_dnd": false}}}'.replace(
            "foobar", "foobar" * MAX_FILE_LENGTH * 2
        ),
    }
    format_botx_client_payload(incoming_request)
    file_data = incoming_request["request_data"]["file"]["data"]
    assert file_data.rfind("foobar" * MAX_FILE_LENGTH) == file_data.find(
        "foobar" * MAX_FILE_LENGTH
    )
