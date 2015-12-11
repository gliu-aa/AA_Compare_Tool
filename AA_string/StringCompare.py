from AA_constant import constantfrom diff_match_patch import diff_match_patch as diffclass StringCompare:    """A utility class to compare string"""    @classmethod    def string_distance(cls, source, target):        """        get string distance between source and target        - return 0: same        - return -1: reject        - return [1, 225]: normal        :param source:        :param target:        :return: string distance        """        changes = cls.string_different(source, target)        distance = 0        for tag, content in changes:            if tag is not 0:                distance += len(content)        return distance    @classmethod    def string_different(cls, source, target):        """        :param source:        :param target:        :return: Array of changes        """        if source == target:            return [(constant.EQUAL, target)]        elif len(source) == 0:            return [(constant.INSERT, target)]        elif len(target) == 0:            return [(constant.DELETE, source)]        elif len(source) > 255 or len(target) > 255:            raise ValueError("Large Input(source or target)")        d = diff()        return d.diff_main(source, target)