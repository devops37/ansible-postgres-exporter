# Ansible Role: postgres exporter

[![CI](https://github.com/zhan9san/ansible-postgres-exporter/actions/workflows/ci.yml/badge.svg)](https://github.com/zhan9san/ansible-postgres-exporter/actions/workflows/ci.yml)
[![Ansible Rolea](https://img.shields.io/badge/ansible%20role-zhan9san.postgres_exporter-blue.svg)](https://galaxy.ansible.com/zhan9san/postgres_exporter/)
[![GitHub tag](https://img.shields.io/github/tag/zhan9san/ansible-postgres-exporter.svg)](https://github.com/zhan9san/ansible-postgres-exporter/tags)

Inspired by [Ansible Role: node exporter](https://github.com/cloudalchemy/ansible-node-exporter).

## Description

Deploy prometheus [postgres exporter](https://github.com/prometheus-community/postgres_exporter) using ansible.

## Requirements

- Ansible >= 2.7 (It might work on previous versions, but we cannot guarantee it)
- gnu-tar on Mac deployer host (`brew install gnu-tar`)
- Passlib is required when using the basic authentication feature (`pip install passlib[bcrypt]`)

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) and are listed in the table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `postgres_exporter_version` | 0.10.0 | Postgres exporter package version. Also accepts latest as parameter. |
| `postgres_exporter_binary_local_dir` | "" | Allows to use local packages instead of ones distributed on github. As parameter it takes a directory where `postgres_exporter` binary is stored on host on which ansible is ran. This overrides `postgres_exporter_version` parameter |
| `postgres_exporter_web_listen_address` | "0.0.0.0:9187" | Address on which postgres exporter will listen |
| `postgres_exporter_web_telemetry_path` | "/metrics" | Path under which to expose metrics |
| `postgres_exporter_extend_query_path` | "" | Path to a YAML file containing custom queries to run |

## Example

### Playbook

Use it in a playbook as follows:

```yaml
- hosts: all
  roles:
    - zhan9san.postgres_exporter
```

## License

This project is licensed under Apache License. See [LICENSE](/LICENSE) for more details.
