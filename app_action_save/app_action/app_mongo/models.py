from mongoengine import Document, fields

class App_action_statis(Document):
    content = fields.StringField()
    timestamp = fields.StringField()
    type = fields.IntField()
    member_id = fields.StringField()
    device_id = fields.StringField()
    extent = fields.StringField()
    device_resolution = fields.StringField()
    app_channel = fields.StringField()
    system_version = fields.StringField()
    device_type = fields.StringField()
    network_provider = fields.StringField()
    network = fields.StringField()
    app_version = fields.StringField()