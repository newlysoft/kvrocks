import redis
from assert_helper import *
from conn import *


def test_siadd():
    conn = get_redis_conn()
    key = "test_siadd"
    ret = conn.execute_command("siadd", key, 1, 2, 3, 4)
    assert(ret == 4)

    ret = conn.delete(key)
    assert(ret == 1)


def test_sirem():
    conn = get_redis_conn()
    key = "test_sirem"
    ret = conn.execute_command("siadd", key, 1)
    assert (ret == 1)
    ret = conn.execute_command("sirem", key, 1)
    assert(ret == 1)


def test_sicard():
    conn = get_redis_conn()
    key = "test_sicard"
    ret = conn.execute_command("siadd", key, 1, 2, 3, 4)
    assert (ret == 4)
    ret = conn.execute_command("sicard", key)
    assert (ret == 4)

    ret = conn.delete(key)
    assert (ret == 1)


def test_sirange():
    conn = get_redis_conn()
    key = "test_sirange"
    ret = conn.delete(key)
    ret = conn.execute_command("siadd", key, 1, 2, 3, 4, 60, 231, 9999)
    assert (ret == 7)
    ret = conn.execute_command("sirange", key, 0, 20)
    assert (ret == ['1', '2', '3', '4', '60', '231', '9999'])
    ret = conn.execute_command("sirange", key, 0, 2)
    assert (ret == ['1', '2'])
    ret = conn.execute_command("sirange", key, 3, 2)
    assert (ret == ['4', '60'])
    ret = conn.execute_command("sirange", key, 0, 2, "cursor", 3)
    assert (ret == ['4', '60'])

    ret = conn.delete(key)
    assert(ret == 1)


def test_sirevrange():
    conn = get_redis_conn()
    key = "test_sirevrange"
    ret = conn.delete(key)
    ret = conn.execute_command("siadd", key, 1, 2, 3, 4, 60, 231, 9999)
    assert (ret == 7)
    ret = conn.execute_command("sirevrange", key, 0, 20)
    assert (ret == ['9999', '231', '60', '4', '3', '2', '1'])
    ret = conn.execute_command("sirevrange", key, 0, 2)
    assert (ret == ['9999', '231'])
    ret = conn.execute_command("sirevrange", key, 3, 2)
    assert (ret == ['4', '3'])
    ret = conn.execute_command("sirevrange", key, 0, 2, "cursor", 3)
    assert (ret == ['2', '1'])

    ret = conn.delete(key)
    assert(ret == 1)