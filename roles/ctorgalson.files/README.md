# Ansible Role Files

[![Build Status](https://travis-ci.com/ctorgalson/ansible-role-files.svg?branch=master)](https://travis-ci.com/ctorgalson/ansible-role-files)

This role simplifies the use of Ansible to create files, directories, and links.

## Role Variables

- `files_files` (default `[]`): a list of objects using Ansible File module
  params. The following File module parameters are not supported:
    - `access_time`
    - `access_time_format`
    - `attributes`
    - `follow`
    - `modification_time`
    - `modification_time_format`
    - `selevel`
    - `serole`
    - `seuser`
    - `unsafe_writes`

  The other File module parameters are used as when creating File tasks
  directly.

## Example Playbook

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    ---
    - hosts: all
      roles:
        - role: ansible-role-files
          vars:
            files_files:
              # Create directory.
              - path: "/home/lorem"
                owner: "lorem"
                group: "lorem"
                mode: "u=rwx,go="
                state: directory
              # Create directory recursively.
              - path: "/home/lorem/foo/bar"
                owner: "lorem"
                group: "lorem"
                state: directory
                mode: "u=rwx,g=rx,o="
              # Create an empty file.
              - path: "/home/lorem/baz"
                owner: "lorem"
                group: "lorem"
                state: touch
              # Change the properties of an existing file.
              - path: "/home/lorem/.bashrc"
                owner: "lorem"
                group: "lorem"
                mode: "u=rw,go=r"
                state: file
              # Remove a file, directory, or link.
              - path: "/home/lorem/DELETE"
                state: absent
              # Create a symlink.
              - src: "/home/lorem/foo/bar"
                dest: "/home/lorem/foobar"
                owner: "lorem"
                group: "lorem"
                state: link
              # Force-create a symlink.
              - src: "/home/lorem/foo/bar"
                dest: "/home/lorem/fubar-link"
                owner: "lorem"
                group: "lorem"
                state: link
                force: true

## License

GPLv3
