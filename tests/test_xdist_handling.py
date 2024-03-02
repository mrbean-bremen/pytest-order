from textwrap import dedent

import pytest


def test_collecting_symlinks(tmpdir):
    testname = str(tmpdir.join("first_test.py"))
    with open(testname, "w") as fi:
        fi.write(
            dedent(
                """
            def test_1():
                pass
            """
            )
        )

    args = ["-v", str(tmpdir)]
    ret = pytest.main(args, [])
    assert ret == 0
