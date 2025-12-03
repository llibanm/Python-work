from tp6.unionfind import UnionFind, uf_new, uf_size, uf_find, uf_union


class TestUnionFindNew:
    def test_unionfind_struct(self):
        try:
            UnionFind()
        except NotImplementedError as e:
            assert False, e
        except TypeError:
            assert True

    def test_unionfind_new(self, dsize):
        uf = uf_new(dsize)
        assert isinstance(uf, UnionFind)


class TestUnionFindSize:
    def test_unionfind_size(self, dsize):
        uf = uf_new(dsize)
        assert uf_size(uf) == dsize


class TestUnionFindFindUnion:

    def test_unionfind_find(self, dsize):
        uf = uf_new(dsize)
        for i in range(dsize):
            assert uf_find(uf, i) == i

    def test_unionfind_union(self, dsize):
        uf = uf_new(dsize)
        for i in range(dsize - 1):
            uf = uf_union(uf, i, i + 1)
        for i in range(dsize):
            assert uf_find(uf, i) == 0
