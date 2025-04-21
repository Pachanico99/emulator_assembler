class Mov(Instruction):
    def __init__(self, target, value):
        self.target = target
        self.value = value

    def execute(self, context):
        context.registers[self.target] = self._get_value(self.value, context)

    def _get_value(self, operand, context):
        if operand in context.registers:
            return context.registers[operand]
        return int(operand)
