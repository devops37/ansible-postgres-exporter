def test_files(host):
    files = [
        "/etc/systemd/system/postgres_exporter.service",
        "/usr/local/bin/postgres_exporter"
    ]
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file


def test_permissions_didnt_change(host):
    dirs = [
        "/etc",
        "/root",
        "/usr",
        "/var"
    ]
    for file in dirs:
        f = host.file(file)
        assert f.exists
        assert f.is_directory
        assert f.user == "root"
        assert f.group == "root"


def test_user(host):
    assert host.group("postgres").exists
    assert "postgres" in host.user("postgres").groups
    assert host.user("postgres").shell == "/bin/bash"
    assert host.user("postgres").home == "/var/lib/pgsql"


def test_service(host):
    s = host.service("postgres_exporter")
    assert s.is_running
    assert s.is_enabled


def test_socket(host):
    sockets = [
        "tcp://127.0.0.1:9187"
    ]
    for socket in sockets:
        s = host.socket(socket)
        assert s.is_listening
