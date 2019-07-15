from tortoise.models import Model
from tortoise import fields


class Todo(Model):
    # Defining `id` field is optional, it will be defined automatically
    # if you haven't done it yourself
    id = fields.IntField(pk=True)
    body = fields.CharField(max_length=255)
    is_finished = fields.BooleanField()
    created_at = fields.DatetimeField(auto_now=True)
    updated_at = fields.DatetimeField(auto_now_add=True)

    # Defining ``__str__`` is also optional, but gives you pretty
    # represent of model in debugger and interpreter
    def __str__(self):
        return self.body


class Token(Model):
    id = fields.IntField(pk=True)
    body = fields.CharField(max_length=255)
    is_finished = fields.BooleanField()
    created_at = fields.DatetimeField(auto_now=True)
    updated_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.body