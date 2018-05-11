import cx_Oracle


class DBSerializer:

    # serialized_data_list should be a list of lists like [class_name, [attrs, types, values]]
    @staticmethod
    def serialize(serialized_data_list):
        for instance_data in serialized_data_list:
            serialized_instance_dict_list = instance_data[1]
            for i in range(len(serialized_instance_dict_list[1])):
                if serialized_instance_dict_list[1][i] == 'str':
                    serialized_instance_dict_list[1][i] = 'VARCHAR(50)'
                elif serialized_instance_dict_list[1][i] in ('int', 'float'):
                    serialized_instance_dict_list[1][i] = 'NUMBER'
                else:
                    raise Exception('Such type of attribute can not be serialized')

    @staticmethod
    def deserialize(serialized_data_list):
        pass


class DBSaver:

    # data is the list of lists like [class_name, [attrs, types, values]]
    @staticmethod
    def save(data):

        DBSerializer.serialize(data)
        data.sort(key=lambda instance_data: instance_data[0]) # sort by class_name

        obj_dict = {}
        max_length = 0
        for elem in data:
            if not obj_dict[elem[0]]:
                obj_dict[elem[0]] = elem[1]
            max_length = max(len(elem[0]), max_length)

        for key, elem in obj_dict:
            con = cx_Oracle.connect("Game", "game2000", "User-PC/XE")

            cursor = con.cursor()

            cursor.execute("""CREATE TABLE %s()""" %(key))
            for attr_data in elem:
                cursor.execute("""ALTER TABLE %s""")

    # Vitaliy took 100 grivnas from you


class DBLoader:

    @staticmethod
    def load():
        pass