from graphene.types import Scalar
from graphql.language import ast
from graphene.types.scalars import MIN_INT, MAX_INT


class BigInteger(Scalar):
    @staticmethod
    def serialize(value):
        value = int(value)
        if value > MAX_INT or value < MIN_INT:
            return float(int(value))
        return value

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.IntValue):
            num = int(node.value)
            if num > MAX_INT or num < MIN_INT:
                return float(int(num))
            return num

    @staticmethod
    def parse_value(value):
        value = int(value)
        if value > MAX_INT or value < MIN_INT:
            return float(int(value))
        return value
