import jsonpickle


def serialize_and_write(file, test_data):
    with open(file, "w") as f:
        jsonpickle.set_encoder_options('json', sort_keys=True, indent=2)
        test_data_serialised = jsonpickle.encode(test_data)
        f.write(test_data_serialised)
