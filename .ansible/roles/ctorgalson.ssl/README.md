# Ansible Role SSL

![](https://github.com/ctorgalson/ansible-role-ssl/workflows/Molecule%20Test/badge.svg)

This role creates and manages an arbitrary, variable-ized set of SSL-related directories and files, and/or creates a set of one or more self-signed SSL certificates on the remote machine.

## Notes

- This role _only_ manages files and directories. It does not configure webservers or include webserver handlers.
- SSL key and related files should be encrypted with a tool like `ansible-vault` if they're stored in your repository.

## Dependencies

This role requires the Python package `pyOpenSSL` (because the `openssl_privatekey`, `openssl_csr`, and `openssl_certificate` Ansible modules use it).

## Role Variables

| Variable name     | Default value | Description |
|-------------------|---------------|-------------|
| `ssl_directories` | `[]`          | A list of remote directories to create or configure. Supports the `path`, `owner`, `group`, and `mode` parameters from the Ansible File module. |
| `ssl_files`       | `[]`          | A list of SSL keys and certificates to copy to the remote server. Supports the `content`, `src`, `dest`, `owner`, `force`, `group`, and `mode` parameters from the Ansible Copy module. |
| `ssl_self_files`       | `[]`          | A list of paths for SSL key, csr, and certificate, plus the common name. Available properties are `key_path`, `crt_path`, `csr_path`, and `csr_common_name`. |

## Example Playbook

The following playbook creates/configures/uploads:

  - Pre-existing SSL files and directories:
    - `/etc/ssl/certs`
    - `/etc/ssl/private`
    - `/etc/ssl/certs/www.example.com.crt`
    - `/etc/ssl/private/www.example.com.key`
  - Self-signed SSL cert, key, csr, and directories:
    - `/etc/ssl/self/certs`
    - `/etc/ssl/self/private`
    - `/etc/ssl/self/certs/www.example.com-key.pem`
    - `/etc/ssl/self/certs/www.example.com-crt.pem`
    - `/etc/ssl/self/private/www.example.com.csr`

For more information and tests, see the repository's `molecule/` directory.

    - hosts: all
      vars:
        ssl_directories:
          - path: "/etc/ssl/certs"
            owner: root
            group: root
            mode: "u=rwx,go=rx"
          - path: "/etc/ssl/private"
            owner: root
            group: root
            mode: "u=rwx,go=rx"
        ssl_files:
          - src: "{{ playbook_dir }}/certs/www.example.com.crt"
            dest: "/etc/ssl/certs/www.example.com.crt"
            owner: root
            group: root
            mode: "u=rw,go=r"
          - content: "{{ lookup('file', playbook_dir + '/certs/www.example.com.key') }}"
            dest: "/etc/ssl/private/www.example.com.key"
            owner: root
            group: root
            mode: "u=rw,go="
        ssl_self_files:
          - key_path: "/etc/ssl/self/certs/www.example.com-key.pem"
            crt_path: "/etc/ssl/self/certs/www.example.com-crt.pem"
            csr_path: "/etc/ssl/self/private/www.example.com.csr"
            csr_common_name: "www.example.com"
      roles:
        - role: ansible-role-ssl

## License

GPLv3
