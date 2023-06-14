from utils import dicts


def test_get_val():
    assert dicts.get_val({}, None, 'git') == 'git'
    assert dicts.get_val({'vcs': 'mercurial'}, 'vcs', 'git') == 'mercurial'
    assert dicts.get_val({}, 'vcs', 'bazaar') == 'bazaar'
    assert dicts.get_val({'vcs': 'mercurial', 'tdd': 'test'}, 'tdd', 'git') == 'test'
